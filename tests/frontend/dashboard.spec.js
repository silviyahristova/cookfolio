import {test, expect} from '@playwright/test';
import {registerUser, loginUser} from './helpers/auth.js';
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

test('dashboard loads after register and login', async ({page}) => {
    await registerUser(page, 'testuser', 'testuser@example.com', 'password123');
    await loginUser(page, 'testuser', 'password123');

    //show empty state on dashboard
    await expect(page).toHaveURL(/dashboard/); // Ensure we are on the dashboard page
    await expect(page.locator('body')).toContainText('You haven\'t added any recipes yet.'); // Ensure the empty state is visible

    //check link exists
    const addLink = page.getByRole('link', {name: '+ Add Your First Recipe'});
    await expect(addLink).toBeVisible();
});

test('dashboard shows categories', async ({page}) => {
    const username = 'testuser2';
    const email = 'testuser2@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //check categories are visible on dashboard
    await page.goto('http://localhost:5000/dashboard');
    await expect(page.locator('body')).toContainText('Breakfast');

    //check recipe count to each category is visible
    await expect(page.locator('.category-card-content', {hasText: 'Breakfast'})).toContainText('recipes');

    const recipeCount= await page.locator('.category-card-content', {hasText: 'Breakfast'}).locator('p').textContent();
    expect(recipeCount).toMatch(/\d+\s+recipes/); // Ensure the recipe count is a number
});

