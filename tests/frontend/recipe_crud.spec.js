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

test('add recipe and check it appears on recipe page', async ({page}) => {
    const username = 'testuser6';
    const email = 'testuser6@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');
    await page.waitForURL(/recipe/); // Wait for the URL to change to the recipe page after adding a recipe

    //check recipe appears on recipe page
    await expect(page.locator('.view-recipe-content')).toContainText('Test Recipe');
});

test('view recipe page shows correct details', async ({page}) => {
    const username = 'testuser7';
    const email = 'testuser7@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');
    await page.waitForURL(/recipe/); // Wait for the URL to change to the recipe page after adding a recipe

    //check recipe details are correct
    await expect(page.locator('.view-recipe-content')).toContainText('Test Recipe');
    await expect(page.getByText(/prep time/i)).toBeVisible();
    await expect(page.getByText(/10 minutes/i)).toBeVisible();
    await expect(page.getByText(/servings/i)).toBeVisible();
    await expect(page.getByText(/4/)).toBeVisible();
    await expect(page.locator('.view-recipe-block', {hasText: 'Ingredients'})).toBeVisible();
    await expect(page.locator('.view-recipe-block', {hasText: 'Instructions'})).toBeVisible();
    await expect(page.locator('.view-recipe-content')).toContainText('Category: Breakfast');
});

test('edit recipe and check changes appear on recipe page', async ({page}) => {
    const username = 'testuser8';
    const email = 'testuser8@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');
    await page.waitForURL(/recipe/);

    //edit recipe
    await page.getByRole('link', {name: 'Edit Recipe'}).click();
    await page.waitForURL(/edit/); // Wait for the URL to change to the edit recipe page
    await page.fill('input[name="title"]', 'Updated Test Recipe');
    await page.click('button:has-text(" Update Recipe")');

    //go to recipe page
    await page.waitForURL(/recipes/);

    //check updated recipe details are correct
    await expect(page.locator('.view-recipe-content')).toContainText('Updated Test Recipe');
});

test('delete recipe and check it no longer appears on recipe page', async ({page}) => {
    const username = 'testuser9';
    const email = 'testuser9@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Delete Recipe');
    await page.waitForURL(/recipe/); // Wait for the URL to change to the recipe page after adding a recipe

    //delete recipe
   await expect(page.locator('body')).toContainText('Delete Recipe'); // Ensure the "Delete Recipe" button is present before clicking
    await page.getByText('Delete Recipe', {exact: true}).click();
    await page.getByRole('button', {name: /yes,\s*delete/i}).click();
    
    //check recipe is deleted
    await expect(page.locator('body')).not.toContainText('Test Delete Recipe');
});

test('cancel edit returns to recipe page without changes', async ({page}) => {
    const username = 'testuser10';
    const email = 'testuser10@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //edit recipe
    await page.getByRole('link', {name: 'Edit Recipe'}).click();
    await page.fill('input[name="title"]', 'Updated Test Recipe');

    //cancel edit
    page.once('dialog', async dialog => {
        expect(dialog.message()).toMatch(/are you sure you want to cancel/i);
        await dialog.accept();
    });
    await page.getByRole('link', {name: 'Cancel'}).click();

    //check that the recipe name has not been updated
    await expect(page.locator('body')).toContainText('Test Recipe');
    await expect(page.locator('body')).not.toContainText('Updated Test Recipe');
});

test('cancel delete returns to recipe page without deleting', async ({page}) => {
    const username = 'testuser11';
    const email = 'testuser11@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //delete recipe
    await page.getByText('Delete Recipe').click();
    
    await page.locator('.delete-confirmation label[for="confirm-delete"]',{hasText:'Cancel'}).click(); // Click the "Cancel" option in the confirmation dialog

    //check that the recipe is still present
    await expect(page.locator('body')).toContainText('Test Recipe');
});

test('add recipe with missing fields shows error message', async ({page}) => {
    const username = 'testuser12';
    const email = 'testuser12@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    // add recipe with missing fields
    await page.goto('http://localhost:5000/add-recipe');

    const titleInput = page.locator('input[name="title"]');
    await titleInput.fill('');
    await page.click('button[type="submit"]');

    await expect(titleInput).toHaveAttribute('required', '');
});

test('edit recipe with missing fields shows error message', async ({page}) => {
    const username = 'testuser13';
    const email = 'testuser13@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //edit recipe
    await page.getByRole('link', {name: 'Edit Recipe'}).click();
    await page.waitForURL(/edit/); // Wait for the URL to change to the edit recipe page

    const titleInput = page.locator('input[name="title"]');
    await titleInput.fill('');
    await page.click('button:has-text("Update Recipe")');
    await expect(page).toHaveURL(/edit/); // Ensure we are still on the edit page after submitting with missing fields

    //check that error message is displayed
    await expect(titleInput).toHaveAttribute('required', '');
});

test('edit validation errors keeps entered data in form', async ({page}) => {
    const username = 'testuser14';
    const email = 'testuser14@example.com';
    const password = 'password123';

    await registerUser(page, username, email, password);
    await loginUser(page, username, password);

    //add recipe
    await addRecipe(page, 'Test Recipe');

    //edit recipe
    await page.getByRole('link', {name: 'Edit Recipe'}).click();
    await page.waitForURL(/edit/); 
    await page.fill('input[name="title"]', '');
    await page.fill('textarea[name="ingredients"]', 'Updated Ingredients');
    //submit edit
    await page.click('button:has-text("Update Recipe")');

    //check that the form still contains the entered data
    await expect(page).toHaveURL(/edit/); // Ensure we are still on the edit page after submitting with missing fields
    await expect(page.locator('textarea[name="ingredients"]')).toHaveValue('Updated Ingredients');
});