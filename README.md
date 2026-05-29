# Cookfolio

![Responsive Mock-up](app/static/images/docs/cookfolio-mock-up.webp)

#### **By Silviya Hristova**

[Click here to view the live web application](https://cookfolio-dc589e41eddc.herokuapp.com/)

Cookfolio is a recipe management website that allows users to create, edit and organize their own recipes, plan weekly meals and discover new recipes. The application is designed to help users manage their cooking and meal planning in a simple and intuitive way.

This is the documentation for Cookfolio, a full-stack web application. It has been built using HTML5, CSS3, JavaScript, Python, Flask and a relational database. It has been developed for educational purposes as part of Code Institute Level 5 Diploma in Web Application Development.

---

## Table of content

- [**About**](#about)
- [**User Experience**](#user-experience)
    - [**User Stories**](#user-stories)
    - [**Strategy**](#strategy)
    - [**Scope**](#scope)
    - [**Structure**](#structure)
    - [**Skeleton**](#skeleton)
    - [**Surface**](#surface)
- [**Agile Planning and Development**](#agile-planning-and-development)
- [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Frameworks and Libraries**](#frameworks-and-libraries)
    - [**Database**](#database)
    - [**APIs**](#apis)
    - [**Testing and Validation Tools**](#testing-and-validation-tools)
    - [**Development Tools**](#development-tools)
    - [**Other Tools**](#other-tools)
- [**Database Design**](#database-design)
- [**Features and Functionality**](#features-and-functionality)
- [**Security Features**](#security-features)
- [**Future Enhancements**](#future-enhancements)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
    - [**Forking the Repository**](#forking-the-repository)
    - [**Cloning the Repository**](#cloning-the-repository)
    - [**Local Development**](#local-development)
    - [**Heroku Production Deployment**](#heroku-production-deployment)
- [**License**](#license)
- [**Credits**](#credits)
- [**Acknowledgements**](#acknowledgements)


## About

Cookfolio is a personal recipe management website designed to help users store, organise and manage their own recipes in one location. The website allows visitors to create an account, add new recipes, upload images, categorise content and edit or delete their recipes.

The website focuses on simplicity, usability and accessibility, using a mobile-first design approach to ensure a consistent experience across different devices. Secure authentication and user ownership controls are implemented to ensure that users can only access and manage their own content.

Cookfolio is developed as part of Code Institute Level 5 Diploma in Web Application Develoment and demostrate full CRUD functionality, relational database design, and server-side logic using Python and Flask.

Click [**here**](https://cookfolio-dc589e41eddc.herokuapp.com/) to view the live website.


## User Experience

### **User Stories**

#### **First-time visitor goals:**

- As a visitor, I want to view the homepage, so that I can understand what is the main goal of the website.
- As a visitor, I want to be able to create an account, so that I can save and manage my own recipes.
- As a visitor, I want to be able to log in so I can access my personal dashboard.
- As a visitor, I want to be able to contact the support to report issues or ask questions about the website.

#### **Registered User:**

- As an user, I want to log in , so that i can access my personal dashboard.
- As an user, I want to see a dashboard after logging in, so I can quickly access my recipes.
- As an user, I want to see my recipes on the dashboard.
- As an user, I want to add a new recipe.
- As an user, I want to upload image for my recipe.
- As an user, I want to view detailed recipe page, so that I can read the full instructions and ingredients.
- As an user, I want to edit my recipes, so that I can update them later.
- As an user, I want to delete recipes, so that I can remove recipes I no longer need.
- As an user, I want to see all my recipes in one place.
- As an user, I want to search recipes by keyword, so that I can quickly find a recipe.
- As an user, I want to be able to discover recipes.
- As an user, I want to filter recipes by category.
- As an user, I want to add recipes to a meal planner.
- As an user, I want to assign recipes to specific days, so I can plan meals ahead.
- As an user, I want to edit my meal plan.
- As an user, I want to remove recipes from my meal planner.
- As an user, I want to access the site on the mobile device.
- As an user, I want to log out of my account anytime.
- As an user, I want to contact support if there is an issue or to ask a questions about the website.
- As an user, I want confirmation that my message was sent.

#### **Site owner (Admin):**

- As an admin, I want to access an admin dashboard.
- As an admin, I want to view all support messages, that users sending.
- As an admin, I want users to register and log in.
- As an admin, I want each recipe to be linked to a specific user so that ownership is enforced.
- As an admin, I want to prevent users from editing or deleting recipes they do not own.
- As an admin, I want the site to be mobile-first.
- As an admin, I want a clean and consistent interface so that users can easily navigate the site.
- As an admin, I want to provide a support contact form so that users can report an issue.
- As an admin, I want the application to be scalable so that new features can be added in the future.
- As an admin, I want to restrict admin pages, so that only authorized users can access them.

### **Strategy**

The Cookfolio website is designed to solve common problem people face when cooking at home, such as losing favourite recipes, struggling to plan meals for the week and finding ispriration for new dishes. The website is designed for home cooks who want to organize their personal recipes, people who want to plan their meals more efficiently, users looking for inspiration and individuals who want a simple digital cookbook accessible from any device. 

The primary goal of the Cookfolio website is to design and develop a full-stack user-friendly web application that allows users to create, manage and organize their personal recipes, plan meals and discover new dishes in a simple and organised way.

The project aims to demostrate the following objectives:

- Implement user authentication and management using Flask.
- Provide full CRUD functionality, allows users to create, read, update, and delete their own recipes.
- Enforce data ownership to ensure users can only manage content they have created.
- Design a relational database schema that supports structures data storage.
- Apply a mobile-first approach to ensure the website is accessible and usable across different devices.
- Follow accessibility best practices, including clear navigation, readable typography and sufficient colour contrast.
- Produce clear planning documentation, wireframes, page-flow diagrams and database schema design.
- Maintain a clean codebase using version control and regular commits.

### **Scope**

The Cookfolio website is designed to allow users to manage their personal recipes, organize cooking content, and plan meals efficiently. The site includes core features that allows users to create and manage recipes and meal plans, while also providing additional tools such as recipe discover, quick access links, empty states and support form to enhance the overal user experience.

#### **Core features**

The following core features are implemented in the Cookfolio application:

- User Authentication - user can create an account, log in, and log out anytime and reset password.

- Secure autentication and protected routes.

- Recipe Management (CRUD functionality) - users can create, view, edit and delete recipes. Each recipe contains details such as title, ingredients, instructions, preparation time, servings and category.

- Recipe Category - Recipes can be organised into categories such as breakfast, lunch, dinner or desserts/snack to make browsing easier.

- Recipe Image Upload - users can upload images for their recipes, allowing each recipe to include a visual representation of the dish.

- Recipe Search and Filtering - users can search for recipes by title or category to find quickly recipes they need.

- Meal Planner (CRUD functionality) - users can create, view, edit and delete meal plans. User can assign recipes to specific days of the week, allowing them to plan meals in advance. User cannot add, edit or delete past meals, but is able to view them.

- Grocery list generation based on meal plans.

- Responsive mobile-first design for mobile, tablet and desktop devices.

- Admin-only access for admin dashboard.

#### **Additional features**

To enhance the user experience, the following additional features are implemented in Cookfolio website:

- API recipe search - two API have been implemented for best expirience TheMealDB and Spoonacular.

- Recipe Discover - users can explore new recipes using an external recipe API, allowing them to discover new dishesh and ideas.

- Dashboard with quick-access navigation 

- Empty-state dashboard sections

- Support Page - users can send support messages through a contact form if they encounter issues or have questions about the application.

#### **Error Handling**

The website includes custom error pages to improve the user experience:

- 403 Access Denied Page - displayed when a user attempts to access a restricted resource.

- 404 Page Not Found - displayed when a user navigates to a page that does not exist.

- 500 Server Error - displayed when an unexpected server error occurs.


### **Structure**

The structure of Cookfolio is designed to provide a clear and logical flow based on the user`s authentication status and interaction flow. The website separates guest and authenticated user experiences, allowing visitors to explore the website before creating an account, while providing registered users with access to advances features such as recipe management and meal planning and grocery list generation. 

Unathenticated users can access the Home page, Login page, Registration page, Discover page and Support page. The Home page introduces the purpose of the application and guides users toward account creation and autentication through clear call-to-action section and navigation links.

Once authenticated, users are redirected to the Dashboard, which acts as the central hub of the application. From the dashboard, users can quickly navigate to key areas including My recipes, Add Recipe, Meal Planner, Grocery list, Discover Recipes and Support pages. The dashboard structure is designed to prioritise commonly used actions and improve usability.

Recipe management follows a structured CRUD workflow, allowing user to create, view, edit and delete recipes through consistent form layouts and navigation. Recipe detail page provide structured information including ingredients, instruction, category, preparation time and servings.

Meal planning functionality is structured around daily and weekly planning workflows. Users can organize meals into categories such as Breakfast, Lunch, Dinner and Dessert/Snack, while grocery list generation is connected to planned meals to support a smooth user experience.

Navigation is handled through a navigation bar and a mobile-friendly hamburger menu, providing access to key areas such as dashboard, meal planner, support page, log out. Logging out ends the user session and redirects the user back to the Login page.

The overall structure supports a predictable, intuitive and responsive user journey, ensuring that users can move through the website efficiently. 

A custom 403, 404 and 500 error pages are implemented to handle errors. The pages provide clear feedback to users and offers navigation back to the Home or Dashboard page, ensuring smooth and controlled user experience.

### **Skeleton**

Low-fidelity wireframes were created during the planning stage to define the skeletal structure of the website before development began. These wireframes focus on layout, content hierarchy and user flow rather visual design or styling.

Wireframes were created using Figma to plan the structure of each page. These wireframes helped ensure that the interface is organised logically and that users could easily navigate between different features of the application. They were designed using a mobile-friendly approach, ensuring that the website would be responsive and function effectively across mobile, tablet and desktop devices. Wireframes were created for mobile and desktop layout for the main pages of the website, including Home page, Login page, Register page, User Dashboard, Empty user Dashboard, My recipe page, Recipe detail page, Add recipe page, Edit recipe page, Delete page, Meal planning page, Discover recipes page, Support page, Search result page, Error pages 403, 404 and 500.

<details><summary>Desktop</summary>

<img src="app/static/images/docs/wireframes/home-page-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/register-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/login-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/empty-dashboard-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/dashboard-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/my-recipes-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/recipe-detail-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/add-recipe-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/edit-recipe-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/delete-recipe-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/meal-planner-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/discover-recipe-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/search-results-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/support-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/403-page-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/404-page-desktop.webp" width=250px>
<img src="app/static/images/docs/wireframes/500-page-desktop.webp" width=250px>

</details>

<details><summary>Mobile</summary>

<img src="app/static/images/docs/wireframes/home-page-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/register-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/login-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/empty-dashboard-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/dashboard-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/my-recipes-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/recipe-detail-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/add-recipe-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/edit-recipe-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/delete-recipe-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/meal-planner-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/discover-recipe-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/search-results-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/support-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/403-page-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/404-page-mobile.webp" width=250px>
<img src="app/static/images/docs/wireframes/500-page-mobile.webp" width=250px>

</details>

### **Surface**

**Colour**

The color palette for Cookfolio was selected to create a warm, inviting,and food-insired visual dentity. The colors were choosen to be associated with cooking, freshness and appetite while maintaining good readability and accessibility across devices. The palette combines warm and natural tones associated with food, ingredients and kitchen environments. Red colour is strongly associated with food and appetite. It is commonly used in food branding because it attracts attention and simulates hunger. In Cookfolio red is used for primary buttons and important actions such as adding and saving recipes. Green colour represents freshness, vegetables and healthy ingredients. It helps balance the strong red tone. The colour is used for confirmation actions and success messages. A light grey background colour was selected to create a clean and neutral interface that allows recipe and images to stand out without overwhelming the user. Dark grey used for body text to maintain strong readability. White colour is used to provide contrast and maintain a clean layout. The selected colours were choosen with accessibility in mind. The palette were created using the site [Color-hex.com](https://www.color-hex.com/). Tints and Shades of these colours will be used also and are created using the site [Maketintsandshade.com](https://maketintsandshades.com/).

![Colour Pallette](app/static/images/docs/cookfolio-colorpalette.webp)

<details><summary>Tints and shades</summary>

![Tints and shades](app/static/images/docs/cookfolio-tintandshades.webp)

</details>

**Typography**

The fonts that will be used in the website will be imported from [Google Fonts](https://fonts.google.com) and will be used [Poppins](https://fonts.google.com/specimen/Poppins) and [Open Sans](https://fonts.google.com/specimen/Open+Sans). They were choosen to ensure readability, visual balance and friendly interface, that reflects the theme of cooking. This is combination of modern sans-serif fonts that provide clarity and welcoming. Poppins was selected for headings and important interface elements. The font provides strong visual hierarchy, making it easy for users to identify page titles, section headings and important actions within the interface. Open Sans is used for body text because it is highly readable across different devices. The clean design ensures that longer section of the text, such as recipe instructions adn ingredient lists remain comfortableto read. Headings are used to structure content and important section, while body text will provide detailed information in a readable format.

**Logo**

The Cookfolio logo is created using [ChatGPT](https://chatgpt.com) logo design tool. It represent the concept of the digital cookbook where users can organise and manage their personal recipes. The design combines visual elemenents related to cooking and food preparation, helping users immediately understand the purpose of the application. The visual style of the logo is friendly and welcoming, simple and modern. The colours used in the logo follow the same colour palette used throughout the Cookfolio interface. This consistency help to strenghten the brand identity of the website. The logo is used primarily in the navigation bar, where it also functions ad a clickable element that allows users to return to the home page.

<details><summary>Logo image</summary>

![Cookfolio Logo](app/static/images/logo-image.webp)

</details>

**Images**

Images are important in the Cookfolio website. They making the interface more engaging and visually appealing. Food-related images help users connect with recipes. The images used in the website support the theme of cooking and meal preparation while helping users better understand the content presented on each page. Users are able to upload images for their recipes. These images help users quickly identify recipes and make browsing more easier. Recipe images also help create a more realistic digital cookbook experience where user can visually explore meals before deciding what to cook. All images used across the website include similar style, colour theme and layout placement across different pages. 

**Icons**

Icons are used across the website to improve usability and provide clear visual interface for users. Icons help users quickly identify actions and features without needing to read detailed instruction, which improves the user experience. The icons were sources from [Font Awesome](https://fontawesome.com/) website. 

[Back to top](#table-of-content)

## Agile Planning and Development

### Agile Workflow

Cookfolio was developed using an Agile workflow approach, allowing features to be planned, built, tested and improved continuously throughout development. The project was developed iteratively in small staged rather than attempting to build all functionallity at once. The approach helped maintain organized development, continuous improvement and a user-focused design process throughout the project development.

### Development Process

The project followed a feature-by-feature workflow:

* Planning the feature and user functionality.
* Designing layouts and database structure.
* Implementing back-end functionality using Flask and SQLAlchemy.
* Building front-end template and responsive layouts.
* Testing functionality manually and automatically.
* Debugging and improving responsiveness.
* Committing changes regularly to GitHub.
* Deploying updates to Heroku.
* Refining the feature based on usability and accesibility improvements.

This workflow allowed features to be developed incrementally while maintaining project stability and organisation.

### Iterative Development

Cookfolio was continuously improved throughout development. Examples of improvements include:

- dashboard redesign and layout refinements
- meal planner usability improvements
- grocery list enchancements
- responsive design improvements
- accessibility and color countrast improvements
- validation and flash messages improvements
- password reset enchancements and etc.

### MoSCoW Prioritisation

MoSCoW Prioritisation was used to organize features based on project importance and development priority.

#### Must Have

- User Authentication system
- Recipe CRUD functionality
- Meal Planner
- Responsive design
- Database integration
- Search functionality
- Heroku deployment

#### Should Have

- Automated testing
- Password reset functionality
- API recipe integration
- Grocery list generation

#### Could Have

- Recipe favourites
- Recipe Cooking mode slider
- Recently view
- Recomended recipes
- Nutrition tracking
- Enchanced CSRF protection and additional form security improvements

#### Won`t Have (Current Version)

- Analytic Dashboard
- User Profile 
- Real-time recipe sharing and commenting

### GitHub and Version Control

Git and GitHub were used for version control and workflow management throughout the development. The workflow included:

- Small and frequent commits
- Descriptive commit messages using feat, fix, style, test, docs, chore.
- Feature-by-feature development
- Continuously updates
- debugging and testing

### Continuous Testing

Testing was integrated throughout the development. The testing process included:

- Manual testing
- Responsive testing
- Browser compatibility testing
- Automated testing with Pytest and Plawright
- Accessibility testing
- Validation testing

[Back to top](#table-of-content)

## Technologies Used

### Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5) - used to structure the website pages, forms, navigation and content layout.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - used for custom styling, responsive design, animation and layout improvements.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - used for interactive front-end functionality.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - used back-end programming language for logic, routing, autentication, database interaction and server-side functionality.

### Frameworks and Libraries

+ [Flask](https://flask.palletsprojects.com/en/stable/)
    + used to handle application routes, server-logic, configuration and app structure.
+ [Flask-SQLAlchemy](https://flask.palletsprojects.com/en/stable/patterns/sqlalchemy/)
    + used to simplify database integration and to manage database models and relationships within the Flask application.
+ [Flask-Login](https://flask.palletsprojects.com/en/stable/logging/)
    + used to manage user autentication, login sessions, route protection and user session handling.
+ [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html)
    + used to manage database migrations and apply database schema changes during development and deployment.
+ [Flask-Mail](https://flask-mail.readthedocs.io/en/latest/)
    + used to send welcome, password reset emails and support-related emails.
+ [SQLAlchemy](https://www.sqlalchemy.org/)
    + used ORM to interact with the database using Python models.
+ [Jinja2](https://jinja.palletsprojects.com/en/stable/)
    +  used as templating engine for dynamically rendering HTML pages and displaying data from the Flask.
+ [Bootstrap 5](https://getbootstrap.com/)
    + used to create the structure and layout of the website, making it responsive on all devices.

### Database

+ [SQLite](https://sqlite.org/index.html)
    + used as local development database during project building and testing.
+ [PostgreSQL](https://www.postgresql.org/)
    + used as production database for the deployed Heroku application

### APIs

+ [TheMealDB API](https://www.themealdb.com/)
    + used to provide external recipe data and functionality.
+ [Spoonacular API](https://spoonacular.com/)
    + used to provide external recipe data and functionality.

### Testing and Validation Tools

+ [Pytest](https://docs.pytest.org/en/stable/)
    + used for automated back-end testing -route, CRUD, authentication and validation testing.
+ [Playwright](https://playwright.dev/)
    + used for front-end testing across different user workflows and responsive layout.
+ [Flake8](https://flake8.pycqa.org/en/latest/)
    +  used to check Python code quality and PEP8 compliance throughout the project.
+ [Black](https://ichard26-testblackdocs.readthedocs.io/en/stable/usage_and_configuration/the_basics.html)
    + used as an automated Python code formatter to maintain consistent code readability and styling.
+ [Autopep8](https://pypi.org/project/autopep8/)
    + used to automatically format Python cod and fix PEP8 style issues such as spacing and line formatting. 
+ [Autoflake](https://pypi.org/project/autoflake/)
    +  used to remove unused imports and clean unnecessary Python code elements.
+ [W3C HTML Validator](https://validator.w3.org/nu/)
    + used to validate HTML files.
+ [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    + used to validate CSS file.
+ [JSHint](https://jshint.com/) 
    + used to validate JS files.

### Development Tools

+ [Git](https://git-scm.com/docs)
    + used for version control and tracking project changes throughout development.
+ [GitHub](https://github.com/)
    + used to store the project repository, manage commits and support deployment.
+ [VS Code](https://code.visualstudio.com/)
    +  used code editor for project development and debugging.
+ [Heroku](https://www.heroku.com/)
    + used to deploy and host the production version of the application.
+ [Heroku CLI](https://www.heroku.com/)
    + used to manage Heroku application through the terminal, including deployment, migrations, view logs, configuration managemnt and remote app access.
+ [Gunicorn](https://gunicorn.org/)
    + used as production server for running Flask application on Heroku.
+ [Pip](https://pip.pypa.io/en/stable/index.html)
    +  used to install and manage Python package dependencies for the project.
+ [Virtual Env](https://docs.python.org/3/library/venv.html)
    + used to create Python environment. 
+ [python-dotenv](https://www.heroku.com/)
    + used to manage variables in .env file such as API keys, secret keys, email credentials and admin testing details.
+ [psycopg](https://www.psycopg.org/)
    + used as PostgreSQL database adapter to connect Flask application to the production database.
+ [werkzeug](https://werkzeug.palletsprojects.com/en/stable/)
    + used for password hashing and Flask support functionality.

### Other Tools

+ [Google Fonts](https://fonts.google.com/)
    + used to get the links to the fonts that are in the head of the html pages. These fonts are then used throughout the website.
+ [Font Awesome](https://fontawesome.com/)
    + used to add icons to the project.
+ [Figma](https://www.figma.com/)
    + used to create the wireframes and design layout for the project.
+ [Pixelied](https://pixelied.com/convert/)
    + used to convert PNG and JPG images to WEBP format images.
+ [Favicon](https://favicon.io/)
    + used to create the favicon for the website.
+ [Color-hex](https://www.color-hex.com/)
    + was used to create the colour palette that was used through the website.
+ [Make Tints and Shades](https://maketintsandshades.com/)
    + used to create the tints and shades from the main colour palette for use on the whole site.
+ [Grammarly](https://app.grammarly.com/)
    + used to check spelling, grammar, and punctuation in the content of the website.
+ [WebAIM](https://webaim.org/resources/contrastchecker/)
    + used to check the color contrast.
+ [WAVE Web Accessibility](https://wave.webaim.org/)
    + used to make web content more accessible to individuals with disabilities.
+ [Mock-up Image](https://amiresponsive.blogspot.com/)
    + used to create the responsive mock-up image that is at the beginning of the readme file.
+ [Google Dev Tools](https://developer.chrome.com/docs/devtools)
    + used to test features, responsiveness and to troubleshoot.
+ [Chrome Capture - screenshot & gif tool](https://chromewebstore.google.com/detail/chrome-capture-screenshot/ggaabchcecdbomdcnbahdfddfikjmphe?hl=en-US&utm_source=ext_sidebar)
    + used to take screenshots and screen record to use in the Readme file.
+ [GIF Compressor](https://www.freeconvert.com/gif-compressor)
    + used to compress gif files to use in the Readme file.
+ [Node JS](https://nodejs.org/en)
    + used to install and manage playwright testing dependencies.
+ [ChatGPT](https://chatgpt.com/)
    + used to create logo and images related for the website, debugging tool and also to check my spelling and improve my sentences in Readme and Testing files.
+ [DB schema diagram](https://dbdiagram.io/home)
    + used to create database schema diagram to show relationships between database models.
+ [MIT License](https://choosealicense.com/)
    + used to help to select open-source license for the project providing permissions, conditions and limitations.
+ [Markdown](https://www.markdownguide.org/)
    + used to structure and format The README and TESTING documentations.

[Back to top](#table-of-content)

## Database Design

Cookfolio uses a relational database structure managed with [SQLAlchemy](https://www.sqlalchemy.org/). The database is designed to support user authentication, recipe management, meal planning, and future features. [SQLite](https://sqlite.org/index.html) was used during local development, while [PostgreSQL](https://www.postgresql.org/) was used in the deployed Heroku production environment. The database structure was planned and visualised using [DB schema diagram](https://dbdiagram.io/home). Main database models are User model, Category model, Recipe model, Meal Plan model and Support messages model. The database relationships were designed to maintan structured and connected data in the application. Foreign keys were used to maintain relationships between users, recipes, categories, meal plans and support messages. [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html) was used to manage database migrations throughout development. Migrations were also applied to the Heroku PostgreSQL production database during deployment.

![Cookfolio Database Schema](app/static/images/docs/cookfolio-database-schema.png)

### User model

- The User model stores user account information and authentication data. Main fields include id, username, email, password_hash.

- Relationships: 
    - One user can have many recipes.
    - One user can have many meal plans.
    - One user can have many support messages.

### Category model

- The Category model stores recipe categories used in the application. Main fields include id, name, order. Order field used for a consistent category order across the application.

- Relationships:
    - One category can contain many recipes.

### Recipe model

- The Recipe model stores recipe information created and managed by users. Main fields are id, title, ingredients, instructions, prep_time, servings, image_url, user_id and category_id.

- Relationships:
    - Each recipe belongs to one user.
    - Each recipe belongs to one category.
    - One recipe can appear in many meal plans.

### Meal Plan Model

- The Meal Plan model stores planned meals for users. Main fields are id, meal_date, meal_type, user_id and recipe_id.

- Relationships: 
    - Each meal plan belongs to one user.
    - Each meal plan belongs to one recipe.

### Support Message Model

- The SupportMessage model stores support requests and feedback submitted by the users through the support/contact form. Main fields are id, user_id, name, email, subject, messages.

- Relationships:
    - One user can submit many messages.

[Back to top](#table-of-content)

## Features and Functionality

### Header and Navigation

<details><summary>Screenshots</summary>

* Desktop header

<img src="app/static/images/docs/cookfolio-header-desktop.png"> 

* Mobile header

<img src="app/static/images/docs/hamburger-menu.png"> <img src="app/static/images/docs/cookfolio-header-guest.png"> 
<img src="app/static/images/docs/cookfolio-header.png">
</details>

* Frontend functionality
    * Cookfolio includes a fully responsive header and navigation systems that remains consistent across all pages of the website. The navigation bar allows users to quickly access important areas such as the Dashboard, Discover recipes, Meal plans, Login, Sign up, My recipes and etc. The website logo is clickable and redirects users back to the homepage, improving usability and navigation flow. Navigation links dynamicaly change depending on whether the user is logged in or logged out, ensuring users only see actions relevant to their account status. On small devices, the navigation collapses into a mobile-friendly hamburger menu to improve usability and prevent overcrowding on narrow screens.

* Backend functionality
    * The navigation system is powered using Flask templating and conditional Jinja logic. Flask-Login is used to determine whether a user is authenticated. Protected pages use route decorators to ensure only authenticated users can access restricted areas such as Dashboard, My recipes, Meal Plans, Grocery lists, Admin features. Unathenticated users attempting to access protected pages are redirected to the login page with feedback messages.

* Technical Reasoning
    * A consistent navigation system improves uasability and reduces user confusion. Dynamic navigation prevents users from seeing inaccessible options while also improving security and user expirience. Responsive components were used to ensure the navigation adapts across mobile, tablet, desktop and large desktop screens.

### Footer

<details><summary>Screenshots</summary>

* Mobile Footer

<img src="app/static/images/docs/cookfolio-footer-mobile.png"> 

* Desktop Footer

<img src="app/static/images/docs/cookfolio-footer.png">
</details>

* Frontend functionality
    * Cookfolio includes a consistent footer across all pages to provide users with quick access to imprortant information and navigation links. The footer contains Navigation links, Social media icons, Copyright information, and for larger screens logo. The footer hepls create a professional appearance while improving overall website navigation. 

* Backend functionality
    * Footer content is managed through reusable base template using Jinja templating, allowing consistent rendering across all pages.

* Technical Reasoning
    * Using a shared footer inside the base template reduces duplicate code and improves usability across the application. The footer layout automatically adjust depending on screen size.

### Buttons and Links

<details><summary>Screenshots</summary>

<img src="app/static/images/docs/buttons-home.png"> <img src="app/static/images/docs/buttons-dashboard.png"> <img src="app/static/images/docs/buttons-navigation.png">
<img src="app/static/images/docs/button-recipe.png"> <img src="app/static/images/docs/buttons-meal-plan.png"> <img src="app/static/images/docs/buttons-meal.png"> 
<img src="app/static/images/docs/links-dashboard.png">
</details>

* Frontend functionality
    * Buttons and links are styled consistently throughout the website using Bootstrap classes and custom CSS styling. Buttons provide users with clear actions such as Add Recipe, Edit Recipe, Delete Recipe, Update Meal, Log in, Cancel actions, View All Recipes, and etc. Clear button text improves usability and reduces user confusion. Hover effects imrpove visual feedback and accessibility.

* Backend functionality
    * Buttons trigger Flask routes connected to backend functoinality such as Database CRUD operations, From submissions, Redirects, Search requests, Meal plan updates and etc. Delete actions require authentication. Dangerous actions require POST requests. Buttons resize and stack depending on the screen size to ensure usability on mobile devices. Form buttons trigger backend actions such as creating records, updating database, deleting records, saving meals and recipes, sending password reset requests.

* Technical Reasoning
    * Consistent button styling improves visual hierarchy and creates a predictable user expirience across the website. They are improtant because they control how users move through the application and interact with features. Buttons and links improve navigation flow, user confidence, accessibility and security.

### Flash messages

<details><summary>Screenshots</summary>

<img src="app/static/images/docs/flash-message-add-meal.png"> <img src="app/static/images/docs/flash-message-add-recipe.png"> <img src="app/static/images/docs/flash-message-all-fields.png">
<img src="app/static/images/docs/flash-message-invalid-username.png"> <img src="app/static/images/docs/flash-message-select-one.png">
</details>

* Frontend functionality
    * Cookfolio uses flash messages to provide users with immediate visual feedback after actions are completed. Messages are displayed for actions such as Successful login, logout confirmation, Adding recipe, Recipe update, Delete recipe, Form validation errors, Password requests, Meal plan updates and etc. Messages are styled using Cookfolio custom color palette for visual consistency.

* Backend functionality
    * Flask Flash messaging is used to dynamically generate user feedback. Categories such as success, warning, danger and error are used to style messages differently depending on the situation. Flash messagin is implemented using flash() functionality. The backend dynamically generates messages after actions are processes inside the route. Messages are temporarily stored in the ser session and displayed after redirects using Jinja templating. Flash messages are passed alongside the message text to apply different Bootstrap alert styles. The base template renders all flash messages globally using a reusable alert component.

* Technical Reasoning
    * Flash messages improve security awaness by informing users when invalid input is detected ot action fail. Immediate feedback improves usability and helps user understand the result of their actions without confusion. Sensitive informations is not exposed inside messages such as login errors avoid revealing whether the username or password was incorrect. Flash messages are lighweight and session-based, making them efficient. Messages only exist temporarily and are automatically cleared after display.

### Favicon

<details><summary>Screenshots</summary>

* Desktop Favicon

<img src="app/static/images/docs/cookfolio-desktop-favicon.png">

* Mobile Favicon

<img src="app/static/images/docs/cookfolio-mobile-favicon.png" width=300px>
</details>

* Frontend functionality
    * Cookfolio includes a custom favicon displayed in browser tabs and bookmarks to improve branding and website recognition. The favicon creates more polished and professional appearance while strengthening the visual identity of the application. Feature include browsing tab icon, bookmark icon, mobile support shortcut.

* Backend functionality
    * Favicon files are stored within the static files directory and linked globally through the base template. Using Flask static routing ensures favicon files are server correctly in local development and deployed production environments. 

* Technical Reasoning
    * Favicon improve professionalism and help users identify the application quickly among multiple browser tabs. Favicons are lighweight assets and load quickly withot affecting page performance.

### Login and Registration

<details><summary>Screenshots</summary>

<img src="app/static/images/docs/register-form.png"> <img src="app/static/images/docs/login-form.png"> <img src="app/static/images/docs/welcome-email.png">
</details>

* Frontend functionality
    * Users can securely create accounts, log in, and log out using responsove authentication forms. Validation messages help users understand errors clearly during submission the form. Features include Login form, Registration form, Flash feedback messages, Forgot password functionality. Users can register with a username, email and password. Log in using their account details. Users can access protected pages only after logging in. The forms are designed to be simple and user-friendly, with clear label, helpful validation messages and buttons that guide the user through the process. Users will receive a welcome email after successful registration

* Backend functionality
    * AUthentication functionality is implemented using Flask-Login and Werkzeug password hashing. Passwords are hashed before storage in the database. User sessions are managed securely using Flask-Login and authenticated users gain access to protected routes and dashboard features. The backend manages creating new user accounts, checking if username or email already exist, hashing passwords, saving new user to database, sending a welcome email, validating login details, starting user sessions after successful login, logging users out, redirecting users based on the status, and protecting private pages with @login_required. User data is stored in the database using the User model. The welcome email is used to confirm registration, introduce to main features and encourage user to start using the website.

* Technical Reasoning
    * Authentication is essential for protecting user content such as recipes, meal plans, grocery lists and etc. Password hashing prevents sessitive user data from being stored insecurely. The login and registration system ensures that users can access only their own account content. The feature improves security and usability because users can safely manage their own cooking data inside a personalised account. The welcome email was added to make registration process feel complete and professional. It improves user onboarding, trus, comunication.

### Password Reset and Emails

<details><summary>Screenshots</summary>

<img src="app/static/images/docs/forgot-password.png"> <img src="app/static/images/docs/reset-form.png"> 
<img src="app/static/images/docs/reset-email.png">
</details>

* Frontend functionality
    * Users can request password reset emails when they forgot their password. The reset workflow provides clear instructions, validation messages, secure reset link send to user email and confirmation feedback. User can click the forgot password link from login page, enter registered email, receive a password reset email, open secure reset link and create new password. User can see clear flsah message during each step. Email functionality improves the user experience because user do not need to create new account if they forgot password.

* Backend functionality
    * Password reset functionality uses Flask-Mail, timed reset token, and secure token validation. The backend manage finding user by email, generate a secure password reset token, sending a reset email using Flask-Mail, validating the reset token when link is opened. Reset links expire after a limited period for securty purposes. Single-use token validation prevents reuse of old reset links. The reser email contains a secure link that redirects the user to their reset password form.

* Technical Reasoning
    * Password reset systems improve usability while maintaining account security and reducing support dependency. This is expected feature in modern-based websites. Using email-based reset links provides realistic and professional authentication system, It makes Cookfolio feel more complete and product-ready web application.

### Dashboard

<details><summary>Screenshots</summary>

* Empty state

<img src="app/static/images/docs/empty-dashboard.png" width=900px> 

* After adding recipe

<img src="app/static/images/docs/dashboard-with-recipe.png" width=900px> 

* Meal plan empty state when only recipes are saved

<img src="app/static/images/docs/dashboard-meal-empty.png" width=900px>

* Dashboard with meal plans and recipes

<img src="app/static/images/docs/meal-planner-dashboard.png" width=900px>

</details>

* Frontend functionality
    * The Cookfolio dashboard provides users with a central overview of their account activity and cooking management features. Dashboard features include Welcome message, Quick access links shortcuts, Recipe category cards with recipe statistic, Empty states and upcoming meal plans. The dashboard dynamically changes depending on whether the user has added recipes or not. Each category cards have recipe count and once opened showing only recipe from that category. User can see all recipes through the View all recipes link where recipes are shown from newest.

* Backend functionality
    * Dashboard data is dynamically generated using database queries and rendered using Jinja templates. Statistic include total recipes, each category recipe count, meal plan count. The backend retrive current logged in user, user`s saved recipes, recipe count, recipes group by category, upcoming meal plans, meal plans for current weeks.

* Technical Reasoning
    * Dynamic dashboard imrpove navigation, user engagement by presenting improtant information immediately after login and personalisation. This helps users find how many recipes have saves, what meals are planned, what to do next and etc.

### Recipe Management

<details><summary>Screenshots</summary>

* Add Recipe Form

<img src="app/static/images/docs/add-recipe-form.png" width=900px>

* View Recipe Page

<img src="app/static/images/docs/view-recipe.png" width=900px>

* Edit Recipe Form

<img src="app/static/images/docs/edit-recipe-form.png" width=900px>

* Delete Recipe

<img src="app/static/images/docs/delete-recipe.png" width=900px>

* My Recipes page

<img src="app/static/images/docs/my-recipes-page.png" width=900px>

* Empty state for My Recipe Page

<img src="app/static/images/docs/empty-my-recipes.png" width=900px>
</details>

* Frontend functionality
    * Cookfolio allows logged in users to create, edit, delete, and view recipes using user-friendly forms and recipe detail pages. Users can add new recipe, edit existing recipe, view recipe details, delete recipe, upload recipe image, add ingredients, cooking instructions, choose recipe category and view recipes in cards or grid and search and filter recipes. Recipe cards help users browse recipes visually, while recipe detail page gives more complete information such as ingredients, instructions, preparation time, servings and cateogry. When editing or creating recipes all entered information is preserved if validation fails. Users can correct individual fields without re-entering the entire recipe. To encourage recipe creation, Cookfolio displays an interactive Add Another Recipe card at the end of the user`s recipe collection. The card acts as a call-to-acion that allows users to quickly add new recipe from the same page.The card is displayed alongside existing recipe cards and follows the sae visual layout to maintain design consistency.

* Backend functionality
    * Recipe CRUD functionality is connected to SQLAlchemy models. Database operations include create recipe, read recipe, update recipe and delete recipe. Recipes are connected to users through database relationships, ensuring each user manages thier own recipe collection. The backend handles form validation, image handling, category selection, ingredients and instruction storage, database, redirects after actions and flash messages.

* Technical Reasoning
    * Recipe CRUD functionality forms the core foundation of the Cookfolio application and supports personalized cooking management. The full CRUD functionality was implemented to allow users to control their own content. This makes the website interactive and database-driven. Recipe management allows users to build a personal cooking collection inside Cookfolio.

### Meal Plan Management

<details><summary>Screenshots</summary>

* Add Meal Plan Form - single meal plan and daily meal plan forms

<img src="app/static/images/docs/add-recipe-to-meal.png" width=900px>
<img src="app/static/images/docs/add-daily-meal-form.png" width=900px>

* View Meal Plan

<img src="app/static/images/docs/daily-meal-plan.png" width=900px>
<img src="app/static/images/docs/view-daily-meal-plan.png" width=900px>

* Edit Meal Plan form - single meal plan and daily meal plan forms

<img src="app/static/images/docs/edit-single-meal.png" width=900px>
<img src="app/static/images/docs/edit-daily-meal-plan.png" width=900px>

* Delete Meal plan 

<img src="app/static/images/docs/delete-meal.png" width=900px>

* My Meal Plans page

<img src="app/static/images/docs/meal-planner-page.png" width=900px>
<img src="app/static/images/docs/meal-planner-page2.png" width=900px>

* Empty state for My Meal Plans page

<img src="app/static/images/docs/empty-my-meal-plans.png" width=900px>

</details>

* Frontend functionality
    * Cookfolio allows logged in users to organize meals into daily and weekly meal plans. Meal plans can be created after user has saved recipes in the database. Meal planner features are Breakfast slot, Lunch slot, Dinner slot, Dessert/Snack slot, Weekly navigation, Daily planning. User can add meal, edit meal, view meal and delete meal. Users can add meal plan for a selected date, choose recipe for different meal category, view daily meal plan, view weekly meal plan, edit existing plans, delete meal plans, navigate between weeks, plan future meals and view recipe images inside meal plan cards. Selected dates, meal categories, and recipe choices are preserved when validation errors ocur, helping users manage meal plans more efficiently. Cookfolio includes a Meal Plan archive feature that allows user to view previously planned meals while preserving historical records. Past meal plans remain accessible for reference, enabling users to review previous meal plans. Past meals are displayed in a read-only format. Users can browse and review archive meal plans, but cannot edit or delete them once the planned date has passed.

* Backend functionality
    * Meal plans are stored in the database and linked to users and recipes using relationships. Validation prevent duplicate meal categories for the same date. The backend manages saving meal plan to the database, linking meal plans to the logged in user, linking meal planto selected recipe, filtering meal plans by date, displaying weekly meal plans, displaying daily meal plans, deleting and updating meal plans, preventing duplicates recipes in the same daily plan, passing selected dates back to the templates, handling empty meal plan states. Meal plans are connected to User and Recipe models, allowing each user to manage their own planned meals.

* Technical Reasoning
    * Structured meal planning improves organization and increases application usefulness beyound recipe storage. It was added to make Cookfolio more useful than a basic recipe storage appication. Meal plan management helps users organise meals in advance, plan cooking weekly, reuse recipes, prepare grocery lists and improve cooking routine.

### Discover and Search

<details><summary>Screenshots</summary>

<img src="app/static/images/docs/discover-recipe-page.png" width=900px>

* API recipe detail page

<img src="app/static/images/docs/api-recipe.png" width=900px>
</details>

* Frontend functionality
    * Users can search recipes using keywords or browse categories through the Discover Recipe page. Feature include APIs recipe search, internal recipe search, category filter, pagination, recipe cards and search result pages. Users can search, browse, discover recipes, view recipe cards, open recipe detail pages, open external link, add recipe to meal plan and save imported recipes.

* Backend functionality
    * The application integrates external APIs to fetch recipe data dynamically. Pagination is implemented to improve performance and usability. The backend handles processing search queries, sending API requests, rendering cards dynamically, displaying API recipe details, manage internal database recipe searched.

* Technical Reasoning
    * Search and Discover features increase user engagement and improve content accessibility.

### API Integration

* Frontend functionality
    * Cookfolio integrates external recipe APIs to provide users with a larger variety of recipe beyound manually created content. API integration imrpoves the user exprerience by allowing users to discover, search and import recipes directly into the application. User can search, browse, view recipe images and details, improt recipes into their personal collection , add API recipe directly to meal plans, discover new meal ideas without manually creating recipes. Recipe cards display recipe image, recipe title, category, cooking information and action buttons.

* Backend functionality
    * Cookfolio uses external API requests to retrieve recipe data dynamically. The backend handles sending API requests, receiving JSON responses, parsing recipe data, mapping category, handle missing data and rendering results into template. The application converts API responses into structured Python dictionaries and objects before displaying them in the frontend. API integration is connected with Search routes, discover page, recipe page and meal plans functionality. Imported recipes are stored in the local database for long-term user access. Pagination was implemented to reduce page load times, improve performance and prevent overwhelming users with too many results. Category mapping was implemented to keep meal plan categories consistent, and improve filtering fnctionality.

* Technical Reasoning
    * API integration significantly improves the functionality and scability of the application. Without it, users would only have access to manually created recipes. External APIs allows Cookfolio to provide larger recipe variety, faster content discovery, better user engagement and dynamic content updates. This make Cookfolio modern platform. 

### Grocery List 

<details><summary>Screenshots</summary>

<img src="app/static/images/docs/grocery-list.png" width=900px>

* Empty state for Grocery List page for weeks without meals

<img src="app/static/images/docs/grocery-list-empty-state.png" width=900px>

</details>

* Frontend functionality
    * Cookfolio automatically generates grocery list based on weekly meal plans that helps users turn planned meals into a practical shopping list. Features include weekly grocery list generation, checkbox interaction and weekly navigation., view grocery list by recipe categories, see helpful empty stated if no meals are planned.

* Backend functionality
    * The grocery list is generated dynamically from meal plan and recipe data stored in the database. The backend handles finding selected date or week, retrieving meal plans, collecting ingredients from linked recipes, preventing other userd from seeing private meal data, showing empty states.

* Technical Reasoning
    * Automated grocery generation improves practicality and provides real-world usefulness for meal planning users.

### Error pages

<details><summary>Screenshots</summary>

* 404 - Error Page

<img src="app/static/images/docs/404-page.png" width=900px>

* 403 - Access Denied

<img src="app/static/images/docs/403-page.png" width=900px>

* 500 - Internal Server Error

<img src="app/static/images/docs/500-page.png" width=900px>
</details>

* Frontend functionality
    * Custom error pages improve user expirience when problems occur. Cookfolio include 404, 403 and 500 pages. Users receive clear messages explaining the problem and helpful navigation options.

* Backend functionality
    * Custom Flask error handlers manage application exceptions and invalid routes. The backend detects invalid routes, forbidden access or missing resources and render the correct custom template. Error pages prevent exposure of sensitive debugging information in production.

* Technical Reasoning
    * Custom error handling imrpoves user guidance, security, website consistency and navigation recovery and prevents confusing user experience.

### Support Messages

<details><summary>Screenshots</summary>

<img src="app/static/images/docs/contact-form.png"> <img src="app/static/images/docs/confirmation-email.png">
</details>

* Frontend functionality
    * Cookfolio includes a support message feature that allows users to contact the site owner or admin through the application. Users can open contact form, enter details, write support message, submit question , feedback or problems, receive a flash messages after submission.

* Backend functionality
    * Support messages are handles using Flask routes, forms, models and database storage. The backend handles receiving submitted support form, validating fields, saving messages to database, showing flash messages, allowing admin user to review messages.

* Technical Reasoning
    * The support message feature was added to improve communication between users and site owner(admin), trust, feedback collection, admin functionality. 

### Admin Dashboard

<details><summary>Screenshots</summary>

* Admin dashboard

<img src="app/static/images/docs/admin-dashboard.png" width=900px>
<img src="app/static/images/docs/admin-support-messages.png" width=900px>
<img src="app/static/images/docs/admin-view-message.png" width=900px>

* Admin email notification for receiving new message from user

<img src="app/static/images/docs/message-received.png">
</details>

* Frontend functionality
    * Cookfolio include admin dashboard to give authorised admin user a central place to monitor and manage application activity. The admin dashboard display user`s support messages.

* Backend functionality
    * The backend manages to check whether the current user is logged in, and has amin permissions, retrieve submitted support messages and pass admin-only data to the template.

* Technical Reasoning
    * The dashboard is showing role based access control. it imporves application management, site owner control, support messages review.

### Form Data Persistence and User-Friendly Editing

* Cookfolio is design to prevent data loss and improve usability by preserving user-entered information throughout the application. When validation errors occur, previously entered data is retained, allowing users to correct mistakes without re-entering information. This functionality is implementet across recipe create form, recipe edit form, meal plan create form, meal plan edit form, authentication forms, search forms and support messages. Search queries remain visible after submission, allowing users to refine searches without typing keywords. During recipe and meal plan editing, existing information is automatically pre-populated into form, enabling users to update only the fields they wish to change while preserving all other data, including uploaded images. Selected dates, meal categories and recipe selections are maintained during meal planning workflows, providing a smoother and more efficient planning experience. This approach reduces user frustraition, improves accessibility, and support intuitive user experience across devices.

### Responsive Design

* Cookfolio is designed for mobile, tablet and desktop devices. Responsive layout are built uing custom CSS, CSS grid, Flexbox and media queries. Cookfolio uses responsive images, mobile-first styling, reusable Jinja templates, collapsable navigation menu. On mobile devices content is stacked vertically to improve readability and touch usability. On larger screens grid layouts are used to display more content side-by-side. A mobile-first approach is useful because cooking applications are often used on phones. Responsive design improves accessibility, mobile usability, readability, navigation and visual consistency.

### Security

* Cookfolio includes security-focused functionality. Users receive feedback when login details are correct, protected page required login, form missing or invalid information, password reset link is invalid or expired. Secure measures include user authentication, password hashing, protected routes, environment variables, gitignore protection, user ownership, and disabled DEBUG mode in production. Security is important because Cookfolio stores user-specific data such as recipes, meal plans, grocery lists, and account information. Users can trust that their account and personal content are handled more safely.

[Back to top](#table-of-content)

## Security Features

Cookfolio includes multiple security features to help protect user data, manage authentication securely and improve overall application safety.

### User Authentication

- Flask-Login is used to manage user authentication and sessions.
- Users are required to log in to access protected pages and features.
- Logged in users are redirected away from login and registration pages where appropriate.

### Password Security

- User passwords are securely hashed before being stored in the database.
- Plain text passwords are never stored.
- Password reset functionality includes secure token generation and validation.
- Password reset tokens are time-limited.
- Reset links are designed for single-use functionality.
- User cannnot reuse their previous password during password reset.

### Route Protection

- Protected routes restrict unauthorised access to private pages.
- Admin-only routes are restricted to administrator accounts.
- User can only edit or delete their own recipes and meal plans.

### Form Validation

Cookfolio uses manual server-side validation to validate user input before data is processed or stored in the database. Validation checks include required fields, title lenght, numeric validation for servings and preparation time, category validation and etc. User feedback through flash messages.

### Environment Variables 

Sensitive configuration data is stored using enviroment variables including secret keys, email credentials, database URLs, API keys, Admin details. This prevent sensitive information from being exposed in the source code.

### Production Security

- DEBUG mode is disabled in production.
- PostgreSQL is used for the deployed production database.
- Gunicorn is used as the production WSGI server on Heroku.

### Session and Access Management

- User session are managed securely through Flask session handling
- Authentication checks are used to prevent unauthorised page access.
- Flash messages provide secure and clear feedback during authentication and form actions.


### Sensitive File Protection

The project uses a ".gitignore" file to prevent sensitive files, unnecessary dependencies and system files from being committed to GitHub. Ignore files include:

- virtual enviroments
- environment variable files
- Python cache files
- IDE configuration files
- Playwright screenshots and test results
- upladed media files
- node modules

This helps protect sensitive information such as secret keys, email credentials, API keys, database configuration.

[Back to top](#table-of-content)

## Future Enhancements

* Favourite recipe and recent viewed recipe functionality.

* Nutritional information and calorie tracking for recipes and meal plans.

* Grocery list merge items and export PDF download file.

* Sharing recipes with other users.

* Recipe rating and review and commenting.

* User profile customization.

* Drag and drop meal planner functionality.

* Recipe image gallery.

* Cooking mode - step by step instruction sliders for mobile devices.

* Admin and User analytics dashboard.

* Enchanced form security and CSFR protection improvements.

[Back to top](#table-of-content)

## Testing

Please refer to [**here**](TESTING.md) for more information on testing Cookfolio.

[Back to top](#table-of-content)

## Deployment

### Forking the Repository

1. NAvigate to the GitHub repository.
2. Click the **Fork** button in the top-right corner.
3. Select your GitHub account.
4. GitHub will create a copy of the repository in your account.

<details><summary>Screenshot</summary>

<img src="app/static/images/docs/fork-repository.png">

</details>

---

### Cloning the Repository

You can clone the repository to use locally by following these steps:

1. Navigate to the GitHub Repository.
2. Click the **Code** button near the top of the repository page.
3. Ensure the **HTTPS** option is selected.
4. Copy the repository link to the clipboard.
5. Open your IDE of choice (git must be installed for the next steps)
6. Type git clone copied-git-url into the IDE terminal
7. Press 'enter' to create the clone
8. Navigate into the project directory.

The project will now be cloned locally for you to use.

<details><summary>Screenshot</summary>

<img src="app/static/images/docs/clone-repository.png">

</details>

---

### Local Development

#### Create Virtual Environment 

* A virtual environment was used to isolate project dependencies and keep the development environment organised. Create a virtual environment using: 

```bash
python -m venv .venv 
```

This creates a local virtual environment folder named .venv .

#### Activate the Virtual Enviroment

* A virtual environment must be activated before installing dependencies or running the application

```bash
.venv\Scripts\activate
```

Once activated, the terminal will display the virtual environment name.

<details><summary>Screenshot</summary>

<img src="app/static/images/docs/active-venv.png">

</details>

#### Install Dependencies

* Install all required project dependencies using:

```bash
python -m pip install -r requirements.txt
```

This install all packages listed in the requirements.txt file

#### Generate Requirements file

* Project dependencies were stored in a requirements.txt file using:

```bash
python -m pip freeze > requirements.txt
```

This ensures the same dependencies can be installed in both local and production environments.

#### Environment Variables

* Create a .env file in the root directory. The .env file is included in .gitignore and must not be committed to GitHub.

```bash
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite://....
API_SECRET_KEY=api_secret_key
```

#### SQLite Local Database

* SQLite is used during local development because it is lightweight and easy to configure for development environments. The local SQLite database file is stored inside the "instance/" folder.

```text
instance/project.db
```

#### Database Setup

* Apply database migrations using:

```bash
python -m flask db migrate -m "message"
python -m flask db upgrade
```
* This creates the required database tables locally.

#### Run the Application

```bash
python run.py
```

The app will run at 

```bash 
http://127.0.0.1:5000
```

#### Deactivate the Virtual Environment

* To exit the virtual environment, run

```bash
deactivate
```
---

### Heroku Production Deployment

#### Create Heroku App

1. Create Heroku account.
2. Log in to Heroku.
3. Create a new app.
4. Choose a unique app name.

#### Setup PostgreSQL for production Database

1. Open the Heroku app dashboard.
2. Go to **Resources**.
3. Search for **Heroku Postgres**.
4. Add the PostgreSQL database.

* After setup Heroku automatically generates the DATABASE_URL config variable.

#### Configure Heroku Config Vars

Environment variables were configures in Heroku to ensure securely store sensitive credentials and production settings.

Using Heroku Dashboard:

1. Go to **Settings/Config Vars**
2. Add them.

or Using the Heroku CLI Terminal:

```bash
heroku config:set SECRET_KEY=your_secret_key -a cookfolio
```
To view existing Heroku Config Vars

```bash
heroku config -a cookfolio
```

#### Deployment Files

- Ensure the project contains the required files
    - requirements.txt
    - Procfile - tells Heroku how to run the application: web:gunicorn run.app
    - .gitignore

#### Connect GitHub Repository to Heroku

1. Open the Heroku app dashboard
2. Go to **Deploy** tab.
3. Choose **GitHub** as the deployment method.
4. Search for the Cookfolio repository.
5. Click **Connect**.

#### Deploy the application

* After connecting the repository

1. Select correct branch.
2. Click **Deploy Branch**.

Automatic deploys can also be enabled so app redeploys each push to GitHub.

#### Run the production Database Migration

* After deployment run migration on the Heroku PostgreSQL database:

```bash
heroku run flask db upgarde -a cookfolio
```
* Open the deployed app from the Heroku dashboard.

<details><summary>Screenshot</summary>

<img src="app/static/images/docs/heroku-deployment.png">

</details>

#### Deployment Workflow

* The following workflow is used when deploying database changes: 

```bash
python -m flask db migrate -m "migration message"
python -m flask db upgrade
git add . 
git commit -m "migration message"
git push
heroku run flask db upgrade -a cookfolio
```

[Back to top](#table-of-content)

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). It allows users to use, modify, distribute and share the project while providng attribution to the author. Additional information about the license can be found in the [License](./LICENSE) file included within the project repository.

[Back to top](#table-of-content)

## Credits

### Content

+ [API images](https://www.themealdb.com/) 
    + recipe data and recipe images are provided through TheMealDB and Spoonacular API integrations.
+ [Favicon.io](https://favicon.io/)
    + used to create the site Favicon and provided the code in the head of all pages.
+ [Font Awesome](https://fontawesome.com/)
    + used to add icons to the project and provided the stylesheet link in the head of all pages.
+ [Google Fonts](https://fonts.google.com/)
    + used to get the links to the fonts that are in the head of the html pages.
+ [ChatGPT Tool](https://chatgpt.com/)
    + Used to create and download logo and images used throught the website.

### Code

+ [Flask](https://flask.palletsprojects.com/en/stable/)
    + Flask official documentation for application structure, routing, configuration, autetication guidance.
+ [SQLAlchemy](https://www.sqlalchemy.org/)
    + SQLAlchemy documentation for database models, relationships and ORM implementation.
+ [Flask-Login](https://flask.palletsprojects.com/en/stable/logging/)
    + Flask-Login documentation for autentication and session management.
+ [Flask-WTF](https://flask.palletsprojects.com/en/stable/patterns/wtforms/)
    + Flask-WTF documentation for form handling and validation.
+ [Flask-Mail](https://flask-mail.readthedocs.io/en/latest/)
    + Flask-Mail documentation for password reset email functionality.
+ [Playwright](https://playwright.dev/)
    + Playwright documentation for automated device testing.
+ [Pytest](https://docs.pytest.org/en/stable/)
    + Pytest documentation for automated back-end testing.
+ [Heroku](https://www.heroku.com/) 
    + Heroku documentation for deployment configuration and PostgreSQL integration.

### Tutorials

+ [Code Institute](https://learn.codeinstitute.net/login?next=/dashboard)
    + used for learning materials, walkthrough projects and course content and requirements.
+ [MDN Web Docs](https://developer.mozilla.org/en-US/)
    + used for help resource for developers, by developers.
+ [W3School](https://www.w3schools.com/)
    + used for HTML, CSS, JS, Python syntax and tutorials.
+ [ChatGPT](https://chatgpt.com/)
    + used as learning tool and debbuging guidance.

[Back to top](#table-of-content)

## Acknowledgements

This project is for educational purpose and was completed as a Portfolio 3 Project for the Full Stack Software Developer Diploma at the Code Institute. I would like to thank 

* My mentor Miguel Orteg Legorreta for his guidance, support and suggestions during the project. Also understanding, guidance and feedbacks throughout the project.
* The whole team at [Code Institute](https://codeinstitute.net/) for their teaching and support.

[Back to top](#table-of-content)