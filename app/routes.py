import os
from flask import Blueprint , render_template, request, flash, redirect, url_for, session
from flask_login import login_user, logout_user, current_user, login_required
from flask import current_app
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Recipe
from . import db
import re
from functools import wraps

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
            return redirect(url_for('main.home'))
        return view_function(*args, **kwargs)
    return wrapped_view_function

#admin dashboard route
@main.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

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

#recipe routes
@main.route('/add-recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category = request.form.get('category', '').strip()
        ingredients = request.form.get('ingredients', '').strip()
        instructions = request.form.get('instructions', '').strip()
        prep_time = request.form.get('prep_time', '').strip()
        servings = request.form.get('servings', '').strip()

        photo = request.files.get('photo')

        # Validate form data
        if not title or not category or not ingredients or not instructions or not prep_time or not servings :
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('main.add_recipe'))
        
        try:
            prep_time = int(prep_time)
            servings = int(servings)
        except ValueError:
            flash('Prep time and servings must be valid numbers.', 'error')
            return redirect(url_for('main.add_recipe'))
        
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
                return redirect(url_for('main.add_recipe'))

        # Create a new recipe and add to the database
        new_recipe = Recipe(
            title=title,
            category=category,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time,
            servings=servings,
            image_filename=image_filename,
            user_id=current_user.id
        )

        db.session.add(new_recipe)
        db.session.commit()

        flash('Recipe added successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('add_recipe.html')

@main.route('/dashboard')
@login_required
def dashboard():
    recipes = Recipe.query.filter_by(user_id=current_user.id).order_by(Recipe.created_at.desc()).all()
    return render_template('dashboard.html', recipes=recipes)

@main.route('/recipes/<int:recipe_id>')
@login_required
def view_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.user_id != current_user.id:
        flash('You do not have permission to view this recipe.', 'error')
        return redirect(url_for('main.dashboard'))
    
    return render_template('view_recipe.html', recipe=recipe)

@main.route('/recipes/<int:recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

    if recipe.user_id != current_user.id:
        flash('You do not have permission to edit this recipe.', 'error')
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category = request.form.get('category', '').strip()
        ingredients = request.form.get('ingredients', '').strip()
        instructions = request.form.get('instructions', '').strip()
        prep_time = request.form.get('prep_time', '').strip()
        servings = request.form.get('servings', '').strip()

        photo = request.files.get('photo')

        db.session.commit() 

        flash('Recipe updated successfully!', 'success')
        return redirect(url_for('main.view_recipe', recipe_id=recipe_id))
    
    return render_template('edit_recipe.html', recipe=recipe)
    
@main.route('/recipes/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)

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
    return redirect(url_for('main.dashboard'))

@main.route('/my-recipes')
@login_required
def my_recipes():
    recipes = Recipe.query.filter_by(user_id=current_user.id).order_by(Recipe.created_at.desc()).all()
    return render_template('my_recipes.html', recipes=recipes)

@main.route('/search')
@login_required
def search():
    query = request.args.get('search', '').strip()
    if not query:
        return redirect(url_for('main.dashboard'))
    
    #search users recipes by title
    results = Recipe.query.filter(Recipe.user_id == current_user.id, Recipe.title.ilike(f'%{query}%')).order_by(Recipe.created_at.desc()).all()
    return render_template('search_results.html', query=query, results=results)

@main.route('/meal-plans')
@login_required
def meal_plans():
    return render_template('meal_plans.html')

@main.route('/discover')
def discover():
    return render_template('discover.html')

@main.route('/support')
def support():
    return render_template('support.html')