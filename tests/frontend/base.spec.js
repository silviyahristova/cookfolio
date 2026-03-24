const {test, expect} = require('@playwright/test');

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
test.describe('Base layout', () => {
    //page loading test
    test('homepage loads successfully and navbar and footer are visible', async ({page}) => {
        await page.goto('/'); // navigate to the homepage
        await expect(page.locator('nav')).toBeVisible(); // check if navbar is visible
        await expect(page.locator('footer')).toBeVisible(); // check if footer is visible
    });

    //logo test
    test(`logo test`, async ({page}) => {
        await page.goto('/'); // navigate to the homepage
        const logo = page.locator('.nav-logo-link'); // locate the logo in the navbar
        await expect(logo).toBeVisible(); // check if the logo is visible
        await expect(logo).toHaveAttribute('href', '/'); // check if the logo links to the homepage
        await logo.click(); // click the logo
        await expect(page).toHaveURL(/\/$/); // check if the URL is still the homepage after clicking the logo
    });

    //test hamburger menu 
    test(` mobile menu test`, async ({page}) => {
        await page.setViewportSize({ width: 375, height: 667 }); // set viewport size to mobile 
        await page.goto('/'); // navigate to the homepage
        const menu = page.locator('#menu-toggle'); // locate the mobile menu button
        await expect(menu).toBeVisible(); // check if the mobile menu button is visible
        await menu.click(); // click the mobile menu button
        await expect(page.locator('.navbar-links')).toBeVisible(); // check if the mobile menu links are visible after clicking the menu button
    });

    //test social media links in the footer
    test(`social media links test`, async ({page}) => {
        await page.goto('/'); // navigate to the homepage
        await expect(page.locator('.social-links')).toBeVisible(); // check if footer is visible
    });
});