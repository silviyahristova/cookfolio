import os
from unicodedata import category
from flask import Blueprint, app , render_template, request, flash, redirect, url_for, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from flask import current_app
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Recipe, Category, SupportMessage, MealPlan
from . import db
import re, requests
from functools import wraps
from sqlalchemy import join, or_
from math import ceil
from datetime import datetime, date, timedelta
from collections import defaultdict

main = Blueprint('main', __name__)

# Allowed file extensions for recipe images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Admin protection decorator
def admin_required(view_function):
    @wraps(view_function)
    def wrapped_view_function(*args, **kwargs):
        if not current_user.is_authenticated:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('main.login'))
        if not current_user.is_admin:
            flash('You do not have permission to access this page.', 'error')
            abort(403)
        return view_function(*args, **kwargs)
    return wrapped_view_function

#admin dashboard route
@main.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
        
    return render_template('admin_dashboard.html')

#admin support messages route
@main.route('/admin/support-messages')
@login_required
@admin_required
def admin_view_support_messages():
    page = request.args.get('page', 1, type=int)

    support_messages = SupportMessage.query.order_by(SupportMessage.created_at.desc()).paginate(page=page, per_page=5, error_out=False)

    return render_template('admin_support_messages.html', support_messages=support_messages)

#admin view support message details route
@main.route('/admin/support-messages/<int:message_id>')
@login_required
@admin_required
def admin_view_support_message_details(message_id):
    support_message = db.session.get(SupportMessage, message_id)

    if not support_message:
        flash('Support message not found.', 'error')
        return redirect(url_for('main.admin_view_support_messages'))
    
    return render_template('admin_support_message_details.html', support_message=support_message)

#admin delete support message route
@main.route('/admin/support-messages/<int:message_id>/delete', methods=['POST'])
@login_required
@admin_required
def admin_delete_support_message(message_id):
    support_message = db.session.get(SupportMessage, message_id)
    if not support_message:
        flash('Support message not found.', 'error')
        return redirect(url_for('main.admin_view_support_messages'))
    
    db.session.delete(support_message)
    db.session.commit()

    flash('Support message deleted successfully!', 'success')
    return redirect(url_for('main.admin_view_support_messages'))

#main home route
@main.route('/')
def home():
    return render_template('index.html')

#register route
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle form submission
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        # Validation
        if not username or not email or not password or not confirm_password:
            flash('All fields are required.', 'error')
            return redirect(url_for('main.register'))
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return redirect(url_for('main.register'))
        
        #Username, email and password validation
        if len(username) < 3 or len(username) > 20:
            flash('Username must be between 3 and 20 characters.', 'error')
            return redirect(url_for('main.register'))
        if not username.isalnum():
            flash('Username can only contain letters and numbers.', 'error')
            return redirect(url_for('main.register'))
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('main.register'))
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'error')
            return redirect(url_for('main.register'))
        if not any(char.isdigit() for char in password):
            flash('Password must contain at least one number.', 'error')
            return redirect(url_for('main.register'))
        if not any(char.isalpha() for char in password):
            flash('Password must contain at least one letter.', 'error')
            return redirect(url_for('main.register'))
        
        #Check if user already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists.', 'error')
            return redirect(url_for('main.register'))
        
        # Hash the password before storing it
        hashed_password = generate_password_hash(password)
        
        # Create a new user and add to the database
        new_user = User(username=username, email=email, password=hashed_password)
        #Save user to database
        db.session.add(new_user)
        db.session.commit()

        # Provide feedback to the user
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

#login route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        #check if both fields are filled
        if not username or not password:
            flash('Both fields are required.', 'error')
            return redirect(url_for('main.login'))
        
        # Check if user exists and password is correct
        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password.', 'error')
            return redirect(url_for('main.login'))

        # Login user using flask-login
        login_user(user)
        flash('Logged in successfully.', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('login.html')

#logout route
@main.route('/logout')
@login_required
def logout():
    # Logout user using flask-login
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.login'))

#Recipe routes
# Add recipe route with GET and POST methods
@main.route('/add-recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    # If GET request, show the add recipe form with category options by orders
    if request.method == 'GET':
        categories = Category.query.order_by(Category.order).all()
        return render_template('recipe_form.html', form_type='add', categories=categories)

    # If POST request, process the form submission
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category_id = request.form.get('category_id')
        ingredients = request.form.get('ingredients', '').strip()
        instructions = request.form.get('instructions', '').strip()
        prep_time = request.form.get('prep_time', '').strip()
        servings = request.form.get('servings', '').strip()

        photo = request.files.get('photo')

        categories = Category.query.order_by(Category.order).all()

        # Validate form data
        if not title or not category_id or not ingredients or not instructions or not prep_time or not servings :
            flash('Please fill in all required fields.', 'error')
            return render_template('recipe_form.html', form_type='add', categories=categories, form_data=request.form)
        
        if len(title) < 3 or len(title) > 100:
            flash('Title must be between 3 and 100 characters long.', 'error')
            return render_template('recipe_form.html', form_type='add', categories=categories, form_data=request.form)
        
        try:
            prep_time = int(prep_time)
            servings = int(servings)
        except ValueError:
            flash('Prep time and servings must be valid numbers.', 'error')
            return render_template('recipe_form.html', form_type='add', categories=categories, form_data=request.form)
        
        if prep_time < 1 or prep_time > 1440:
            flash('Prep time must be between 1 and 1440 minutes.', 'error')
            return render_template('recipe_form.html', form_type='add', categories=categories, form_data=request.form)
        
        if servings < 1 or servings > 100:
            flash('Servings must be between 1 and 100.', 'error')
            return render_template('recipe_form.html', form_type='add', categories=categories, form_data=request.form)
        
        # Handle file upload
        image_filename = None
        if photo and photo.filename:
            if allowed_file(photo.filename):
                filename = f"{current_user.id}_{secure_filename(photo.filename)}"
                upload_folder = current_app.config['UPLOAD_FOLDER']
                os.makedirs(upload_folder, exist_ok=True)
                photo_path = os.path.join(upload_folder, filename)
                photo.save(photo_path)

                image_filename = filename
            else:
                flash('Invalid file type. Allowed types are png, jpg, jpeg, webp.', 'error')
                return render_template('recipe_form.html', form_type='add', categories=categories, form_data=request.form)

        # Create a new recipe and add to the database
        new_recipe = Recipe(
            title=title,
            category_id=int(category_id),
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time,
            servings=servings,
            image_filename=image_filename,
            user_id=current_user.id
        )

        # Save recipe to database
        db.session.add(new_recipe)
        db.session.commit()

        flash('Recipe added successfully!', 'success')
        return redirect(url_for('main.view_recipe', recipe_id=new_recipe.id))

    return render_template('recipe_form.html', form_type='add', categories=categories)

# Dashboard route to show user's recipes and categories with counts
@main.route('/dashboard')
@login_required
def dashboard():

    # Fetch the user's recipes ordered by creation date (newest first)
    recipes = Recipe.query.filter_by(user_id=current_user.id).order_by(Recipe.created_at.desc()).all()
   
    #Fetch categories in meal order
    categories = Category.query.order_by(Category.order).all()

    #each category has a image file
    category_images = {
        'Breakfast': 'breakfast-category',
        'Lunch': 'lunch-category',
        'Dinner': 'dinner-category',
        'Dessert/Snack': 'dessert-category'
    }

    #count recipe in each category for the user
    category_counts = {}
    for category in categories:
        count = Recipe.query.filter_by(user_id=current_user.id, category_id=category.id).count()
        category_counts[category.id] = count

    # Get meal plans for the current week
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    # Join MealPlan with Recipe to get recipe details in the same query and order by meal date and meal type
    meal_plans = MealPlan.query.filter(MealPlan.user_id == current_user.id, MealPlan.meal_date >= week_start, MealPlan.meal_date <= week_end).join(Recipe).order_by(MealPlan.meal_date.asc()).all()

    # show today,tomorrow and day after tommorw on dashboard
    preview_days = []

    for i in range(3):
        preview_date = today + timedelta(days=i)

        day_meals = [meal_plan for meal_plan in meal_plans if meal_plan.meal_date == preview_date]
        preview_days.append({"date": preview_date, "meals": day_meals})

    return render_template('dashboard.html', recipes=recipes, categories=categories, category_counts=category_counts, category_images=category_images, meal_plans=meal_plans, preview_days=preview_days, today=today, timedelta=timedelta)

# View recipe details route
@main.route('/recipes/<int:recipe_id>')
@login_required
def view_recipe(recipe_id):
    recipe = db.session.get(Recipe, recipe_id)
    is_imported_recipe = recipe.image_url is not None
    if not recipe:
        flash('Recipe not found.', 'error')
        return redirect(url_for('main.dashboard'))

    if recipe.user_id != current_user.id:
        flash('You do not have permission to view this recipe.', 'error')
        return redirect(url_for('main.dashboard'))
    
    return render_template('view_recipe.html', recipe=recipe, is_api_recipe=False, is_imported_recipe=is_imported_recipe)

# Edit recipe route with GET and POST methods
@main.route('/recipes/<int:recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = db.session.get(Recipe, recipe_id)
    if not recipe:
        flash('Recipe not found.', 'error')
        return redirect(url_for('main.dashboard'))
    
    categories = Category.query.order_by(Category.order).all()

    if recipe.user_id != current_user.id:
        flash('You do not have permission to edit this recipe.', 'error')
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category_id = request.form.get('category_id', '').strip()
        ingredients = request.form.get('ingredients', '').strip()
        instructions = request.form.get('instructions', '').strip()
        prep_time = request.form.get('prep_time', '').strip()
        servings = request.form.get('servings', '').strip()

        photo = request.files.get('photo')
        
        # Validate form data
        if not title or not category_id or not ingredients or not instructions or not prep_time or not servings :
            flash('Please fill in all required fields.', 'error')
            return render_template('recipe_form.html', form_type='edit', recipe=recipe, categories=categories, form_data=request.form)
        
        if len(title) < 3 or len(title) > 100:
            flash('Title must be between 3 and 100 characters long.', 'error')
            return render_template('recipe_form.html', form_type='edit', recipe=recipe, categories=categories, form_data=request.form)
        
        try:
            prep_time = int(prep_time)
            servings = int(servings)
        except ValueError:
            flash('Prep time and servings must be valid numbers.', 'error')
            return render_template('recipe_form.html', form_type='edit', recipe=recipe, categories=categories, form_data=request.form)
        
        if prep_time < 1 or prep_time > 1440:
            flash('Prep time must be between 1 and 1440 minutes.', 'error')
            return render_template('recipe_form.html', form_type='edit', recipe=recipe, categories=categories, form_data=request.form)
        
        if servings < 1 or servings > 100:
            flash('Servings must be between 1 and 100.', 'error')
            return render_template('recipe_form.html', form_type='edit', recipe=recipe, categories=categories, form_data=request.form)
        
        # Update recipe details
        recipe.title = title
        recipe.category_id = int(category_id)
        recipe.ingredients = ingredients
        recipe.instructions = instructions
        recipe.prep_time = int(prep_time)
        recipe.servings = int(servings)

        # Handle file upload
        if photo and photo.filename:
            if allowed_file(photo.filename):
                # Delete old image file if it exists
                if recipe.image_filename:
                    upload_folder = current_app.config['UPLOAD_FOLDER']
                    old_image_path = os.path.join(upload_folder, recipe.image_filename)
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)

                filename = f"{current_user.id}_{secure_filename(photo.filename)}"
                upload_folder = current_app.config['UPLOAD_FOLDER']
                os.makedirs(upload_folder, exist_ok=True)
                photo_path = os.path.join(upload_folder, filename)
                photo.save(photo_path)

                recipe.image_filename = filename
            else:
                flash('Invalid file type. Allowed types are png, jpg, jpeg, webp.', 'error')
                return render_template('recipe_form.html', form_type='edit', recipe=recipe, categories=categories, form_data=request.form)

        db.session.commit() 

        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('main.view_recipe', recipe_id=recipe_id))
    
    return render_template('recipe_form.html', form_type='edit', recipe=recipe, categories=categories)

# Delete recipe route
@main.route('/recipes/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = db.session.get(Recipe, recipe_id)
    if not recipe:
        flash('Recipe not found.', 'error')
        return redirect(url_for('main.dashboard'))

    if recipe.user_id != current_user.id:
        flash('You do not have permission to delete this recipe.', 'error')
        return redirect(url_for('main.dashboard'))

    # Delete image file if it exists
    if recipe.image_filename:
        upload_folder = current_app.config['UPLOAD_FOLDER']
        image_path = os.path.join(upload_folder, recipe.image_filename)
        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(recipe)
    db.session.commit()

    flash('Recipe deleted successfully!', 'success')
    return redirect(url_for('main.my_recipes'))

# My recipes route with category filter, search and pagination
@main.route('/my-recipes')
@login_required
def my_recipes():

    category_id = request.args.get('category_id', type=int)
    search = request.args.get('search', '').strip()
    page = request.args.get('page', 1, type=int)

    #current_user's recipes query
    query = Recipe.query.filter_by(user_id=current_user.id)

    # Filter by category
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    # Search by title, ingredients or instructions
    if search:
        query = query.filter(
            or_(
                Recipe.title.ilike(f'%{search}%'),
                Recipe.ingredients.ilike(f'%{search}%'),
                Recipe.instructions.ilike(f'%{search}%')
            )
        )
    
    # Newest recipes first, 8 recipes per page
    recipes = query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=8)

    #Fetch categories in meal order for the dropdown menu
    categories = Category.query.order_by(Category.order).all()

    # Get recipe titles for datalist suggestions
    recipe_titles = Recipe.query.with_entities(Recipe.title).filter_by(user_id=current_user.id).order_by(Recipe.title).all()
    
    # Convert list of tuples to list of strings
    recipe_titles = [t[0] for t in recipe_titles]

    return render_template('my_recipes.html', recipes=recipes, categories=categories, selected_category_id=category_id, search=search, recipe_titles=recipe_titles)

# Meal plans routes
@main.route('/meal-plans')
@login_required
def meal_plans():
    week_start_str = request.args.get('week_start')
    today = date.today()

    if week_start_str:
        start_of_week = datetime.strptime(week_start_str, '%Y-%m-%d').date()
    else:
        start_of_week = today - timedelta(days=today.weekday())
    
    end_of_week = start_of_week + timedelta(days=6)

    #paginate weeks
    previous_week = start_of_week - timedelta(days=7)
    next_week = start_of_week + timedelta(days=7)

    #create list with all 7days
    week_days = [(start_of_week + timedelta(days=i)) for i in range(7)]

    meal_plans = MealPlan.query.filter(MealPlan.user_id == current_user.id, MealPlan.meal_date >= start_of_week, MealPlan.meal_date <= end_of_week).join(Recipe).order_by(MealPlan.meal_date, MealPlan.meal_type).all()
    has_recipes = Recipe.query.filter_by(user_id=current_user.id).first() is not None
    has_meal_plans = MealPlan.query.filter_by(user_id=current_user.id).first() is not None 

    #meal category order 
    meal_category_order = {
        'Breakfast': 1,
        'breakfast': 1,
        'Lunch': 2,
        'lunch': 2,
        'Dinner': 3,
        'dinner': 3,
        'Dessert/Snack': 4,
        'dessert/snack': 4
    }

    meal_plans = sorted(meal_plans, key=lambda mp: (mp.meal_date, meal_category_order.get(mp.meal_type, 99)))

    return render_template('meal_plans.html',week_days=week_days, start_of_week=start_of_week, end_of_week=end_of_week, previous_week=previous_week, next_week=next_week, meal_plans=meal_plans, has_recipes=has_recipes, has_meal_plans=has_meal_plans, today=today)

# Add meal plan route with GET and POST methods
@main.route('/meal-plans/add', methods=['GET', 'POST'])
@login_required
def add_meal_plan():
    recipes = Recipe.query.filter_by(user_id=current_user.id).order_by(Recipe.title).all()
    selected_date = request.args.get('meal_date') or date.today()
    selected_meal_type = request.args.get('meal_type')
    selected_recipe_id = request.args.get('recipe_id')

    if not recipes:
        flash('You need to have at least one recipe to add a meal plan. Please add a recipe first.', 'error')
        return redirect(url_for('main.meal_plans'))
    
    if request.method == 'POST':
        recipe_id = request.form.get('recipe_id')
        meal_date = request.form.get('meal_date')
        meal_type = request.form.get('meal_type')
        selected_date = meal_date

        if not recipe_id or not meal_date or not meal_type:
            flash('Please fill in all fields.', 'error')
            return render_template('meal_plan_form.html', recipes=recipes, meal_type=meal_type, selected_date=selected_date, form_data=request.form)

        #convert meal_date string to date object and validate that it's not in the past
        try:
            meal_date = datetime.strptime(meal_date, '%Y-%m-%d').date()
        except ValueError:
            flash('You can only add meal plans for valid dates.', 'error')
            return render_template('meal_plan_form.html', recipes=recipes, meal_type=meal_type, selected_date=selected_date, form_data=request.form)

        #prevent past date meal plans
        if meal_date < date.today():
            flash('You can only add meal plans for today or future dates.', 'error')
            return render_template('meal_plan_form.html', recipes=recipes,meal_type=meal_type, selected_date=selected_date, form_data=request.form)
        
        # prevent duplicates meal category for the same day
        existing_meal_category = MealPlan.query.filter_by(user_id=current_user.id, meal_date=meal_date, meal_type=meal_type).first()

        if existing_meal_category:
            flash(f'You already have a {meal_type} planned for {meal_date.strftime("%d.%m.%Y")}. Please edit it instead.', 'warning')
            return render_template('meal_plan_form.html', recipes=recipes,meal_type=meal_type, selected_date=selected_date, form_data=request.form)

        #prevent same recipe been planned more than once on the same day
        existing_recipe_for_day = MealPlan.query.filter_by(user_id=current_user.id, meal_date=meal_date, recipe_id=int(recipe_id)).first()

        if existing_recipe_for_day:        
            flash(f'You already have this recipe planned for {meal_date.strftime("%d.%m.%Y")}. Please choose a different recipe.', 'warning')   
            return render_template('meal_plan_form.html', recipes=recipes, meal_type=meal_type, selected_date=selected_date, form_data=request.form)

        #create new meal plan and save to database
        new_meal_plan = MealPlan(
            user_id=current_user.id,
            recipe_id=int(recipe_id),
            meal_date=meal_date,
            meal_type=meal_type
        )

        db.session.add(new_meal_plan)
        db.session.commit()

        flash('Meal plan added successfully!', 'success')
        return redirect(url_for('main.view_day_meal_plan', meal_date=meal_date.strftime('%Y-%m-%d')))
    
    return render_template('meal_plan_form.html', recipes=recipes, meal_plan=None, today=date.today(), selected_date=selected_date, selected_meal_type=selected_meal_type, selected_recipe_id=selected_recipe_id, form_data=request.form)

#View meal plan details route
@main.route('/meal-plans/day/<meal_date>')
@login_required
def view_day_meal_plan(meal_date):

    meal_plan = MealPlan.query.filter_by(user_id=current_user.id, meal_date=meal_date).first()
    selected_date = datetime.strptime(meal_date, '%Y-%m-%d').date()
    day_meals = MealPlan.query.filter_by(user_id=current_user.id, meal_date=selected_date).join(Recipe).order_by(MealPlan.meal_type).all()

    if not meal_plan:
        flash('Meal plan not found.', 'error')
        return redirect(url_for('main.meal_plans'))

    if meal_plan.user_id != current_user.id:
        flash('You do not have permission to view this meal plan.', 'error')
        return redirect(url_for('main.meal_plans'))
    
    # Join MealPlan with Recipe to get recipe details in the same query and order by meal type
    day_meals = MealPlan.query.filter_by(user_id=current_user.id, meal_date=selected_date).join(Recipe).order_by(MealPlan.meal_type).all()
    day_meals = sorted(day_meals, key=lambda meal_plan: {'breakfast': 1, 'lunch': 2, 'dinner': 3, 'dessert/snack': 4}.get(meal_plan.meal_type, 99))

    #meal category order for missing categories in the day meal plan
    meal_types = ["breakfast", "lunch", "dinner", "dessert/snack"]

    meals_by_type = {meal.meal_type.lower(): meal for meal in day_meals}

    return render_template('view_day_meal_plan.html', meal_plan=meal_plan, day_meals=day_meals, selected_date=selected_date, meals_by_type=meals_by_type, meal_types=meal_types, today=date.today())

# Edit meal plan route with GET and POST methods
@main.route('/meal-plans/<int:meal_plan_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_meal_plan(meal_plan_id):
    meal_plan = MealPlan.query.get_or_404(meal_plan_id)

    if not meal_plan:
        flash('Meal plan not found.', 'error')
        return redirect(url_for('main.meal_plans'))

    if meal_plan.user_id != current_user.id:
        flash('You do not have permission to edit this meal plan.', 'error')
        return redirect(url_for('main.meal_plans'))

    recipes = Recipe.query.filter_by(user_id=current_user.id).order_by(Recipe.title).all()

    if request.method == 'POST':
        recipe_id = request.form.get('recipe_id')
        meal_type = request.form.get('meal_type')
        meal_date = datetime.strptime(request.form.get('meal_date'), '%Y-%m-%d').date()
        selected_date = meal_plan.meal_date

        # Validate form data
        if not recipe_id or not meal_type or not meal_date:
            flash('Please fill in all fields.', 'error')
            return render_template('meal_plan_form.html', recipes=recipes, meal_plan=meal_plan, today=date.today(), selected_date=selected_date, form_data=request.form)
        
        try:
            meal_date = datetime.strptime(request.form.get('meal_date'), '%Y-%m-%d').date()
        except ValueError:
            flash('You can only set meal plans for valid dates.', 'error')
            return render_template('meal_plan_form.html', recipes=recipes, meal_plan=meal_plan, today=date.today(), selected_date=selected_date, form_data=request.form)
        
        if meal_date < date.today():
            flash('You can only set meal plans for today or future dates.', 'error')
            return render_template('meal_plan_form.html', recipes=recipes, meal_plan=meal_plan, today=date.today(), selected_date=selected_date, form_data=request.form)

        # prevent duplicates meal category for the same day
        existing_meal_category = MealPlan.query.filter_by(user_id=current_user.id, meal_date=meal_date, meal_type=meal_type).first()
        
        if existing_meal_category and existing_meal_category.id != meal_plan_id:
            flash(f'You already have a {meal_type} planned for {meal_date.strftime("%d.%m.%Y")}. Please choose a different meal type or edit the existing one.', 'warning')
            return render_template('meal_plan_form.html', recipes=recipes, meal_plan=meal_plan, today=date.today(), selected_date=selected_date, form_data=request.form)
        
        #prevent same recipe been planned more than once on the same day
        existing_recipe_for_day = MealPlan.query.filter_by(user_id=current_user.id, meal_date=meal_date, recipe_id=int(recipe_id)).first()
        
        if existing_recipe_for_day and existing_recipe_for_day.id != meal_plan_id:
            flash(f'You already have this recipe planned for {meal_date}. Please choose a different recipe.', 'warning')
            return render_template('meal_plan_form.html', recipes=recipes, meal_plan=meal_plan, today=date.today(), selected_date=selected_date, form_data=request.form)
        
        meal_plan.recipe_id = int(recipe_id)
        meal_plan.meal_date = meal_date
        meal_plan.meal_type = meal_type

        db.session.commit()

        flash('Meal plan updated successfully!', 'success')
        return redirect(url_for('main.view_day_meal_plan', meal_date=meal_date.strftime('%Y-%m-%d')))

    return render_template('meal_plan_form.html', recipes=recipes, meal_plan=meal_plan, today=date.today(), selected_date=meal_plan.meal_date, form_data=None)

# Delete meal plan route
@main.route('/meal-plans/<int:meal_plan_id>/delete', methods=['POST'])
@login_required
def delete_meal_plan(meal_plan_id):
    meal_plan = MealPlan.query.get_or_404(meal_plan_id)
    meal_date = meal_plan.meal_date

    if meal_plan.user_id != current_user.id:
        flash('You do not have permission to delete this meal plan.', 'error')
        return redirect(url_for('main.meal_plans'))

    db.session.delete(meal_plan)
    db.session.commit()

    flash('Meal plan deleted successfully!', 'success')
    return redirect(url_for('main.view_day_meal_plan', meal_date=meal_date.strftime('%Y-%m-%d')))

#Helper function to search recipes from TheMealDB and Spoonacular APIs by title, ingredients and instructions
def search_api_recipes(search_query, api_page=1):
    
    api_per_page = 8
    offset = (api_page - 1) * api_per_page
    start = (api_page - 1) * api_per_page
    end = start + api_per_page

    all_recipes = []

    #Search TheMealDB API
    mealdb_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={search_query}"
    mealdb_response = requests.get(mealdb_url, timeout=5)

    if mealdb_response.status_code == 200:
        mealdb_data = mealdb_response.json()
        mealdb_recipes = mealdb_data.get('meals') or []
        for meal in mealdb_recipes:
            recipe = {
                "id": meal.get('idMeal'),
                "title": meal.get('strMeal'),
                "image_url": meal.get('strMealThumb'),
                "category": meal.get('strCategory'),
                "cuisine": meal.get('strArea'),
                "prep_time": 30,
                "servings": 4,
                "api_source": "themealdb"
            }
            all_recipes.append(recipe)

    #Search Spoonacular API
    spoonacular_url = f"https://api.spoonacular.com/recipes/complexSearch?query={search_query}&number={api_per_page}&apiKey={os.getenv('SPOONACULAR_API_KEY')}"
    spoonacular_params = {
        'query': search_query,
        'number': api_per_page,
        'offset': offset,
        'addRecipeInformation': True,
        'apiKey': os.getenv('SPOONACULAR_API_KEY')
    }

    spoonacular_response = requests.get(spoonacular_url, params=spoonacular_params, timeout=5)

    if spoonacular_response.status_code == 200:
        spoonacular_data = spoonacular_response.json()
        spoonacular_recipes = spoonacular_data.get('results') or []
        for recipe in spoonacular_recipes:
            recipe["api_source"] = "spoonacular"
            recipe["source_name"] = recipe.get("sourceName", "Spoonacular")
            recipe["cuisine"] = ",".join(recipe.get("cuisines", [])) or "Spoonacular Recipe"
            recipe["title"] = recipe.get("title", "Untitled Recipe")
            recipe["image_url"] = recipe.get("image", "")
            recipe["category"] = recipe.get("dishTypes", ["Unknown"])[0] if recipe.get("dishTypes") else "Unknown"
            recipe["prep_time"] = recipe.get("readyInMinutes", 30)
            recipe["servings"] = recipe.get("servings", 4)

            all_recipes.append(recipe)

    return all_recipes[start:end], len(all_recipes)

# Search route to search recipe globally- users recipes and API recipes, search by title, ingredients and instructions, show results in a separate page with pagination
@main.route('/search')
@login_required
def search():
    search_query = request.args.get('search', '').strip()
    categories = Category.query.order_by(Category.order).all()
    selected_category = selected_category = request.args.get('category', '').strip()
    page= request.args.get('page', 1, type=int)
    api_page = request.args.get('api_page', 1, type=int)
    api_per_page = 8

    user_recipes = None
    api_recipes = []
    api_total = 0
    api_total_pages = 1

    #Get API category
    category_response = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")

    api_categories = []

    if category_response.status_code == 200:
        category_data = category_response.json()
        api_categories = [category['strCategory'] for category in category_data.get('categories', [])]

    #Get user category
    user_categories = [category.name for category in categories]

    all_categories = sorted(set(api_categories + user_categories))

    # If a category is selected, filter meals by that category, otherwise search by query or show all meals
    if selected_category:
        api_search_query = selected_category
    elif search_query:
        api_search_query = search_query
    else:
        api_search_query = "chicken"  # Default search query to show some results when search is empty

    #saved recipes query
    user_query = Recipe.query.filter(Recipe.user_id == current_user.id)

    #search filter
    if search_query:
        user_query = Recipe.query.filter(db.or_(Recipe.title.ilike(f'%{search_query}%'), Recipe.ingredients.ilike(f'%{search_query}%'), Recipe.instructions.ilike(f'%{search_query}%')))
        
    #category filter
    if selected_category:
        user_query = user_query.join(Category).filter(Category.name == selected_category)

    #pagination for user recipes, 8 recipes per page, newest first
    user_recipes = user_query.order_by(Recipe.created_at.desc()).paginate(page=page, per_page=8, error_out=False)

    #API recipes search and pagination
    
    api_recipes, api_total = search_api_recipes(api_search_query, api_page)
    api_total_pages =max(1, ceil(api_total / api_per_page))

    if api_total_pages == 0:
        api_page = 1
    elif api_page > api_total_pages:
            
        return redirect(url_for('main.search', search=search_query, page=page, api_page=api_total_pages))

    return render_template('search_results.html',user_recipes=user_recipes, api_recipes=api_recipes, search_query=search_query, selected_category=selected_category,api_categories=api_categories, categories=all_categories, page=page, api_page=api_page, api_total_pages=api_total_pages)

# Discover route to show recipes from the API with category filter, search and pagination
@main.route('/discover')
def discover():
    search_query = request.args.get('search', '').strip()
    selected_category = request.args.get('category', '').strip()
    api_page = request.args.get('api_page', 1, type=int)
    api_per_page = 8
    meals = []
    
    #Get API category
    category_response = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")

    api_categories = []

    if category_response.status_code == 200:
        category_data = category_response.json()
        api_categories = [category['strCategory'] for category in category_data.get('categories', [])]

    # If a category is selected, filter meals by that category, otherwise search by query or show all meals
    if selected_category:
        api_search_query = selected_category
    elif search_query:
        api_search_query = search_query
    else:
        api_search_query = "chicken"  # Default search query to show some results when search is empty

    meals, api_total = search_api_recipes(api_search_query, api_page)
    total_pages = max(1, ceil(api_total / api_per_page))

    return render_template('discover.html', meals=meals, search_query=search_query, selected_category=selected_category, categories=api_categories, api_categories=api_categories, api_page=api_page, total_pages=total_pages)

# View TheMeal DB API discover recipe details route
@main.route('/discover/<int:meal_id>')
def view_discover_recipe(meal_id):
    api_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(api_url)

    if response.status_code != 200:
        abort(404)

    data = response.json()
    meals = data.get('meals') or []
    if not meals:
        abort(404)
    
    meal = meals[0]

    recipe = {
        'id': meal.get('idMeal'),
        'title': meal.get('strMeal'),
        'description':f"{meal.get('strArea')} recipe",
        'category': meal.get('strCategory'),
        'image': meal.get('strMealThumb'),
        'ingredients': "",
        'instructions': meal.get('strInstructions'),
        'source': meal.get('strSource'),
        'youtube': meal.get('strYoutube')
    }

    # Extract ingredients and measurements
    ingredients = []
    for i in range(1, 21):
        ingredient = meal.get(f'strIngredient{i}')
        measurement = meal.get(f'strMeasure{i}')
        if ingredient and ingredient.strip():
            ingredients.append(f"{measurement.strip()} {ingredient.strip()}")
    recipe['ingredients'] = "\n".join(ingredients)

    already_imported = None
    if current_user.is_authenticated:
        already_imported = Recipe.query.filter_by(user_id=current_user.id, title=meal.get('strMeal')).first()

    return render_template('view_recipe.html', recipe=recipe, is_api_recipe=True, already_imported=already_imported)

#Import TheMealDB API recipe route
@main.route('/discover/<int:meal_id>/import', methods=['POST'])
@login_required
def import_discover_recipe(meal_id):
    api_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(api_url)
    redirect_to_planner = request.args.get('planner')

    if response.status_code != 200:
        flash('Failed to fetch recipe details from API.', 'error')
        return redirect(url_for('main.discover'))

    data = response.json()
    meals = data.get('meals') or []

    if not meals:
        flash('Recipe not found in API.', 'error')
        return redirect(url_for('main.discover'))
    
    meal = meals[0]

    # Check if the recipe already exists in the user's collection based on title
    existing_recipe = Recipe.query.filter_by(user_id=current_user.id, title=meal.get('strMeal')).first()
    if existing_recipe:

        # if user want to add recipe to planner before importing, redirect to planner page, otherwise redirect to recipe details page
        if redirect_to_planner:
            return redirect(url_for('main.add_meal_plan', recipe_id=existing_recipe.id))
        
        #else after importing, stay on the API recipe details page
        flash('You have already imported this recipe.', 'warning')
        return redirect(url_for('main.view_recipe', meal_id=meal_id))
    
    ingredients = []
    for i in range(1, 21):
        ingredient = meal.get(f'strIngredient{i}')
        measurement = meal.get(f'strMeasure{i}')
        if ingredient and ingredient.strip():
            ingredients.append(f"{measurement.strip()} {ingredient.strip()}")

    instructions_steps = []
    for step in meal.get('strInstructions', '').split('\r\n'):
        if step.strip():
            instructions_steps.append(step.strip())

    #Map API category to user's category, if not found assign to first category
    category_mapping = {
        'Breakfast': 'Breakfast',
        'Lunch': 'Lunch',
        'Dinner': 'Dinner',
        'Dessert': 'Dessert/Snack',
        'Snack': 'Dessert/Snack',
        'Miscellaneous': 'Dinner',
        'Starter': 'Lunch',
        'Side': 'Lunch',
        'Pasta': 'Dinner',
        'Vegan': 'Dinner',
        'Vegetarian': 'Dinner',
        'Gluten-Free': 'Dinner',
        'Seafood': 'Dinner',
        'Beef': 'Dinner',
        'Chicken': 'Dinner',
        'Lamb': 'Dinner',
        'Pork': 'Dinner',
        'Goat': 'Dinner',
    }

    api_category = meal.get('strCategory')
    category_name = category_mapping.get(api_category, 'Dinner')
    category = Category.query.filter_by(name=category_name).first()

    # Create a new recipe based on the API data
    imported_recipe = Recipe(
        title=meal.get('strMeal'),
        category_id=category.id ,
        ingredients="\n".join(ingredients),
        instructions="\n".join(instructions_steps),
        prep_time=30,  # Default prep time for imported recipes
        servings=4,   # Default servings for imported recipes
        image_url=meal.get('strMealThumb'),
        user_id=current_user.id
    )

    db.session.add(imported_recipe)
    db.session.commit()

    # if user want to add recipe to planner before importing, redirect to planner page, otherwise redirect to recipe details page
    if redirect_to_planner:
        return redirect(url_for('main.add_meal_plan', recipe_id=imported_recipe.id))

    flash('Recipe imported successfully!', 'success')
    return redirect(url_for('main.view_discover_recipe', meal_id=meal_id))

# View Spoonacular API discover recipe details route
@main.route('/discover/spoonacular/<int:recipe_id>')
def view_spoonacular_recipe(recipe_id):
    spoonacular_api_key = os.getenv('SPOONACULAR_API_KEY')
    api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={spoonacular_api_key}"
    response = requests.get(api_url)

    if response.status_code != 200:
        abort(404)

    data = response.json()

    ingredients = []

    for item in data.get('extendedIngredients', []):
        if item.get('original'):
            ingredients.append(item['original'])

    recipe = {
        'id': data.get('id'),
        'title': data.get('title'),
        'description': data.get("cuisines")[0] if data.get("cuisines") else "Unknown" + " recipe",
        'category': data.get('dishTypes') [0] if data.get('dishTypes') else 'Recipe',
        'image_url': data.get('image'),
        'ingredients': "\n".join(ingredients),
        'instructions': data.get('instructions'),
        'source': data.get('sourceUrl'),
        'source_name': 'Spoonacular',
        'api_source': 'spoonacular'
    }

    already_imported = None
    if current_user.is_authenticated:
        already_imported = Recipe.query.filter_by(user_id=current_user.id, title=data.get('title')).first()

    return render_template('view_recipe.html', recipe=recipe, is_api_recipe=True, already_imported=already_imported)

#Import Spoonacular API recipe route
@main.route('/discover/spoonacular/<int:recipe_id>/import', methods=['POST'])
@login_required
def import_spoonacular_recipe(recipe_id):
    api_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={os.getenv('SPOONACULAR_API_KEY')}"
    response = requests.get(api_url)
    redirect_to_planner = request.args.get('planner')

    if response.status_code != 200:
        flash('Failed to fetch recipe details from API.', 'error')
        return redirect(url_for('main.discover'))
    
    data = response.json()

    ingredients = []
    for item in data.get('extendedIngredients', []):
        if item.get('original'):
            ingredients.append(item['original'])

    # Check if the recipe already exists in the user's collection based on title
    existing_recipe = Recipe.query.filter_by(user_id=current_user.id, title=data.get('title')).first()
    if existing_recipe:
        flash('You have already imported this recipe.', 'warning')

        # if user want to add recipe to planner before importing, redirect to planner page, otherwise redirect to recipe details page
        if redirect_to_planner:
            return redirect(url_for('main.add_meal_plan', recipe_id=existing_recipe.id))
        
        #else after importing, stay on the API recipe details page
        return redirect(url_for('main.view_spoonacular_recipe', recipe_id=recipe_id))
    
    #Map API category to user's category, if not found assign to first category
    category_mapping = {
        'Breakfast': 'Breakfast',
        'Lunch': 'Lunch',
        'Dinner': 'Dinner',
        'Dessert': 'Dessert/Snack',
        'Snack': 'Dessert/Snack',
    }

    category = Category.query.filter_by(name=category_mapping.get(data.get('dishTypes')[0], 'Dinner')).first()

    imported_recipe = Recipe(
        title=data.get('title'),  
        category_id=category.id,
        ingredients="\n".join(ingredients),
        instructions=data.get('instructions'),
        prep_time=30,  # Default prep time for imported recipes
        servings=4,   # Default servings for imported recipes
        image_url=data.get('image'),
        user_id=current_user.id 
    )

    db.session.add(imported_recipe)
    db.session.commit()

    # if user want to add recipe to planner before importing, redirect to planner page, otherwise redirect to recipe details page
    if redirect_to_planner:
        return redirect(url_for('main.add_meal_plan', recipe_id=imported_recipe.id))

    flash('Recipe imported successfully!', 'success')
    return redirect(url_for('main.view_spoonacular_recipe', recipe_id=recipe_id))

# Support route with GET and POST methods
@main.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        # Validate form data
        if not name or not email or not subject or not message:
            flash('All fields are required.', 'error')
            return render_template('support.html', form_data=request.form)
        
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            flash('Please enter a valid email address.', 'error')
            return render_template('support.html', form_data=request.form)
        
        if len(subject) < 3 or len(subject) > 200:
            flash('Subject must be between 3 and 200 characters long.', 'error')
            return render_template('support.html', form_data=request.form)
        
        if len(message) < 10 or len(message) > 2000:
            flash('Message must be between 10 and 2000 characters long.', 'error')
            return render_template('support.html', form_data=request.form)
        
        if len(name) < 3 or len(name) > 100:
            flash('Name must be between 3 and 100 characters long.', 'error')
            return render_template('support.html', form_data=request.form)
        
        # Create a new support message and add to the database
        support_message = SupportMessage(
            name=name,
            email=email,
            subject=subject,
            message=message,
            user_id=current_user.id if current_user.is_authenticated else None
        )

        db.session.add(support_message)
        db.session.commit()

        flash('Your message has been sent. We will get back to you shortly.', 'success')
        return redirect(url_for('main.support'))
    
    return render_template('support.html')#

#Error handlers
@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@main.app_errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@main.app_errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500