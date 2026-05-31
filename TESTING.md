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

### User Stories

<details><summary> As a visitor, I want to view the homepage, so that I can understand what is the main goal of the website.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Homepage| Open the homepage URL.| Homepage loads successfully and clearly explains Cookfolio.|

<img src="">

</details>

<details><summary> As a visitor, I want to be able to create an account, so that I can save and manage my own recipes.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Registration| Complete the registration form with details.| Account is created successfully.|

<img src="">

</details>

<details><summary> As a visitor, I want to be able to log in so I can access my personal dashboard.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Login| Enter valid login details.| User is logged in and redirected to dashboard.|

<img src="">

</details>

<details><summary> As a visitor, I want to be able to contact the support to report issues or ask questions about the website.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Support Form| Submit a valid support message.| Message sends successfully and confirmation is shown.|

<img src="">

</details>

<details><summary> As an user, I want to log in , so that I can access my personal dashboard.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Login| Enter valid login details.| User is logged in and redirected to dashboard.|

<img src="">

</details>

<details><summary> As an user, I want to see a dashboard after logging in, so I can quickly access my recipes.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Dashboard| Log in and open dashboard.| Dashboard displays quick links and user content.|

<img src="">

</details>

<details><summary> As an user, I want to see my recipes on the dashboard.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Dashboard-My recipes| Click **View All Recipes**.| User is redirected to My Recipes page and can see all recipe cards.|

<img src="">

</details>

<details><summary> As an user, I want to add a new recipe.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Add Recipe| Complete add recipe form.| Recipe is saved successfully.|

<img src="">
</details>

<details><summary> As an user, I want to upload image for my recipe.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Image Upload| Add or edit recipe with image upload.| Image displays on recipe card and recipe detail page.|

<img src="">
</details>

<details><summary> As an user, I want to view detailed recipe page, so that I can read the full instructions and ingredients.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Recipe page| Open recipe detail page bh clicking **View recipe** link.| Full recipe information displayed.|

<img src="">

</details>

<details><summary> As an user, I want to edit my recipes, so that I can update them later.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Edit Recipe| Edit an existing recipe and save.| Recipe updates successfully.|

<img src="">

</details>

<details><summary> As an user, I want to delete recipes, so that I can remove recipes I no longer need.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Delete Recipe| Delete a recipe and confirm.| Recipe is deleted successfully.|

<img src="">

</details>

<details><summary> As an user, I want to see all my recipes in one place.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|My Recipes| Open My Recipes page| All users recipes are displayed.|

<img src="">

</details>

<details><summary> As an user, I want to search recipes by keyword, so that I can quickly find a recipe.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Recipe Search| Search using recipe keyword.| Matching recipes are shown.|

<img src="">

</details>

<details><summary> As an user, I want to be able to discover recipes.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Discover Recipes| Open Discover page.| External recipe ideas are displayed.By default - chicken recipes.|

<img src="">

</details>

<details><summary> As an user, I want to filter recipes by category.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Category Filter| Select a recipe category.| Recipes are filtered by selected category.|

<img src="">

</details>

<details><summary> As an user, I want to add recipes to a meal planner.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Add Meal Plan| Fill the form and save.| Recipe is added to selected date and meal category.|

<img src="">

</details>

<details><summary> As an user, I want to assign recipes to specific days, so I can plan meals ahead.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Meal Planner| Add recipe to meal planner.| Recipe is added to selected date and meal category.|

<img src="">

</details>

<details><summary> As an user, I want to edit my meal plan.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Edit Meal Plan| Edit an existing meal plan and save.| Meal plan updates successfully.|

<img src="">

</details>

<details><summary> As an user, I want to remove recipes from my meal planner.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Delete Meal Plan| Remove recipe from meal planner.| Meal plan entry is deleted.|

<img src="">

</details>

<details><summary> As an user, I want to access the site on the mobile device.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Responsive Design| Test site on mobile device.| Layout adapts correctly.|

<img src="">

</details>

<details><summary> As an user, I want to log out of my account anytime.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Log out| Click Log out.| User is logged out successfully.|

<img src="">

</details>

<details><summary> As an user, I want to contact support if there is an issue or to ask a questions about the website.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Support Form| Submit issue/quiestion form.| Message is sent and confirmation email is sent.|

<img src="">

</details>

<details><summary> As an user, I want confirmation that my message was sent.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Flash Messages| Submit support form.| Success message appears.|

<img src="">

</details>

<details><summary> As an admin, I want to access an admin dashboard.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Admin Dashboard| Log in as admin and open admin page.| Admin dashboard opens successfully.|

<img src="">

</details>

<details><summary> As an admin, I want to view all support messages, that users sending.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
Admin Support Messages| Open admin support inbox.| Support messages are displayed.|

<img src="">

</details>

<details><summary> As an admin, I want users to register and log in.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Authentication| Fill Register/Login form.| Users can create accounts and log in securely.|

<img src="">

</details>

<details><summary> As an admin, I want each recipe to be linked to a specific user so that ownership is enforced.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Recipe Ownership| Check recipe is connected to logged in user.| Recipe belongs only tp the creator.|

<img src="">

</details>

<details><summary> As an admin, I want to prevent users from editing or deleting recipes they do not own.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Access Control| Try accessing another user`s edit/delete route.| Access is blocked.|

<img src="">

</details>

<details><summary> As an admin, I want the site to be mobile-first.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Mobile-First Design| Test pages on mobile devices.| PAges remain usable on small screens.|

<img src="">

</details>

<details><summary> As an admin, I want a clean and consistent interface so that users can easily navigate the site.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|UI Consistency| Check navigation, buttons, cards, and page layout.| Interface is consistent across all pages.|

<img src="">

</details>

<details><summary> As an admin, I want to provide a support contact form so that users can report an issue.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Support Form| Submit support form.| User message is sent successfullyand message is stored.|

<img src="">

</details>

<details><summary> As an admin, I want the application to be scalable so that new features can be added in the future.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Scalability| Check strcture, models, routes and templates.| Code is organized and allows future improvements.|

<img src="">

</details>

<details><summary> As an admin, I want to restrict admin pages, so that only authorized users can access them.</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Admin Access Control| Try opening admin page as normal user.| Access is denied and admin page remain protected.|

<img src="">

</details>

### Website Testing

<details><summary>Homepage</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Logo|Click logo|User is redirected to the home page.|
|Login Button| Click Login button.| Login page opens.|
|Sign up| Click Sign up button| Registration page opens.|
|Hero CTA| Click call-to-action button.| User is redirected to the intended page.|
|Create account button| Click the button.| Registration page opens.|
|Footer links| Click footer links.| Links navigate to the correct pages.|
|Footer social icons| Click icon.| External social media link opens.|
</details>

<details><summary>Registration page</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Username field| Leave field empty and submit the form.| Validation message displayed.|
|Email field| Enter invalid email address.| Validation message displayed.|
|Password field| Enter invalid password.| Validation message displayed.|
|Confirm password| Enter invalid password| Validation message displayed.|
|Create account| Submit valid registration details.| Account created.|
|Success flash message| Complete registration.| Success message displayed.|
|Welcome email| Register new account| Welcome email received.|
 </details>

<details><summary>Login and Password reset</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Username field| Enter invalid username field.| Login prevented and error message displayed.|
|Password field| Enter incorrect password.| Error message displayed.|
|Login Button| Submit valid credentials.| User redirected to dashboard.|
|Forgot password link| Click link| Forgot password page opens.|
|Success flash message| Login successfully.| Success message displayed.|
|Send reset link| Enter valid email and click button.| Reset password email received.|
|Reset link| Click password reset link from email.| Password reset frm opens.|
|Password update| Submit a new valid password.| Password updates successfully and user redirected to login page.|
|Reuse reset link| Click the same password reset link.| Reset request rejected and user informed that the token is invalid or already has been used.|
|Old password check| Attempt to reset password using current password| Password change prevented and validation message displayed.|
|Success Flash message| Successfully reset password| Confirmation message displayed.|
</details>

<details><summary>User Dashboard</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Quick links access| Click each quick access button.| Correct page opens.|
|View All Recipes link| Click link.| Opens My recipes and displayes all recipe cards.|
|View Breakfast Recipes link| Click link.| Only displayed Breakfast recipes.|
|View Lunch Recipes link| Click link.| Only displayed Lunch recipes.|
|View Dinner Recipes link| Click link.| Only displayed Dinner recipes.|
|View Dessert/Snack Recipes link| Click link.| Only displayed Dessert/Snack recipes.|
|View All Meals plans| Click link.| Opens My meal plans page.|
|View today`s meals| Click link.| Opens Daily Meal planner.|
|Add Meal button| Click button.| Opens add meal plan form.|
</details>

<details><summary>Recipe management</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Add new recipe button| Click button.| Opens add recipe form.|
|Required fields| Submit empty form.| Validation messages displayed.|
|Recipe image upload| Upload valid image.| Image saved to database.|
|Save Recipe button| Submit valid recipe.| Recipe saved successfully.|
|Cancel button| Click cancel.| User returned to previous page.|
|Flash message| Save recipe.| Success message displayed.|
|Edit recipe button| Click button.| Recipe edit form opens, data populated.|
|Update recipe button| Update recipe information and click button.| Changes saved successfully, flash message displayed.|
|Delete Recipe button| Click button, then click yes, delete.| Recipe removed successfully.|
|View Recipe link| Click link| Open recipe details page.|
|Search field| Type keyword anc click search.| Displayed recipes from user`s recipe collection.|
|Add another recipe button| Click button.| Add recipe form opens.|
|Previous page button| Click button.| Previous page displayed.|
|Next page| Click button.| Next page displayed.|
</details>

<details><summary>Meal Planner</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Previous Week button| Click button.| Previous week displayed.|
|Next week button| Click button.| Next week displayed.|
|View past meals button| Click button.| Daily meals for past day displayed.|
|Edit and Delete actions| Open past meals page| No edit and delete options available.|
|View Meals button| Click button.| Displayed daily meals for selected day.|
|View Grocery List link| Click link| Redirect to weekly grocery list page.|
|Add Meals button| Click button.| Opens add meal plan form. If already meal selected opens Edit meal plan form.|
|Select recipe for each category| Click select option.| Choose recipe.|
|Save meal plan button| Submit valid meal plan.| Meal plan created successfully, user redirected to daily meal plan.|
|Add Breakfast button| Click button.| Opens single meal plan form, date and breakfast category pre-selected.|
|Add Lunch button| Click button.| Opens single meal plan form, date and lunch category pre-selected.|
|Add Dinner button| Click button.| Opens single meal plan form, date and dinner category pre-selected.|
|Add Dessert-snack button| Click button.| Opens single meal plan form, date and dessert/snack category pre-selected.|
|Edit meal plan button| Click button.| Open edit meal plan form.|
|Update meal plan| Click button.| Changes saved successfully.|
|Delete Meal Plan| Click button, then click yes, delete.| Meal plan for this category removed successfully.|
</details>

<details><summary>Discpver Recipes</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Discover recipes link| Click discover recipes link.| Redirect user to discover recipe page.|
|Search field| Type keyword and click button.| Matching recipes retrieved and displayed.|
|Category filter| Select recipe category.| Results are filtered according to the selected category.|
|Search button| Click search after entering keyword.| Search results from both APIs loaded successfully.|
|Recipe cards| View recipe cards from APIs| Full recipe details loaded, external recipe link can be open.|
|Import recipe button| Open API recipe, click button.| Recipe saed successfully to user`s recipe collection and database.|
|View imported recipe button| Click button.| Redirect to saved recipe details page.|
</details>

<details><summary>Support page</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Message field| Submit empty form.| Validation message displayed.|
|Send message button| Submit valid message.| Message sent successfully.|
|Flash message| Submit form.| Success message dispalyed.|
|Confirmation email| Submit support form.| Confirmation email received.|
</details>

<details><summary>Admin Dashboard</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Admin login| Log in using admin credentials.| Admin user logged in successfully, redirect to admin dashboard.|
|Admin login| Enter incorrect details.| Access denied, user not able to open admin dashboard.|
|Guest access| Try open admin dashboard.| User redirected to login page.|
|View Support messages button| Click button.| Submitted suport messages are displayed.|
|Delete button| Click button.| Remove message successfully.|
|View button| Click button.| View support message details page.|
</details>

### Backend Functionality Testing

In addition to front-end testing, backend functionality of Cookfolio was verified throughout development. Database records were checked after create, update, and delete operations to ensure data integrity. Authentication and authorization were tested using Flask-Login, while API integrations were verifies through successful requests to external recipe services. Form validation, route protection, session management, email functionality and database relationships were also tested to confirm correct server-side behaviour.

Backend testing confirmed that Cookfolio correctly handles authentication, authorization, database operations, form validation, ownership checks, API integrations, email functionality, security measures, and deployment requirements. Testing demontrates that data is processed securely and consistently across local and production development.

<details><summary> Authentication and Authorization</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|User Registration| Register new account with valid details.| Account created successfully and stored in the database, welcome email send to new user.|
|User Registration| Register new account with incorrect details.| Account is not created and flash message displayed.|
|User Login| Login with valid credentials.| User authenticated and redirected to dashboard.|
|Invalid Login| Login with incorrect credentials.| Login prevented and validation message displayed.|
|Logout| Click logout button.| User session ended successfully.|

<img src="">

</details>

<details><summary> Route Protection</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Protected Routes|Access dashboard without logging in.| User redirected to login page.|
|Recipe Management| Access add/edit recipe route as guest.| Access denied and login required.|
|Admin Routes| Access admin as normal user.| Access denied successfully.|
|Archive Meal Plan Protection| View past meal plans.| Read-only access is provided, preventing from deleting and updating.|

<img src="">

</details>

<details><summary> CRUD Database Operations</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Create Recipe| Submit new recipe form.| Recipe stored in database.|
|Read Recipe| Open recipe detail page.| Recipe information retrieved correctly.|
|Update Recipe| Edit recipe details.| Changes saved successfully.|
|Delete Recipe| Delete recipe and confirm deletion.| Recipe removed from database.|

<img src="">

</details>

<details><summary> SQLAlchemy Model Relationships</summary>

| **Feature** | **Test case** | **Outcome** | **Relationship**|
|-------------|---------------|-------------|-----------------|
|User -> Recipe| Create a recipe while logged in as a user.| Recipe is linked to the correct user.| One User -> Many Recipes.|
|Recipe -> User| Open saved recipe record.| Recipe ownership correctly identifies the user.| One Recipe -> One User.|
|Category -> Recipe| Assigned a recipe to a category.| Recipe appears under the selected category.| One Category -> Many Recipes.|
|Recipe -> Category| Open a recipe detail page.| The correct category information is retrieved and displayed.| One Recipe -> One Category.|
|User -> Meal Plan| Create a meal plan entry.| Meal plan is linked to the user.| One User -> Many Meal Plans.|
|Meal Plan -> User| Retrieve meal plan records.| Meal plans ownership correctly identifies the user.| One Meal plan -> One User.|
|Recipe -> Meal Plan| Add a saved recipe to meal plan.| Meal plan referenced the correct recipe record.| One Recipe -> Many Meal Plans.|
|Meal Plan -> Recipe| View meal plan entry.| The associated recipe details are retrieved successfully.| One Meal Plan -> One Recipe.|
|User -> Support Message| Submit a support message while logged in.| Support message is linked to user account.| One User -> Many Support Messages.|
|Support Message -> User| View support message in admin panel.| Admin could identify which user submitted each message.| One Support Message -> One User.|

<img src="">

</details>

<details><summary> Database Verification</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|User Records| Verify registered users in database.| User records stored correctly.|
|Recipe Records| Verify recipes after creation.| Recipe data saved correctly.|
|Meal Plan Records| Verify meal plans entries.| Meal plans stored correctly.|
|Support Messages| Verify support messages table.| Messages stored successfully.|
|Foreign Keys| Verify relationships between models.| Relationships functioning correctly.|

<img src="">

</details>

<details><summary> Session Management</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Login Session| Login and navigate site.| Session maintained correctly.|
|Logout Session| Logout and access dashboard| Access denied after logout.|
|Session Persistance| Refresh browser after login.| User remains authenticated.|

<img src="">

</details>

<details><summary> Form Processing and Validation</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Required Fields| Sumbit empty form.| Validation errors displayed.|
|Email Validation| Enter invalid email address.| Form submission blocked.|
|Password Validaiton| Enter invalid password.| Validation message displayed.|
|Recipe Validation| Submit incomplete recipe.| Form prevented from submitting.|
|Form Data Retention| Submit the form with an error.| Previously entered data remained in form.|
|Date Persistence| Select a future date and open the Add Meal Plan form.| Selected date is preserved and the form is pre-filled with correct date value.|
|Meal Plan Category Pre-Population| Click **Add Lunch** from the Daily meal plan.| The selected date and category are automatically pre-selected fields in the form.|
|Form Pre-Population| Open an existing recipe/meal plan using Edit Recipe/Edit Meal Plan button.| All existing data is automatically loaded in the form.|
|Dashboard Recipe Category Filtering| Select a category from a dashboard.| Correctly filtered recipes by category and return only recipes matching the selected categoty.|

<img src="">

</details>

<details><summary> Flash Messages Functionality</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Success Mssages| Create recipe successfully.| Success message displayed.|
|Error Messages| Submit invalid form.| Error message displayed.|
|Warning Messages| Attempt restricted action.| Warning message displayed.|

<img src="">

</details>

<details><summary> Error Handling</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|404 Page| Visit invalid URL.| Custom 404 page displayed.|
|403 Page| Access restricted page.| Custom 403 page displayed.|
|500 Page| Trigger server error in testing environment.| Custom 500 page displayed.|

<img src="">

</details>

<details><summary> Password Reset System</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Request Reset| Submit registered email.| Reset email sent successfully.|
|Reset Link| Open reset link.| Reset form diplayed.|
|Password Update| Enter new password.| Password updated successfully.|
|Token Validation| Reuse token after password change.| Token rejected successfully.|

<img src="">

</details>

<details><summary> API Integration Testing</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|MealDB Search| Search API recipes.| Recipe returned successfully.|
|Spoonacular Search| Seacrh API recipes.| Results displayed correctly.|
|Import Recipe| Import API recipe| Recipe saved to database.|
|API Error Handling| Test unavailable API response.| User-friendly error shown.|
|API Recipe to Meal Plan| Add not imported recipe to meal planner.| Recipe first saved to database and then added to meal plan.|

<img src="">

</details>

<details><summary> Email Functionality</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Welcome Email| Register new user.|Custom welcome email received.|
|Password Reset Email| Request password reset.| Custom reset email received.|
|Support Confirmation Email| Submit support form.| Custom confirmation email received.|
|Admin notification Email| User submits support form.| Admin notification email received.|

<img src="">

</details>

<details><summary> Ownership Testing</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Edit Protectoin| User attempts to edit another user`s recipe.| Access denied.|
|Delete Protection| User attempts to delete another user`s recipe.| Access denied.|
|Recipe Visisbility| User views own recipes.| Only appropriate recipes displayed.|

<img src="">

</details>

<details><summary> Admin Access Control</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Admin Dashboard| Login as admin.| Access granted.|
|Non- Admin Access| Login as normal user.| Access denied.|
|Support Messaged| Admin view support messages.| Messages displayed successfully.|
 
<img src="">

</details>

<details><summary> Security Testing</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Password Hashing| check stored passwords.| Password stored securely as hashes.|
|Session Protection| Access protected route after logout.| Access denied.|
|Authorization checks| Attempt restricted actions.| Access prevented.|

<img src="">

</details>

<details><summary> Deployment Verification</summary>

| **Feature** | **Test case** | **Outcome** |
|-------------|---------------|-------------|
|Heroku Deployment| Open deployed application.| Application loads successfully.|
|PostgreSQL Connection| Verify production database.| Database connected successfully.|
|User Authentication| Login on production site.| Authentication functions correctly.|
|CRUD Operations| Create, read, update and delete recipes.| Functionality works in production.|

<img src="">

</details>

### Real User Testing

Cookfolio was tested by family members and friends using common user workflows including registration, recipe management, meal planning, grocery list generation, support messaging, and mobile browsing. Feedback confirmed that the website application is intuitive and easy to navigate. Users confirmed that flash messages provided clear feedback. Success, warning, and error messaging were displayed after actions such as registration, login, recipe creation, meal planning, support message submission, and password reset requests, helping users understand the result of each action. They also confirmed that all automated emails, including welcoming emails, password reset emails and support confirmation emails were received successfully. Email content was clear, professional, and provided feedback for each action performed withing the site. Users reported that the website was responsive and easy to use on mobile devices. Some users noted a slight delay during initial page load. Once loaded, navigation and functionality remained smooth and responsive. Performance optimisation remains an area for future improvements.

| **Tester** | **Task** | **Feedback** |
|-------------|---------------|-------------|
|Family Member 1| Register a new account and log in.| Registration and Login process are straighforward and easy to follow. Welcome email was received and the content was clear and informative.|
|Friend 1| Register a new account and log in.| Registration and Login process are straighforward and easy to follow. Welcome email was received and the content was clear and informative.|
|Family Member 1| Request password reset.| Password reset email was received immediately and the reset link worked as expected.|
|Friend 1| Request password reset.| Password reset email was received immediately and the reset link worked as expected.|
|Family Member 1| Add recipe and upload photo.| Recipe form was easy to complete.|
|Friend 1| Add recipe and upload photo.| Recipe form was easy to complete.|
|Family Member 1| Read recipe.| Recipe details were clear and easy to follow.|
|Friend 1| Read recipe.| Recipe details were clear and easy to follow.|
|Family Member 1| Edit a recipe.| Edit was clear and easy to follow. Details pre-filled made editing easy.|
|Friend 1| Edit a recipe.| Edit form was clear and easy to follow. Details were pre-filled and made editing easy.|
|Family Member 1| Delete a recipe.| The delete button was easy to find and the confirmation step helped prevent accidental deletion.|
|Friend 1| Delete a recipe.| The delete button was easy to find and the confirmation step helped prevent accidental deletion.|
|Family Member 1| Search Recipe.| Easy to search and find recipes by keywords or filter by category.|
|Friend 1| Search Recipe.| Easy to search and find recipes by keywords or filter by category.|
|Family Member 1| Create a weekly meal plan.| The meal planner was easy to understand and made meal organization easy.|
|Friend 1| Create a weekly meal plan.| The meal planner was easy to understand and made meal organization easy.|
|Family Member 1| Generate a grocery list.| Grocery list was useful but category grouping and merging would improve readability.|
|Friend 1| Generate a grocery list.| Grocery list was useful but category grouping and merging would improve readability.|
|Family Member 1| Browse on mobile device.| Website remained easy to navigate on mobile screen.  After loading the website performed smoothly, but the first page load could be faster.|
|Friend 1| Browse on mobile device.| Website remained easy to navigate on mobile screen. After loading the website performed smoothly, but the first page load could be faster.|
|Family Member 1| Submit a support message.| Confirmation message clearly indicate successfull submission. Confirmation email was received immediately.|
|Friend 1| Submit a support message.| Confirmation message clearly indicate successfull submission. Confirmation email was received immediately.|
|Family Member 1| Import API recipe.| The import process was straightforward and the recipe appeared immediately in recipe collection.|
|Friend 1| Import API recipe.| The import process was straightforward and the recipe appeared immediately in recipe collection.|
|Family Member 1| Logout.| Logout process was quick and easy to find from navigation menu.|
|Friend 1| Logout.| Logout process was quick and easy to find from navigation menu.|

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