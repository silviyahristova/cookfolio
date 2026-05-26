# turn testing mode and create test version for the app
import os
import sys
import tempfile
import pytest
from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import SupportMessage, User, Category, Recipe, MealPlan
from datetime import datetime, timedelta

# Add the parent directory to the system path to allow imports from the app package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Fixture to create a test app with an in-memory database


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    os.environ["TESTING"] = "1"
    os.environ["DATABASE_URL"] = "sqlite:///" + str(db_path)

    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "WTF_CSRF_ENABLED": False,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///" + str(db_path),
            # Ensure exceptions are not propagated to the test client,
            # allowing error handlers to be tested, mainly the 500 error handler
            "PROPAGATE_EXCEPTIONS": False,
        }
    )

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


# fixture to provide a database session for
# tests that need to interact with the database


@pytest.fixture
def db_session(app):
    with app.app_context():
        yield db.session


# Fixture to create a test user for login tests


@pytest.fixture
def test_user(app):
    with app.app_context():
        user = User(
            username="testuser",
            email="testuser@test.com",
            password=generate_password_hash("testpassword"),
        )
        db.session.add(user)
        db.session.commit()
        return user.id


# fixture to create a recipe for testing the dashboard page


@pytest.fixture
def test_recipe(app, test_user):
    with app.app_context():
        user = User.query.filter_by(username="testuser").first()
        category = Category.query.filter_by(name="Breakfast").first()
        if not category:
            category = Category(name="Breakfast", order=1)
            db.session.add(category)
            db.session.commit()

        recipe = Recipe(
            title="Pancakes",
            category_id=category.id,
            ingredients="Flour, Eggs, Milk, Sugar, Baking Powder",
            instructions="1. Mix dry ingredients. "
            "2. Add wet ingredients and mix until smooth. "
            "3. Cook on griddle until golden brown.",
            prep_time=30,
            servings=4,
            user_id=user.id,
        )
        db.session.add(recipe)
        db.session.commit()

        return recipe.id


# fixture to login the test user for testing the dashboard page


@pytest.fixture
def logged_in_client(client, test_user):
    client.post(
        "/login",
        data={
            "username": "testuser",
            "email": "testuser@test.com",
            "password": "testpassword",
        },
        follow_redirects=True,
    )
    return client


# fixture for admin user for testing the admin page


@pytest.fixture
def admin_user(app):
    with app.app_context():
        admin = User(
            username="admin",
            is_admin=True,
            email="admin@example.com",
            password=generate_password_hash("adminpassword"),
        )

        db.session.add(admin)
        db.session.commit()

        return admin


# fixture to create a support message for testing the support page


@pytest.fixture
def test_support_message(app):
    with app.app_context():

        support_message = SupportMessage(
            name="Test User",
            email="testuser@example.com",
            subject="Test Support Message",
            message="This is a test support message.",
        )

        db.session.add(support_message)
        db.session.commit()

        return support_message


# fixture to create a meal plan for testing the meal plan page


@pytest.fixture
def test_meal_plan(db_session, test_user, test_recipe):

    meal_plan = MealPlan(
        meal_date=datetime.now().date() + timedelta(days=1),
        meal_type="Dinner",
        user_id=test_user,
        recipe_id=test_recipe,
    )
    db.session.add(meal_plan)
    db.session.commit()

    return meal_plan.id


# Fixture to create a test client for making requests to the app


@pytest.fixture
def client(app):
    return app.test_client()
