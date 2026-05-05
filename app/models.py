from sqlalchemy import String, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from . import db, login_manager
from datetime import datetime
from typing import List, Optional

# User model
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    support_messages: Mapped[List['SupportMessage']] = relationship('SupportMessage', back_populates='user', cascade='all, delete-orphan')

    #Relationship to recipe- one user can have many recipes, and each recipe belongs to one user
    recipes = db.relationship('Recipe', back_populates='user', cascade='all, delete-orphan')

    #Method to check if user is admin
    def is_admin_user(self):
        return self.is_admin

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
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), nullable=False)
    ingredients: Mapped[str] = mapped_column(String(1000), nullable=False)
    instructions: Mapped[str] = mapped_column(String(2000), nullable=False)
    prep_time: Mapped[int] = mapped_column(nullable=False)
    servings: Mapped[int] = mapped_column(nullable=False)
    image_filename: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    #Relationship to category- many recipes can belong to one category, and each recipe belongs to one category
    category = db.relationship('Category', back_populates='recipes')

    #Relationship to user- many recipes can belong to one user, and each recipe belongs to one user
    user = db.relationship('User', back_populates='recipes')

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