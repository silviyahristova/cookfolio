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

test.describe('User Registration', () => {
    test('should register a new user successfully', async ({page}, testInfo) => {
        const unique = `${Date.now()}-${testInfo.project.name}`; // Generate a unique timestamp to ensure unique username and email
        await page.goto('http://127.0.0.1:5000/register'); // navigate to the registration page

        // Fill out the registration form
        await page.fill(`input[name="username"]`, `testuser${unique}`);
        await page.fill(`input[name="email"]`, `testuser${unique}@example.com`);
        await page.fill(`input[name="password"]`, 'password123');
        await page.fill(`input[name="confirm_password"]`, 'password123');

        // Submit the registration form
        await page.click('button[type="submit"]');
        // wait for the page to load after submission
        await page.waitForLoadState('networkidle'); 
        // Expect a success message to be visible
        await expect(page.locator('.flash-message')).toBeVisible(); // Check for flash message visibility
    });

    test('should show error message for duplicate username', async ({page}, testInfo) => {
        const unique = `${Date.now()}-${testInfo.project.name}`; // Generate a unique timestamp to ensure unique username and email
        const username = `duplicate-${unique}`;
        const email = `duplicate-${unique}@example.com`;

        await page.goto('http://127.0.0.1:5000/register'); // navigate to the registration page

        // Fill out the registration form for first user
        await page.fill(`input[name="username"]`, username);
        await page.fill(`input[name="email"]`, email);
        await page.fill(`input[name="password"]`, 'password123');
        await page.fill(`input[name="confirm_password"]`, 'password123');
        await page.click('button[type="submit"]');
        await page.waitForLoadState('networkidle');

        // Fill out the registration form for second user with duplicate username
        await page.goto('http://127.0.0.1:5000/register');

        await page.fill(`input[name="username"]`, username);
        await page.fill(`input[name="email"]`, email);
        await page.fill(`input[name="password"]`, 'password123');
        await page.fill(`input[name="confirm_password"]`, 'password123');

        // Submit the registration form
        await page.click('button[type="submit"]');
        await expect(page).toHaveURL(/register/); // Ensure we are still on the registration page
        // Expect an error message to be visible
        await expect(page.locator('.flash-message')).toBeVisible();
    });
});

//Check for password mismatch error message
test('should show error message for password mismatch', async ({page}, testInfo) => {
    const unique = `${Date.now()}-${testInfo.project.name}`; // Generate a unique timestamp to ensure unique username and email

    await page.goto('http://127.0.0.1:5000/register'); // navigate to the registration page

    // Fill out the registration form with mismatched passwords
    await page.fill(`input[name="username"]`, `mismatch-${unique}`);
    await page.fill(`input[name="email"]`, `mismatch-${unique}@example.com`);
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password456');

    // Submit the registration form
    await page.click('button[type="submit"]');
    await expect(page).toHaveURL(/register/); // Ensure we are still on the registration page
    // Expect a password mismatch error message to be visible
    await expect(page.locator('.flash-message')).toBeVisible();
});

//Check flash messages appears
test('should show flash message after registration attempt', async ({page}, testInfo) => {
    const unique = `${Date.now()}-${testInfo.project.name}`; // Generate a unique timestamp to ensure unique username and email
    const username = `flash-${unique}`;
    const email = `flash-${unique}@example.com`;

    await page.goto('http://127.0.0.1:5000/register');
    // Fill out the registration form with valid data to trigger a message
    await page.fill(`input[name="username"]`, username);
    await page.fill(`input[name="email"]`, email);
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password123');

    // Submit the registration form
    await page.click('button[type="submit"]');
    await page.waitForLoadState('networkidle'); // wait for the page to load after submission

    //second attempt with the same username to trigger a message
    await page.goto('http://127.0.0.1:5000/register');
    await page.fill(`input[name="username"]`, username);
    await page.fill(`input[name="email"]`, email);
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password123');

    // Submit the registration form
    await page.click('button[type="submit"]');
    await page.waitForLoadState('networkidle'); // wait for the page to load after submission

    // Expect a success message to be visible
    await expect(page.locator('.flash-message')).toBeVisible();
});

//check for flash message close button functionality
test('should close flash message when close button is clicked', async ({page}, testInfo) => {
    const unique = `${Date.now()}-${testInfo.project.name}`; // Generate a unique timestamp to ensure unique username and email
    const username = `closeflash-${unique}`;
    const email = `closeflash-${unique}@example.com`;
    await page.goto('http://127.0.0.1:5000/register'); 
    // Fill out the registration form to create a user
    await page.fill(`input[name="username"]`, username);
    await page.fill(`input[name="email"]`, email);
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password123');

    await page.click('button[type="submit"]');
    await page.waitForLoadState('networkidle'); // wait for the page to load after submission

    //Trigger a flash message by attempting to register the same user again
    await page.goto('http://127.0.0.1:5000/register');
    await page.fill(`input[name="username"]`, username);
    await page.fill(`input[name="email"]`, email);
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password123');

    // Submit the registration form
    await page.click('button[type="submit"]');

    const flashMessage = page.locator('.flash-message');
    await expect(flashMessage).toBeVisible(); // Ensure the flash message is visible
    await page.click(`.flash-message .close-btn`); // Click the close button on the flash message
    await expect(flashMessage).not.toBeVisible(); // Ensure the flash message is no longer visible
});

