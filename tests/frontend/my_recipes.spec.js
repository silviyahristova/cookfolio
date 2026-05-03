import { test, expect } from '@playwright/test';
import { registerUser, loginUser } from './helpers/auth.js';
import { addRecipe } from './helpers/recipe.js';

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

test('click on category shows recipes in that category', async ({page}) => {
    const username = 'testuser3';
    const email = 'testuser3@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //check categories are visible on dashboard
    await page.goto('http://localhost:5000/dashboard');
    await expect(page.locator('body')).toContainText('Breakfast');

    //click on category
    await page.locator('a.category-card-link', {hasText: 'Breakfast'}).click();
    await page.waitForLoadState('networkidle');

    //should navigate to the category page
    await expect(page).toHaveURL(/my-recipes/);
    await expect(page.url()).toContain('category_id=');

    //show the recipes in that category
    await expect(page.locator('.all-recipes-grid')).toContainText('Test Recipe'); // Ensure the recipe is visible on the category page
});

test('click all recipes link shows all recipes', async ({page}) => {
    const username = 'testuser4';
    const email = 'testuser4@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //go to dashboard
    await page.goto('http://localhost:5000/dashboard');

    //click on all recipes link
    await page.locator('.dashboard-section-header').getByRole('link', {name: 'View All Recipes'}).click();

    //should navigate to the all recipes page
    await expect(page).toHaveURL(/my-recipes/);

    //show all recipes
    await expect(page.locator('.all-recipes-grid')).toContainText('Test Recipe'); // Ensure the recipe is visible on the all recipes page
});

test('click category with no recipes shows empty state', async ({page}) => {
    const username = 'testuser5';
    const email = 'testuser5@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //go to dashboard
    await page.goto('http://localhost:5000/dashboard');

    //click on category with no recipes
    await page.locator('.category-card-content').getByRole('link', {name: 'View Lunch Recipes'}).click();

    //should navigate to the category page
    await expect(page).toHaveURL(/my-recipes/);
    await expect(page.url()).toContain('category_id=');

    //show empty state
    await expect(page.locator('body')).toContainText('No recipes yet.');
});