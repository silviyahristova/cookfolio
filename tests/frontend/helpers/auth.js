export async function registerUser(page, username, email, password) {
    await page.goto('http://localhost:5000/register');
    await page.fill('input[name="username"]', username);
    await page.fill('input[name="email"]', email);
    await page.fill('input[name="password"]', password);
    await page.fill('input[name="confirm_password"]', password);
    await page.click('button[type="submit"]');
    await page.waitForLoadState('networkidle'); // wait for the registration to complete
}

export async function loginUser(page, username, password) {
    await page.goto('http://localhost:5000/login');
    await page.fill('input[name="username"]', username);
    await page.fill('input[name="password"]', password);
    await page.click('button[type="submit"]');
    await page.waitForLoadState('networkidle'); // wait for the page to load after login
}