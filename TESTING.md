# Cookfolio Testing

![Responsive Mock-up](app/static/images/docs/cookfolio-mock-up.webp)

#### **By Silviya Hristova**

[Click here to view the live web application](https://cookfolio-dc589e41eddc.herokuapp.com/)

Cookfolio is a recipe management website that allows users to create, edit and organize their own recipes, plan weekly meals and discover new recipes. The application is designed to help users manage their cooking and meal planning in a simple and intuitive way.

This is the documentation for Cookfolio, a full-stack web application. It has been built using HTML5, CSS3, JavaScript, Python, Flask and a relational database. It has been developed for educational purposes as part of Code Institute Level 5 Diploma in Web Application Development.

---

## Table of content

- [**Testing Strategy**](#testing-strategy)
- [**Manual Testing**](#manual-testing)
- [**Automated Testing**](#automated-testing)
- [**Browser Compatibility**](#browser-compatibility)
- [**Responsiveness**](#responsiveness)
- [**Performance**](#performance)
- [**Code Validation**](#code-validation)
- [**Accessibility**](#accessibility)
- [**Bugs**](#bugs)

## Testing Strategy

Testing was performed throughout the development lifecycle of Cookfolio to ensure that features functioned correctly, user requirements were met and the application provided a reliable and user-friendly experience. A combination of manual testing, automated testing, validation, accessibility testing, security testing, and responsive design testing was used to verify frontend and backend functionality. Testing was carried out continuously during development. Each feature was tested after implementation to identify issues early, reduce risks and improve overall application stability. 

The testing approach focused to verify that all features function as intended, ensure users can successfully complete key tasks, validate user input and error handling, confirm that authentication system work correctly, test database interaction and data persistance, verify API integration function correctly, ensure responsiveness, confirm consistent behaviour across browsers, validate accessibility and usability, identify and resolve bugs, verify that deployment behaves consistenlty with the local development.

Several testing methods were used throughout the project. Manual testing was performed feature-by-feature to verify user interactions, navigation, forms, validations, and overall functionality. User stories were tested tp ensure that use requirements and project goals were successfully implemented. Automated testing was implemented using Pytest and Playwright to verify backend functionality, route behaviour, authentication, database interactions and end-to-end user jorney. Validation tools were used to access HTML, CSS, Python and JS code quality and standart complience. Accessibility testing have been done using Lighthoute. The application was tested across mobile, tablet, laptop and desktop screen sizes to ensurea consistent user experience. Security testing focused on authentication, authorization, role-based access control, password management, protected routesa and forms. Deployment testing was conducted on local and deployed environment to ensure application functionality remained consistent after deployment.

Overall, the testing strategy helped ensure that Cookfolio delivers a stable, secure, responsive, and user-friendly experience while maintaining code quality and reliability.

[Back to top](#table-of-content)

## Manual Testing

[Back to top](#table-of-content)

## Automated Testing

Automated testing was implemented throughout the development of Cookfolio to verify application functionality, reduce regression issues and ensure that features are working when new functionality is added. The project used both Pytest and Playwright for automated testing.

### Pytest Testing

* Pytest was used to test backend functionality, routes, models, and authentication. Areas covered include user registration, user login and logout, protected routes, recipe creation, editing,deleting, meal planner functionality, error handling and database interactions. Pytest helped ensure that backend functionality behave as expected and that future code changes did not introduce regressions. To improve tes reliability and reduce code duplication, Pytest fixtures were created and used for the automated testing. Fixtures were used to provide reusable test data including test client setup, test user, admin user, test recipe, test meal plan, standard user. Fixtures ensured that each test can run independently using predictable data.

* Final test results

<img src="app/static/images/test/final-pytest-pass.png">

<details><summary>Pytest Results during development</summary>

<img src="app/static/images/test/pytest-relationships-during-testing.png"> <img src="app/static/images/test/pytest-routes-during-coding.png"> <img src="app/static/images/test/pytest-testing-during-coding.png">
</details>

### Playwright Testing

* Playwright testing was used to perfom automated end-to-end testing of Cookfolio from user`s perspective. These tests simulate real user interactions within a browser and help verify that features function correctly. Playwright was implemented during development nad was regularly executed after feature additions and bug fixes. Playwright was used to verify responsive behaviour across multiple devices. Testing included mobile, table and desktop layouts. Playwright automatically generated screenshots during test execution. Screenshots were used to verify rendering, compare layout across devices, assist with debugging during development. Screenshot were collected for both successful and failed test runs. Playwright testing successfully verified key user journeys throughout the application and helped ensure that Cookfolio functions consistently across the devices and browsers.

* Final test results

<img src="app/static/images/test/final-playwright-pass.png">

<details><summary>Playwright Results during development</summary>

<img src="app/static/images/test/playwright-meal-crud-test.png"> <img src="app/static/images/test/playwright-testing-during-coding.png">
</details>

[Back to top](#table-of-content)

## Browser Compatibility

| **Browser tested** | **Intended appearance** | **Intended responsiveness** | 
|--------------------|-------------------------|-----------------------------|
| Google Chrome      |Excellent|Excellent|
| Mozzila            |Excellent|Excellent|
| Firefox            |Excellent|Excellent|
| Microsoft edge     |Excellent|Excellent|
| Safari            |Very Good|Very Good|

* Browser compatibility testing was performed to ensure that Cookfolio provides a consistent user experience across modern web browsers. Testing was conducted throughout development and during final testing using manual testing. The application was tested in Google Chrome, Mozzila, Firefox, Microsoft edge and Safari. All tests passed. All features tested and verified in eah browser. Cookfolio functions correctly across all tested browsers and provides a consistent user experience.

[Back to top](#table-of-content)

## Responsiveness

| **Device Tested** | **Site responsive** | **Renders as expected** |
|-------------------|---------------------|-------------------------|
| Samsung Galaxy S21 Ultra|Excellent|Yes|
| Iphone 5s/6s      |Excellent|Yes|
| Ipad              |Excellent|Yes|
| Samsung Galaxy Tab 3|Excellent|Yes|
| Desktop           |Excellent|Yes|
| Laptop            |Excellent|Yes|
| Google Dev Tools  |Excellent|Yes|

* Responsive design testing was performed during development of Cookfolio to ensure that the application remains functional, accessible and visually consistent across a wide range of devices and screen sizes. Testing was conducted using browser developer tools, real devices, Playwright devices emulation. The website was tested across multiple viewport sizes. All features were tested and passed. Cookfolio includes several responsive design improvements as responsive recipe cards, navigation menu, meal planner, touch-friendly buttons and links, and etc. Responsive testing confirmed that Cookfolio provides a consistent and user-friendly experience across mobile, tablet, desktop and laptop screens. No critical responsive design issues remain.

[Back to top](#table-of-content)

## Performance

Lighthouse performance testing was completed on both mobile and desktop views. Desktop performance scores were consistently strong, usually ranging between 90 and 100. Mobile performance scores varied more, usually ranging between 80 and 95, depending on the page content, image loading, network, and whether page include dynamic content suach as recipe images, API data, and dashboard components. The main factor affecting mobile performance were large recipe and hero images, external APIs recipe images, dynamic page content, Large contentful paint timings. The project uses WebP images, png fallback images, responsive layouts, pagination for recipe collection. While some mobile scores are lower than desktop scores. the results remaining within an acceptable range, and no critical performance issues were identified. There will be improvements in the future for better performance.

<details><summary>Lighthouse test results</summary>

* Desktop view

<img src="app/static/images/test/lighthouse-home.png"> <img src="app/static/images/test/lighthouse-discover-desktop.png"> <img src="app/static/images/test/lighthouse-desktop-meal.png">

* Mobile view

<img src="app/static/images/test/lighthouse-mobile-home.png"> <img src="app/static/images/test/lighthouse-mobile-recipe.png"> <img src="app/static/images/test/lighthouse-mobile-form.png">
<img src="app/static/images/test/lighthouse-mobile-recipes.png"> <img src="app/static/images/test/lighthouse-mobile-support.png"> <img src="app/static/images/test/lighthouse-mobile-grocery.png">
</details>

[Back to top](#table-of-content)

## Code Validation

Code validation was perfomed throughout the development process to ensure that Cookfolio follows modern web development standarts, maintain code quality, and provides a reliable user ecperience. Validation testing was carried out on HTML, CSS, Python and JS.

### HTML Validation

<details><summary>HTML Validation</summary>

<img src="app/static/images/test/html-validation.png">
</details>

* The validation site [W3C HTML Validator](https://validator.w3.org/nu/) was used to validate the HTML. 
* No errors were found.

### CSS Validation

<details><summary>CSS Validation</summary>

<img src="app/static/images/test/css-validation.png">
</details>

* The validation site [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate the CSS.
* No errors were found.

### JavaScript Validation

<details><summary>JS Validation</summary>

<img src="app/static/images/test/js-validation.png">
</details>

* The validation site [JSHint](https://jshint.com/) was used to validate the JavaScript files.
* No errors were found.

### Python Validation

<details><summary>Python Validation</summary>

<img src="app/static/images/test/flake8-final.png">
</details>

* Python code was validated using [Flake8](https://flake8.pycqa.org/en/latest/) and PEP8 guidlines. Validation covered are routes, models, forms, automated testing and configuration files.
* Cookfolio complies with PEP8 coding standarts and passed Flake8 validation checks. 
* Some errors were found and resolved. More details can be found [here](#resolved-bugs).

### Link Checker

<details><summary>Link Validation</summary>

<img src="app/static/images/test/link-checker-pass.png">
</details>

* The validation site [W3C Link Checker](https://validator.w3.org/checklink) was used to check the website for broken links.
* No broken internal links were identified. The validator reported Facebook, LinkdIn and Twitter external links. All external social media links verified manually.
* One error was found and resolved. More details can be found [here](#resolved-bugs).

[Back to top](#table-of-content)

## Accessibility

### Color contrast

* Cookfolio uses a carefully selected colour palette to maintain readability and visual accessibility. Testing were performed to ensure that text remains readable against background colours, buttons prove sufficient contrast, navigation elements remain visible.The project colour scheme was adjusted during development to improve compliance with accesibility recommendations. Colours were tested with [WebAIM contrast checker](https://webaim.org/resources/contrastchecker/).

<img src="app/static/images/test/contast1.png" width=300px> <img src="app/static/images/test/contrast2.png" width=300px> <img src="app/static/images/test/contrast3.png" width=300px>

### WAVE Web Accessibility Evaluation Tools

* The WAVE Web Accessibility Tool was used to review Cookfolio pages for accessibility issues and potential improvements. 
* Some warnings, alerts and one error appears. More details can be found [here](#resolved-bugs).

<img src="app/static/images/test/wave-home.png"> <img src="app/static/images/test/wave-meal-plan.png"> <img src="app/static/images/test/wave-support.png">

[Back to top](#table-of-content)

## Bugs

### Resolved Bugs

#### Bug: Missing Safari Pinned Tab Favicon File

* Issue: During W3C Link Checker validation, a broken link was detected for the Safari pinned tab favicon file. The validator returned 404 error page because the file referenced in the favicon configuration did not exist in the project directory. The favicon package originally included a reference to safari-pinned-tab.svg, but the file was not generated. 

* Fix: The favicon configuraion was reviewed and the invalid reference was removed. The broken link was eliminated, reducing validation warnings. The issue did not affect core application functionallity.

<details><summary>Link Validation</summary>

<img src="app/static/images/test/link-check-bugs.png">
</details>

#### Bug: Python Validation errors

* Issue: During Python validation using Flake8 several code quality issued were identify during development included line lenght violations, unused imports, trailing whitespace, formatting inconsistencies. This issues did not prevent the application from running, but affected code readability, maintanability and compliance with PEP* standarts.

* Fix: Long statements were split across multiple lines using parenthness nd proper indentation. Unused improts were removed from routes, models and test files. Whitespaces was removed manually and with formatting tools. Blank lines were adjusted according to PEP8 Standarts. Imports were moved to the top of the files and grouped logically.

<details><summary>Python Validation</summary>

<img src="app/static/images/test/flake8-test-1.png" width=600px> <img src="app/static/images/test/flake8-test-2.png" width=600px>
<img src="app/static/images/test/flake8-test-3.png" width=600px> <img src="app/static/images/test/flake8-test-4.png" width=600px>
</details>

#### Bug: WAVE error - Multiple form labels

* Issue: WAVE reported a Multiple form labels error on the delete confirmation checkbox used for meal and recipe deletion. The hidden box used for the delete confirmation had two labels connected to the same ID. One label opened the delete confirmation,another label was used as a Cancel button.

* Fix: The first label was kept to open the confirmation, and the second wa replaces with a normal button. The duplicate label association was removed and the WAVE error was resolved.

<details><summary>WAVE error - Multiple form labels</summary>

<img src="app/static/images/test/wave-error.png" width=600px> <img src="app/static/images/test/multi-form-label.png" width=600px>
<img src="app/static/images/test/labet-button.png" width=600px>
</details>

### Unresolved bugs and warnings

#### Warning: SQLAlchemy Deprecation Warnings

* Issue: Minor SQLAlchemy deprecation warnings were displayed during automated testing. The warning originate from compatibility between libraries and SQLAlchemy 2.x rather than from application code.

* Decision: The warnings were reviewed and documented. They do not affect application functionality, testing or user experience.

<details><summary>SQLAlchemy deprecation warnings</summary>

<img src="app/static/images/test/pytest-pass.png">
</details>

#### WAVE Suspicios Alternative text

* Issue: WAVE reported warning suspicious alternative text on some recipe images, particularly recipe imported from external APIs. The approach allows screen reader users to identify the recipe associated with image and provides meaningful context. Alt value is too repetitive. 

* Decision: The warning reviewed and considered acceptable because the alt text remains descreptive enought for users of assistive technologies. No functional or accessibility barriers were identified. The warning was therefore documented but not changed

#### WAVE Redundant links

* Issue: WAVE reported redundant links alert where multiple nearby elements linked to the same destination. This behaviour occurs intentionally within recipe cards, where users can access same page through images and text links.

* Decision: The links were retained because they improve usability and provide larger click for users on mibile devices. No functionality barries were identified. The alert was documented but not chanhed.

Back to [**README.md**](README.md#testing)