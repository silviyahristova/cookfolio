import {test, expect} from '@playwright/test';

test.describe('User Registration', () => {
    test('should register a new user successfully', async ({page}) => {
        const unique = Date.now(); // Generate a unique timestamp to ensure unique username and email
        await page.goto('http://127.0.0.1:5000/register'); // navigate to the registration page

        // Fill out the registration form
        await page.fill(`input[name="username"]`, `testuser${unique}`);
        await page.fill(`input[name="email"]`, `testuser${unique}@example.com`);
        await page.fill(`input[name="password"]`, 'password123');
        await page.fill(`input[name="confirm_password"]`, 'password123');


        // Submit the registration form
        await page.click('button[type="submit"]');
        // Expect a success message to be visible
        await expect(page.locator('.flash-message')).toBeVisible();
    });

    test('should show error message for duplicate username', async ({page}) => {
        await page.goto('http://127.0.0.1:5000/register'); // navigate to the registration page

        // Fill out the registration form with a duplicate username
        await page.fill(`input[name="username"]`, 'testuser'); // assuming 'testuser' already exists
        await page.fill(`input[name="email"]`, 'testuser2@example.com');
        await page.fill(`input[name="password"]`, 'password123');
        await page.fill(`input[name="confirm_password"]`, 'password123');

        // Submit the registration form
        await page.click('button[type="submit"]');

        // Expect an error message to be visible
        await expect(page.locator('.flash-message')).toBeVisible();
    });
});

//Check for password mismatch error message
test('should show error message for password mismatch', async ({page}) => {
    await page.goto('http://127.0.0.1:5000/register'); // navigate to the registration page
    // Fill out the registration form with mismatched passwords
    await page.fill(`input[name="username"]`, 'testuser2');
    await page.fill(`input[name="email"]`, 'testuser2@example.com');
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password456');

    // Submit the registration form
    await page.click('button[type="submit"]');

    // Expect a password mismatch error message to be visible
    await expect(page.locator('.flash-message')).toBeVisible();
});

//Check flash messages appears
test('should show flash message after registration attempt', async ({page}) => {
    await page.goto('http://127.0.0.1:5000/register');
    // Fill out the registration form with valid data to trigger a success message
    await page.fill(`input[name="username"]`, 'testuser4');
    await page.fill(`input[name="email"]`, 'testuser4@example.com');
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password123');

    // Submit the registration form
    await page.click('button[type="submit"]');

    // Expect a success message to be visible
    await expect(page.locator('.flash-message')).toBeVisible();
});

//check for flash message close button functionality
test('should close flash message when close button is clicked', async ({page}) => {
    await page.goto('http://127.0.0.1:5000/register'); // navigate to the registration page
    // Fill out the registration form with valid data to trigger a success message
    await page.fill(`input[name="username"]`, 'testuser4');
    await page.fill(`input[name="email"]`, 'testuser4@example.com');
    await page.fill(`input[name="password"]`, 'password123');
    await page.fill(`input[name="confirm_password"]`, 'password123');

    // Submit the registration form
    await page.click('button[type="submit"]');

    // Expect a success message to be visible
    await expect(page.locator('.flash-message')).toBeVisible();

    // Click the close button on the flash message
    await page.click('.flash-message .close-btn');

    // Expect the flash message to be hidden
    await expect(page.locator('.flash-message')).not.toBeVisible();
});

