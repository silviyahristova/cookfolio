import {expect} from '@playwright/test';
import {addRecipe} from './recipe.js';

export async function createRecipeForMealPlan(page, title = null ) {

    // If title is not provided, generate a unique title using the current timestamp
    if (!title) {
        title = `Test Recipe ${Date.now()}`;
    }
    
    // Add a recipe to ensure there is at least one recipe available for the meal plan test
    await addRecipe(page, title);

    await expect(page.getByText('Recipe added successfully!')).toBeVisible(); // Wait for the success message to ensure the recipe is added before adding a meal plan
    return title; // Return the title of the created recipe so it can be used in the meal plan test
}

export async function addMealPlan(page, 
    {mealType = "breakfast",
    recipe,
    date = null} = {}) {

    // unique future date for testing
    if (!date) {
        const futureDate = new Date();
        futureDate.setDate(futureDate.getDate() + 14); // Set to 14 days in the future to avoid conflicts with existing meal plans
        date = futureDate.toISOString().split('T')[0]; // Format as YYYY-MM-DD
    }

    //Unique recipe title for testing
    if (!recipe) {
        recipe = `Test Recipe ${Date.now()}`;
    }

    await page.goto(`http://localhost:5000/meal-plans/add?meal_date=${date}&meal_type=${mealType}`);
    await expect(page.locator('select[name="recipe_id"]')).toBeVisible();
    await page.selectOption('select[name="recipe_id"]', {label: recipe});
    await page.click('button[type="submit"]');
    await expect(page.getByText('Meal plan added successfully!')).toBeVisible(); // wait for the meal plan to be added
    
    return {date, mealType, recipe}; // Return the details of the created meal plan for verification in tests
}