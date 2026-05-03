export async function addRecipe(page, title = 'Test Recipe') {
    await page.goto('http://localhost:5000/add-recipe');
    await page.fill('input[name="title"]', title);
    await page.selectOption('select[name="category_id"]',{label: 'Breakfast'});
    await page.fill('textarea[name="ingredients"]', 'Test ingredients');
    await page.fill('textarea[name="instructions"]', 'Test instructions');
    await page.fill('input[name="prep_time"]', '10');
    await page.fill('input[name="servings"]', '4');
    await page.click('button[type="submit"]');
    await page.waitForLoadState('networkidle'); // wait for the recipe to be added
}