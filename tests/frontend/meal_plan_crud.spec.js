import {test , expect} from '@playwright/test';
import {registerUser, loginUser} from './helpers/auth.js';
import {createRecipeForMealPlan, addMealPlan} from './helpers/meal.js';
import {addRecipe} from './helpers/recipe.js';

// Take a screenshot after each test if fail and save it in the screenshots directory
const fs = require('fs');
test.afterEach(async ({page}, testInfo) => {
    const name = testInfo.title.replace(/\s+/g, '_'); // create a filename based on the test title
    const device = testInfo.project.name; // get the device name from the project configuration

    let folder = 'screenshots/failed'; // default folder for failed tests

    if (testInfo.status !== testInfo.expectedStatus) { // only take a screenshot if the test failed
        folder = 'screenshots/failed'; // folder for failed tests
    } else 
    if (testInfo.status === 'passed') {
        folder = 'screenshots/passed'; // folder for passed tests
    }
    await page.screenshot({path: `${folder}/${name}_${device}.png`, fullPage: true}); // take a screenshot after each test
});

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

test('edit meal plan updates successfully and shows updated details on meal plan page', async ({page}) => {
    const uniqueID = Date.now().toString().slice(-6);
    const username = `testuser${uniqueID}`;
    const email = `${username}@example.com`;
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    // Create a recipe to use in the meal plan
    const firstRecipeTitle = await createRecipeForMealPlan(page);

    // Create second recipe to update the meal plan to
    const updatedRecipeTitle = `Updated Recipe ${Date.now()}`;
    await addRecipe(page, updatedRecipeTitle);

    // Add a meal plan
    const mealPlanDetails = await addMealPlan(page, {mealType: 'dinner', recipe: firstRecipeTitle});

    await page.getByRole('link', {name: 'Edit Meal'}).click(); // Click the Edit link to go to the edit page for the meal plan    
    await expect(page.locator('select[name="recipe_id"]')).toBeVisible(); // Wait for the recipe select field to be visible on the edit page
    await page.selectOption('select[name="recipe_id"]', {label: updatedRecipeTitle}); // Select the updated recipe in the select field
    await page.locator('button[type="submit"]').click();

    // Check that the meal plan page shows the updated recipe details
    await expect(page.getByText(/meal plan updated successfully/i)).toBeVisible();
    await expect(page.locator('.view-meal-day-card', {hasText: updatedRecipeTitle})).toBeVisible();
});

test('cancel edit keeps form open', async ({page}) => {
    const uniqueID = Date.now().toString().slice(-6);
    const username = `testuser${uniqueID}`;
    const email = `${username}@example.com`;
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    // Create a recipe to use in the meal plan
    const firstRecipeTitle = await createRecipeForMealPlan(page);
    // Create second recipe to update the meal plan to
    const updatedRecipeTitle = `Updated Recipe ${Date.now()}`;
    await addRecipe(page, updatedRecipeTitle);

    // Add a meal plan
    const mealPlanDetails = await addMealPlan(page, {mealType: 'dinner', recipe: firstRecipeTitle});

    await page.getByRole('link', {name: 'Edit Meal'}).click(); // Click the Edit link to go to the edit page for the meal plan    
    await expect(page.locator('select[name="recipe_id"]')).toBeVisible(); // Wait for the recipe select field to be visible on the edit page
    await page.selectOption('select[name="recipe_id"]', {label: updatedRecipeTitle}); // Select the updated recipe in the select field
    await page.getByRole('link', {name: 'Cancel'}).click(); // Click the Cancel link to cancel editing
    await page.once('dialog', async dialog => {
        expect(dialog.message()).toMatch(/are you sure you want to cancel/i);
        await dialog.dismiss();
    });

    await page.getByRole('link', {name: 'Cancel'}).click(); // Click the Cancel link to cancel editing

    // Check that the meal plan page shows the original recipe details and not the updated details
    await expect(page).toHaveURL(/\/meal-plans\/\d+\/edit/); // Check that we are back on the meal plans page

    //form still visible with original details
    await expect(page.locator('select[name="recipe_id"]')).toBeVisible();
});

test('cancel edit returns user to meal plan page', async ({page}) => {
    const uniqueID = Date.now().toString().slice(-6);
    const username = `testuser${uniqueID}`;
    const email = `${username}@example.com`;
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    // Create a recipe to use in the meal plan
    const firstRecipeTitle = await createRecipeForMealPlan(page);

    // Create second recipe to update the meal plan to
    const updatedRecipeTitle = `Updated Recipe ${Date.now()}`;
    await addRecipe(page, updatedRecipeTitle);    

    // Add a meal plan
    const mealPlanDetails = await addMealPlan(page, {mealType: 'dinner', recipe: firstRecipeTitle});

    await page.getByRole('link', {name: 'Edit Meal'}).click(); // Click the Edit link to go to the edit page for the meal plan    
    await expect(page.locator('select[name="recipe_id"]')).toBeVisible(); // Wait for the recipe select field to be visible on the edit page
    await page.selectOption('select[name="recipe_id"]', {label: updatedRecipeTitle}); // Select the updated recipe in the select field
    await page.getByRole('link', {name: 'Cancel'}).click(); // Click the Cancel link to cancel editing
    await page.once('dialog', async dialog => {
        expect(dialog.message()).toMatch(/are you sure you want to cancel/i);
        await dialog.accept();
        });

    await expect(page).toHaveURL(/\/meal-plans\/\d+\/edit/); // Check that we are back on the meal plans page
});

test('delete meal plan removes it from meal plan page', async ({page}) => {
    const uniqueID = Date.now().toString().slice(-6);
    const username = `testuser${uniqueID}`;
    const email = `${username}@example.com`;
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    // Create a recipe to use in the meal plan
    const firstRecipeTitle = await createRecipeForMealPlan(page);

    // Add a meal plan
    const mealPlanDetails = await addMealPlan(page, {mealType: 'dinner', recipe: firstRecipeTitle});

    // Check that the meal plan appears on the meal plan page with correct details
    await expect(page.locator('.view-meal-day-card', {hasText: firstRecipeTitle})).toBeVisible();

    const mealCard = page.locator('.view-meal-day-card', {hasText: firstRecipeTitle});
    // Delete the meal plan
    await page.once('dialog', async dialog => {
        expect(dialog.message()).toMatch(/are you sure you want to delete/i);
        await dialog.accept();
    });

    await mealCard.getByText('Delete Meal').click(); // Click the Delete button for the meal plan
    await page.getByRole('button', {name: /yes,\s*delete/i}).click(); // Confirm deletion in the dialog
    // Check that the meal plan is removed from the meal plan page
    await expect(page.locator('.view-meal-day-card', {hasText: firstRecipeTitle})).not.toBeVisible();
});