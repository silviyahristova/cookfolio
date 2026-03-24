const {test, expect} = require('@playwright/test');

test.describe('Base layout', () => {
    test('homepage loads successfully and navbar and footer are visible', async ({page}) => {
        await page.goto('/'); // navigate to the homepage
        await expect(page.locator('nav')).toBeVisible(); // check if navbar is visible
        await expect(page.locator('footer')).toBeVisible(); // check if footer is visible
    });
});