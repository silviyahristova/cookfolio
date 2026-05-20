import { test, expect } from '@playwright/test';
import { loginAsAdmin } from './helpers/admin';

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

test('support page loads and can submit support message', async ({ page }) => {
  // Go to the support page
  await page.goto('http://localhost:5000/support');

  // Submit the support form
  await page.fill('input[name="name"]', 'Test User');
  await page.fill('input[name="email"]', 'testuser@example.com');
  await page.fill('input[name="subject"]', 'Test Support Message');
  await page.fill('textarea[name="message"]', 'This is a test support message.');
  await page.click('button[type="submit"]');

  // Expect a success message
  await expect(page).toHaveURL('http://localhost:5000/support');
  await expect(page.locator('body')).toContainText('Your message has been sent. We will get back to you shortly.');
});

test('support form validation appears', async ({ page }) => {
    // Go to the support page
    await page.goto('http://localhost:5000/support');
    // Submit the support form with missing fields
    await page.fill('input[name="name"]', '');
    await page.fill('input[name="email"]', 'invalid-email');
    await page.fill('input[name="subject"]', '');
    await page.fill('textarea[name="message"]', '');
    await page.click('button[type="submit"]');

    // Expect validation errors
    await expect(page.locator('body')).toContainText('All fields are required');
});

test('support form email validation appears', async ({ page }) => {
    // Go to the support page
    await page.goto('http://localhost:5000/support');
    // Submit the support form with an invalid email
    await page.fill('input[name="name"]', 'Test User');
    await page.fill('input[name="email"]', 'invalid-email');
    await page.fill('input[name="subject"]', 'Test Support Message');
    await page.fill('textarea[name="message"]', 'This is a test support message.');
    await page.click('button[type="submit"]');

    // Expect email validation error
    await expect(page.locator('body')).toContainText('Please enter a valid email address');
});

test('admin can view support messages', async ({ page }) => {

    // Use a unique identifier in the subject and message to ensure we can find the specific test message in the admin view
    const uniqueID = Date.now(); // unique identifier to ensure the message is distinct
    const subjectText = `Test Support Message ${uniqueID}`;
    const messageText = `This is a test support message. ${uniqueID}`; 

    // Submit a test support message to ensure there is at least one message to view
    await page.goto('http://localhost:5000/support');
    await page.fill('input[name="name"]', 'Test User');
    await page.fill('input[name="email"]', 'testuser@example.com');
    await page.fill('input[name="subject"]', subjectText);
    await page.fill('textarea[name="message"]', messageText);
    await page.click('button[type="submit"]');

    // Log in as admin user
    await loginAsAdmin(page);

    // Go to the admin support messages page
    await page.goto('http://localhost:5000/admin/support-messages');

    // Expect to see the test support message
    await expect(page.locator('body')).toContainText(messageText);
});