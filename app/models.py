from sqlalchemy import String, Boolean, DateTime, ForeignKey, func # Importing necessary SQLAlchemy types and functions for defining the database models
from sqlalchemy.orm import Mapped, mapped_column, relationship # Importing Mapped and relationship for defining model attributes and relationships between models
from flask_login import UserMixin # Importing UserMixin for user authentication and session management with Flask-Login
from . import db, login_manager # Importing the database instance and login manager from the app package
from datetime import date, datetime # For handling date and time fields in the models
from typing import List, Optional # For type hinting of relationships
from itsdangerous import URLSafeTimedSerializer # Serializer for generating and verifying password reset tokens

# User model
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False) # Field to indicate if the user has admin privileges
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable=False) # Timestamp for when the user account was created

    #Relationship to support messages- one user can have many support messages, and each support message belongs to one user
    support_messages: Mapped[List['SupportMessage']] = relationship('SupportMessage', back_populates='user', cascade='all, delete-orphan') 

    #Relationship to recipe- one user can have many recipes, and each recipe belongs to one user
    recipes = db.relationship('Recipe', back_populates='user', cascade='all, delete-orphan')

    #Relationship to meal plan- one user can have many meal plans, and each meal plan belongs to one user
    meal_plans = db.relationship('MealPlan', back_populates='user', cascade='all, delete-orphan')

    #Method to check if user is admin
    def is_admin_user(self):
        return self.is_admin
    
    #Method to generate password reset token
    def generate_reset_token(self):
        serializer = URLSafeTimedSerializer(db.app.config['SECRET_KEY']) # Create a serializer using the application's secret key for securely signing the token
        return serializer.dumps(self.email, salt='password-reset-salt') # Generate a token using the user's email and a salt for added security

    #Static method to verify password reset token
    @staticmethod
    def verify_reset_token(token, expiration=3600):
        serializer = URLSafeTimedSerializer(db.app.config['SECRET_KEY']) # Create a serializer using the application's secret key for securely signing the token

        try:
            email = serializer.loads(token, salt='password-reset-salt', max_age=expiration) # Attempt to decode the token and retrieve the email, ensuring it hasn't expired
        except Exception:
            return None # If the token is invalid or has expired, return None
        return User.query.filter_by(email=email).first() # If the token is valid, return the user associated with the email
    
# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

#Category model
class Category(db.Model):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    order: Mapped[int] = mapped_column(nullable=False) #Field to specify the order of categories in the dropdown menu

    #Relationship to recipe- one category can have many recipes, and each recipe belongs to one category
    recipes = db.relationship('Recipe', back_populates='category', cascade='all, delete-orphan')

# Recipe model
class Recipe(db.Model):
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    ingredients: Mapped[str] = mapped_column(db.Text, nullable=False)
    instructions: Mapped[str] = mapped_column(db.Text, nullable=False)
    prep_time: Mapped[int] = mapped_column(nullable=False)
    servings: Mapped[int] = mapped_column(nullable=False)
    image_filename: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(db.Text, nullable=True) # New field to store image URL for API recipes

    #Relationship to category- many recipes can belong to one category, and each recipe belongs to one category
    category = db.relationship('Category', back_populates='recipes')

    #Relationship to user- many recipes can belong to one user, and each recipe belongs to one user
    user = db.relationship('User', back_populates='recipes')

    #Relationship to meal plan- one recipe can have many meal plans, and each meal plan belongs to one recipe
    meal_plans = db.relationship('MealPlan', back_populates='recipe', cascade='all, delete-orphan')

#Meal plan model
class MealPlan(db.Model):
    __tablename__ = 'meal_plans'

    id: Mapped[int] = mapped_column(primary_key=True)
    meal_date: Mapped[date] = mapped_column(nullable=False)
    meal_type: Mapped[str] = mapped_column(String(50), nullable=False) #Breakfast, Lunch, Dinner, or Dessert/Snack
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    recipe_id: Mapped[int] = mapped_column(ForeignKey('recipes.id'), nullable=False)

    #Relationship to user- many meal plans can belong to one user, and each meal plan belongs to one user
    user = db.relationship('User', back_populates='meal_plans')

    #Relationship to recipe- many meal plans can belong to one recipe, and each meal plan belongs to one recipe
    recipe = db.relationship('Recipe', back_populates='meal_plans')

#Support message model for contact form
class SupportMessage(db.Model):
    __tablename__ = 'support_messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    subject: Mapped[str] = mapped_column(String(200), nullable=False)
    message: Mapped[str] = mapped_column(String(2000), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'), nullable=True)
    user: Mapped[Optional['User']] = relationship('User', back_populates='support_messages')

# Function to seed initial categories into the database
def seed_categories():
    categories = [
        {"name": "Breakfast", "order": 1},
        {"name": "Lunch", "order": 2},
        {"name": "Dinner", "order": 3},
        {"name": "Dessert/Snack", "order": 4},
    ]
    for item in categories:
        existing_category = Category.query.filter_by(name=item["name"]).first()

        if not existing_category:
            new_category = Category(name=item["name"], order=item["order"])
            db.session.add(new_category)
    db.session.commit()