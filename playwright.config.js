// configuration file for Playwright tests
const{defineConfig}=require('@playwright/test');

module.exports=defineConfig({
    testDir: './tests/frontend', // directory where tests are located
    use:{
        headless:true, // run tests without opening a browser window
        baseURL: 'http://127.0.0.1:5000', // base URL for the Flask app
    }, 
    outputDir: 'playwright-test-results/', // directory to store test results
});