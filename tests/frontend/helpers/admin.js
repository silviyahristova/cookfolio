export async function loginAsAdmin(page) {

    const adminUsername=process.env.TEST_ADMIN_USERNAME;
    const adminPassword=process.env.TEST_ADMIN_PASSWORD;

    if (!adminUsername || !adminPassword) {
        throw new Error('Admin credentials are not set in environment variables');
    }
    
    // Go to the login page
    await page.goto('http://localhost:5000/login');
    // Fill in the admin credentials
    await page.fill('input[name="username"]', adminUsername);
    await page.fill('input[name="password"]', adminPassword);
    // Click the login button
    await page.click('button[type="submit"]');
}