const {test, expect} = require('@playwright/test');

// Take a screenshot after each test if fail and save it in the screenshots directory
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
test.describe('Base layout', () => {
    test('homepage loads successfully and navbar and footer are visible', async ({page}) => {
        await page.goto('/'); // navigate to the homepage
        await expect(page.locator('nav')).toBeVisible(); // check if navbar is visible
        await expect(page.locator('footer')).toBeVisible(); // check if footer is visible
    });
});