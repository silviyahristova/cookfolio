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
- [**Bugs**](#bugs)
- [**Accessibility**](#accessibility)

## Testing Strategy

Testing was performed throughout the development lifecycle of Cookfolio to ensure that features functioned correctly, user requirements were met and the application provided a reliable and user-friendly experience. A combination of manual testing, automated testing, validation, accessibility testing, security testing, and responsive design testing was used to verify frontend and backend functionality. Testing was carried out continuously during development. Each feature was tested after implementation to identify issues early, reduce risks and improve overall application stability. 

The testing approach focused to verify that all features function as intended, ensure users can successfully complete key tasks, validate user input and error handling, confirm that authentication system work correctly, test database interaction and data persistance, verify API integration function correctly, ensure responsiveness, confirm consistent behaviour across browsers, validate accessibility and usability, identify and resolve bugs, verify that deployment behaves consistenlty with the local development.

Several testing methods were used throughout the project. Manual testing was performed feature-by-feature to verify user interactions, navigation, forms, validations, and overall functionality. User stories were tested tp ensure that use requirements and project goals were successfully implemented. Automated testing was implemented using Pytest and Playwright to verify backend functionality, route behaviour, authentication, database interactions and end-to-end user jorney. Validation tools were used to access HTML, CSS, Python and JS code quality and standart complience. Accessibility testing have been done using Lighthoute. The application was tested across mobile, tablet, laptop and desktop screen sizes to ensurea consistent user experience. Security testing focused on authentication, authorization, role-based access control, password management, protected routesa and forms. Deployment testing was conducted on local and deployed environment to ensure application functionality remained consistent after deployment.

Overall, the testing strategy helped ensure that Cookfolio delivers a stable, secure, responsive, and user-friendly experience while maintaining
 code quality and reliability.

## Manual Testing
## Automated Testing
## Browser Compatibility
## Responsiveness
## Performance
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

<img src="">
</details>

* The validation site [W3C Link Checker](https://validator.w3.org/checklink) was used to check the website for broken links.
* Some errors were found and resolved. More details can be found [here](#resolved-bugs).

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

Issue: During Python validation using Flake8 several code quality issued were identify during development included line lenght violations, unused imports, trailing whitespace, formatting inconsistencies. This issues did not prevent the application from running, but affected code readability, maintanability and compliance with PEP* standarts.

Result: Lomg statements were split across multiple lines using parenthness nd proper indentation. Unused improts were removed from routes, models and test files. Whitespaces was removed manually and with formatting tools. Blank lines were adjusted according to PEP8 Standarts. Imports were moved to the top of the files and grouped logically.

<details><summary>Python Validation</summary>

<img src="app/static/images/test/flake8-test-1.png" width=600px> <img src="app/static/images/test/flake8-test-2.png" width=600px>
<img src="app/static/images/test/flake8-test-3.png" width=600px> <img src="app/static/images/test/flake8-test-4.png" width=600px>
</details>

### Unresolved bugs and warnings

#### Warning: SQLAlchemy Deprecation Warnings

Issue: Minor SQLAlchemy deprecation warnings were displayed during automated testing. The warning originate from compatibility between libraries and SQLAlchemy 2.x rather than from application code.

Result: The warnings were reviewed and documented. They do not affect application functionality, testing or user experience.

<details><summary>SQLAlchemy deprecation warnings</summary>

<img src="app/static/images/test/pytest-pass.png">
</details>

## Accessibility

### Color contrast

* The main colors, used for the website, have very good contrast. They were tested with [WebAIM contrast checker](https://webaim.org/resources/contrastchecker/).

<img src="assets/images/testing/contrast1.png" width=250px>, <img src="assets/images/testing/contrast3.png" width=250px>, <img src="assets/images/testing/contrast5.png" width=250px>

### WAVE Web Accessibility Evaluation Tools

<details><summary>Home page</summary>

<img src="assets/images/testing/indexpage-wave.png">

</details>

<details><summary>Contact page</summary>

<img src="assets/images/testing/contactpage-wave.png">

</details>

<details><summary>404 page</summary>

<img src="assets/images/testing/404page-wave.png">

</details>

* On all pages same alert came up - that there is more than 1 redundant link. This is, because some links are navigating users to the same page, but was made to be user friendly and intuitive as possible for the user. No further action was taken.

Back to [**README.md**](README.md#testing)