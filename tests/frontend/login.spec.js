import {test, expect} from '@playwright/test';

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

test.describe('User Login', () => {
    test('should log in successfully with valid credentials', async ({page}) => {
        await page.goto('http://127.0.0.1:5000/login');
        await expect(page).toHaveURL(/login/); // Ensure we are on the login page
        await expect(page.locator(`form`)).toBeVisible(); // Ensure the login form is visible
    });
});

test(`login form fields are visible`, async ({page}) => {
    await page.goto('http://127.0.0.1:5000/login');
    await expect(page.locator(`input[name="username"]`)).toBeVisible(); // Ensure the username field is visible
    await expect(page.locator(`input[name="password"]`)).toBeVisible(); // Ensure the password field is visible
    await expect(page.locator(`button[type="submit"]`)).toBeVisible(); // Ensure the submit button is visible
});

test(`user can fill the form and submit`, async ({page}) => {
    await page.goto('http://127.0.0.1:5000/logout'); // Ensure we are logged out before testing login
    await page.goto('http://127.0.0.1:5000/login');
    await page.fill(`input[name="username"]`, 'testuser');
    await page.fill(`input[name="password"]`, 'password123');
    await page.click(`button[type="submit"]`);
    await page.waitForLoadState('networkidle'); // wait for the page to load after submission
    await expect(page).toHaveURL(/dashboard/); // Ensure we are on the dashboard page
});

test(`invalid login stays on login page and shows error message`, async ({page}) => {
    await page.goto('http://127.0.0.1:5000/login');
    await page.fill(`input[name="username"]`, 'testuser');
    await page.fill(`input[name="password"]`, 'wrongpassword');
    await page.click(`button[type="submit"]`);
    await page.waitForLoadState('networkidle'); // wait for the page to load after submission
    await expect(page).toHaveURL(/login/); // Ensure we are still on the login page
    await expect(page.locator('.flash-message')).toBeVisible(); // Check for flash message visibility
});

test(`flash message can be dismissed`, async ({page}) => {
    await page.goto('http://127.0.0.1:5000/login');
    await page.fill(`input[name="username"]`, 'testuser');
    await page.fill(`input[name="password"]`, 'wrongpassword');
    await page.click(`button[type="submit"]`);
    await page.waitForLoadState('networkidle'); // wait for the page to load after submission
    await expect(page).toHaveURL(/login/); // Ensure we are still on the login page
    await expect(page.locator('.flash-message')).toBeVisible(); // Check for flash message visibility
    await page.click('.flash-message .close-btn'); // Click the close button to dismiss the flash message
    await expect(page.locator('.flash-message')).not.toBeVisible(); // Ensure the flash message is no longer visible
});
