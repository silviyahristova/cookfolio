# Cookfolio

<!--add responsive mock-up image-->

#### **By Silviya Hristova**

<!--add link-->

Cookfolio is a recipe management website that allows users to create, edit and organize their own recipes, plan weekly meals and discover new recipes. The application is designed to help users manage their cooking and meal planning in a simple and intuitive way.

This is the documentation for Cookfolio, a full-stack web application. It has been built using HTML5, CSS3, JavaScript, Python, Flask and a relational database. It has been developed for educational purposes as par of Code Institute Level 5 Diploma in Web Application Development.

---

## Table of content

- [**About**](#about)
- [**User Experiences**](#user-experiences)
    - [**User Stories**](#user-stories)
    - [**Strategy**](#strategy)
    - [**Scope**](#scope)
    - [**Structure**](#structure)
    - [**Skeleton**](#skeleton)
    - [**Surface**](#surface)
- [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Tools**](#tools)
- [**Features**](#features)
- [**Functionality**](#functionality)
- [**Future improvemens**](#future-improvements)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**License**](#license)
- [**Credits**](#credits)
- [**Acknowledgements**](#acknowledgements)


## About

Cookfolio is a personal recipe management website designed to help users store, organise and manage their own recipes in one location. The website allows visitors to create an account, add new recipes, upload images, categorise content and edit or delete their recipes.

The website focuses on simplicity, usability and accessibility, using a mobile-first design approach to ensure a consistent experience across different devices. Secure authentication and user ownership controls are implemented to ensure that users can only access and manage their own content.

Cookfolio is developed as part of Code Institute Level 5 Diploma in Web Application Develoment and demostrate full CRUD functionality, relational database design, and server-side logic using Python and Flask.

<!--add link-->

## User Experiences

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
- As an admin, I want to view all registered users.
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
- Prrduce clear planning documentation, wireframes, page-flow diagrams and database schema design.
- Maintain a clean codebase using version control and regular commits.

### **Scope**

The Cookfolio website is designed to allow users to manage their personal recipes, organize cooking content, and plan meals efficiently. The site includes core features that allows users to create and manage recipes, while also providing additional tools such as recipe discovery and meal planning to enhance the overal user experience.

#### **Core features**

The following core features are implemented in the Cookfolio application:

- User Authentication - user can create an account, log in, and log out anytime.

- Recipe Management (CRUD functionality) - users can create, view, edit and delete recipes. Each recipe contains details such as title, ingredients, instructions, preparation time, servings and category.

- Recipe Category - Recipes can be organised into categories such as breakfast, lunch, dinner or desserts to make browsing esier.

- Recipe Image Upload - users can upload images for their recipes, allowing each recipe to include a visual representation of the dish.

- Recipe Search and Filtering - users can search for recipes by title or category to find quickly recipes they need.

#### **Additional features**

To enhance the user experience, the following additional features are implemented in Cookfolio website:

- Meal Planner - users can assign recipes to specific days of the week, allowing them to plan meals in advance.

- Recipe Discovery - users can explore new recipes using an external recipe API, allowing them to discover new dishesh and ideas.

- Grocery List - Ingredients from planned recipes can be used to generate a grocery list to assist the users with shopping.

- Support Page - users can send support messages through a contact form f they encounter issues or have questions about the application.

- Analytics Dashboard - the dashboard provides insights such as the number of recipes created and etc.

#### **Error Handling**

The website includes custom error pages to improve the user experience:

- 403 Access Denied Page - displayed when a user attempts to access a restricted resource.

- 404 Page Not Found - displayed when a user navigates to a page that does not exist.

- 500 Server Error - displayed when an unexpected server error occurs.


### **Structure**

The structure of Cookfolio is designed to provide a clear and logical flow based on the user`s authentication state. The website separates public pages from authenticated user features, allowing visitors to explore the website before creating an account, while providing registered users with access to advances features such as recipe management and meal planning. 

Unathenticated users can access the Home page, where the purpose of the site is explained, and are guided toward the Login and Registration pages. These pages provide a simple and focused authentication flow without distractions.

Once authenticated, users are redirected to the Dashboard, which acts as the main hub of the website. From the dashboard, users can view all of their recipes and access core actions such as adding, editing, or deleting recipes. The dashboard layout ensures that content management actions are easy to locate and perform.

Form-based pages such as Add Recipe, Edit Recipe, and Support follow a consistent layout. This helps users recognise familiar patterns and easy interacting with the website.

Navigation is handled through a navigation bar and a mobile-friendly hamburger menu, providing access to key areas such as dashboard, support page, log out. Logging out ends the user session and redirects the user back to the Home page.

The overall structure supports a predictable and intuitive user journey, ensuring that users can move through the website efficiently. 

A custom 403, 404 and 500 error pages are implemented to handle errors. The pages provide clear feedback to users and offers navigation back to the Home or Dashboard page, ensuring smooth and controlled user experience.

### **Skeleton**

Low-fidelity wireframes were created during the planning stage to define the skeletal structure of the website before development began. These wireframes focus on layout, content hierarchy and user flow rather visual design or styling.

Wireframes were created using Figma to plan the structure of each page. These wireframes helped ensure that the interface is organised logically and that users could easily navigate between different features of the application. They were designed using a mobile-friendly approach, ensuring that the website would be responsive and function effectively across mobile, tablet and desktop devices. Wireframes were created for mobile and desktop layout for the main pages of the website, including Home page, Login page, Register page, User Dashboard, Empty user Dashboard, My recipe page, Recipe detail page, Add recipe page, Edit recipe page, Delete page, Meal planning page, Discover recipes page, Support page, Search result page, Error pages 403, 404 and 500.

<details><summary>Desktop</summary>

<img src="static/images/docs/wireframes/home-page-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/register-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/login-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/empty-dashboard-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/dashboard-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/my-recipes-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/recipe-detail-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/add-recipe-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/edit-recipe-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/delete-recipe-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/meal-planner-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/discover-recipe-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/search-results-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/support-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/403-page-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/404-page-desktop.webp" width=250px>
<img src="static/images/docs/wireframes/500-page-desktop.webp" width=250px>

</details>

<details><summary>Mobile</summary>

<img src="static/images/docs/wireframes/home-page-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/register-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/login-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/empty-dashboard-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/dashboard-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/my-recipes-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/recipe-detail-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/add-recipe-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/edit-recipe-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/delete-recipe-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/meal-planner-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/discover-recipe-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/search-results-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/support-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/403-page-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/404-page-mobile.webp" width=250px>
<img src="static/images/docs/wireframes/500-page-mobile.webp" width=250px>

</details>

### **Surface**

**Colour**

The color palette for Cookfolio was selected to create a warm, inviting,and food-insired visual dentity. The colors were choosen to be associated with cooking, freshness and appetite while maintaining good readability and accessibility across devices. The palette combines warm and natural tones associated with food, ingredients and kitchen environments. Red colour is strongly associated with food and appetite. It is commonly used in food branding because it attracts attention and simulates hunger. In Cookfolio red is used for primary buttons and important actions such as adding and saving recipes. Green colour represents freshness, vegetables and healthy ingredients. It helps balance the strong red tone. The colour is used for confirmation actions and success messages. A light grey background colour was selected to create a clean and neutral interface that allows recipe and images to stand out without overwhelming the user. Dark grey used for body text to maintain strong readability. White colour is used to provide contrast and maintain a clean layout. The selected colours were choosen with accessibility in mind. The palette were created using the site [Color-hex.com](https://www.color-hex.com/). Tints and Shades of these colours will be used also and are created using the site [Maketintsandshade.com](https://maketintsandshades.com/).

![Colour Pallette](static/images/docs/cookfolio-colorpalette.webp)

<details><summary>Tints and shades</summary>

![Tints and shades](static/images/docs/cookfolio-tintandshades.webp)

</details>

**Typography**

The fonts that will be used in the website will be imported from [Google Fonts](https://fonts.google.com) and will be used [Poppins](https://fonts.google.com/specimen/Poppins) and [Open Sans](https://fonts.google.com/specimen/Open+Sans). They were choosen to ensure readability, visual balance and friendly interface, that reflects the theme of cooking. This is combination of modern sans-serif fonts that provide clarity and welcoming. Poppins was selected for headings and important interface elements. The font provides strong visual hierarchy, making it easy for users to identify page titles, section headings and important actions within the interface. Open Sans is used for body text because it is highly readable across different devices. The clean design ensures that longer section of the text, such as recipe instructions adn ingredient lists remain comfortableto read. Headings are used to structure content and important section, while body text will provide detailed information in a readable format.

**Logo**

The Cookfolio logo is created using [ChatGPT](https://chatgpt.com) logo design tool. It represent the concept of the digital cookbook where users can organise and manage their personal recipes. The design combines visual elemenents related to cooking and food preparation, helping users immediately understand the purpose of the application. The visual style of the logo is friendly and welcoming, simple and modern. The colours used in the logo follow the same colour palette used throughout the Cookfolio interface. This consistency help to strenghten the brand identity of the website. The logo is used primarily in the navigation bar, where it also functions ad a clickable element that allows users to return to the home page.

**Images**

Images are important in the Cookfolio website. They making the interface more engaging and visually appealing. Food-related images help users connect with recipes. The images used in the website support the theme of cooking and meal preparation while helping users better understand the content presented on each page. Users are able to upload images for their recipes. These images help users quickly identify recipes and make browsing more easier. Recipe images also help create a more realistic digital cookbook experience where user can visually explore meals before deciding what to cook. All images used across the website include similar style, colour theme and layout placement across different pages. 

**Icons**

Icons are used across the website to improve usability and provide clear visual interface for users. Icons help users quickly identify actions and features without needing to read detailed instruction, which improves the user experience. The icons were sources from [Font Awesome](https://fontawesome.com/) website. 

[Back to top](#table-of-content)

## Technologies Used


### **Languages**


### **Tools**

[Back to top](#table-of-content)

## Features

[Back to top](#table-of-content)

## Future features

[Back to top](#table-of-content)

## Testing

Please refer to [**here**](TESTING.md) for more information on testing Cookfolio.

[Back to top](#table-of-content)

## Deployment

[Back to top](#table-of-content)

## License

[Back to top](#table-of-content)

## Credits

[Back to top](#table-of-content)

## Acknowledgements

[Back to top](#table-of-content)