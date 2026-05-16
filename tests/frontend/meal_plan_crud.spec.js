import {test , expect} from '@playwright/test';
import {registerUser, loginUser} from './helpers/auth.js';
import {createRecipeForMealPlan, addMealPlan} from './helpers/meal.js';
import {addRecipe} from './helpers/recipe.js';

test('add meal plan and check it appears on meal plan page', async ({page}) => {
    const uniqueID = Date.now().toString().slice(-6); // Generate a unique ID based on the current timestamp
    const username = `testuser${uniqueID}`;
    const email = `${username}@example.com`;
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    // Create a recipe to use in the meal plan
    const recipeTitle = await createRecipeForMealPlan(page);

    // Add a meal plan using the created recipe
    const mealPlanDetails = await addMealPlan(page, {mealType: 'breakfast', recipe: recipeTitle});

    // Check the meal plan appears on the meal plan page with correct details

    // Navigate to the meal plans page for the week of the meal plan date, because meal plans are displayed by week
    await page.goto(`http://localhost:5000/meal-plans?week_start=${mealPlanDetails.date}`); 
    await expect(page.getByText(recipeTitle)).toBeVisible();
    await expect(page.getByText('Breakfast')).toBeVisible();
});

test('add meal plan with missing fields shows error message', async ({page}) => {
    const uniqueID = Date.now().toString().slice(-6);
    const username = `testuser${uniqueID}`;
    const email = `${username}@example.com`;
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    const recipeTitle = await createRecipeForMealPlan(page);

    // Try to add a meal plan without providing required fields
    await page.goto('http://localhost:5000/meal-plans/add');
    await page.locator('button[type="submit"]').click({force: true}); // Force click to submit the form without filling in required fields

    // Check that an error message is displayed
    const validatioMessage = await page.locator('select[name="recipe_id"]').evaluate((select) => select.validationMessage);
    expect(validatioMessage).toBe('Please select an item in the list.'); // This is the default browser validation message for a required select field
});

test('add meal plan with duplicate date and meal type shows error message', async ({page}) => {
    const uniqueID = Date.now().toString().slice(-6);
    const username = `testuser${uniqueID}`;
    const email = `${username}@example.com`;
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    // Create a recipe to use in the meal plan
    const recipeTitle = await createRecipeForMealPlan(page);

    // Add a meal plan
    const mealPlanDetails = await addMealPlan(page, {mealType: 'lunch', recipe: recipeTitle});

    // Try to add another meal plan with the same date and meal type
    await page.goto(`http://localhost:5000/meal-plans/add?meal_date=${mealPlanDetails.date}&meal_type=${mealPlanDetails.mealType}`);
    await expect(page.locator('select[name="recipe_id"]')).toBeVisible();
    await page.selectOption('select[name="recipe_id"]', {label: recipeTitle});
    await page.locator('button[type="submit"]').click({force: true});

    // Check that an error message is displayed
    await expect(page.getByText(/already have a lunch planned/i)).toBeVisible();
});