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

test('404 page displays correctly', async ({page}) => {
    await page.goto('/nonexistentpage');
    await expect(page.locator('h1')).toHaveText('404 - Page Not Found');
    await expect(page.locator('.error-text')).toContainText('Sorry, but the page you are looking for does not exist or may have been removed.');
});

test('404 page has link to home page', async ({page}) => {
    await page.goto('/nonexistentpage');
    const homeLink = page.locator('a', {hasText: 'Return to Home'});
    await expect(homeLink).toBeVisible();
});

test('clicking home link on 404 page redirects to home page', async ({page}) => {
    await page.goto('/nonexistentpage');
    const homeLink = page.locator('a', {hasText: 'Return to Home'});
    await homeLink.click();
    await expect(page).toHaveURL('/');
});

test('404 page shows correct content for logged in user', async ({page}) => {
    const username = 'testuser5';
    const email = 'testuser5@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    await page.goto('/nonexistentpage');
    await expect(page.locator('h1')).toHaveText('404 - Page Not Found');
    await expect(page.locator('.error-text')).toContainText('Sorry, but the page you are looking for does not exist or may have been removed.');
});