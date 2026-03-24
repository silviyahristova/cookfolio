// configuration file for Playwright tests
const{defineConfig}=require('@playwright/test');

module.exports=defineConfig({
    testDir: './tests/frontend', // directory where tests are located
    use:{
        headless:true, // run tests without opening a browser window
        baseURL: 'http://127.0.0.1:5000', // base URL for the Flask app
    }, 
    outputDir: 'playwright-test-results/', // directory to store test results
    screenshotDir: 'screenshots/', // directory to store screenshots
    projects:[ //testing on different viewports to ensure responsive design
        { 
            name: `Desktop`,
            use: { 
                viewport: { width: 1280, height: 720 }, // set viewport size for desktop
            },
        },
        {   
            name: `Tablet`,
            use: { 
                viewport: { width: 768, height: 1024 }, // set viewport size for tablet
            },
        },
        { 
            name: `Mobile`,
            use: { 
                viewport: { width: 375, height: 667 }, // set viewport size for mobile
            },
        },
    ],
});