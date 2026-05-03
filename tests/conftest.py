# turn testing mode and create test version for the app
import os
import sys
import tempfile
import pytest
from werkzeug.security import generate_password_hash

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User, Category, Recipe

# Fixture to create a test app with an in-memory database
@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    os.environ['TESTING'] = '1'
    os.environ['DATABASE_URL'] = 'sqlite:///' + str(db_path)

    app = create_app()
    app.config.update({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + str(db_path)
        })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

# Fixture to create a test user for login tests
@pytest.fixture
def test_user(app):
    with app.app_context():
        user = User(username='testuser', email='testuser@test.com', password=generate_password_hash('testpassword'))
        db.session.add(user)
        db.session.commit()
        return user.id

#fixture to create a recipe for testing the dashboard page
@pytest.fixture
def test_recipe(app, test_user):
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        category = Category.query.filter_by(name='Breakfast').first()
        if not category:
            category = Category(name='Breakfast', order=1)
            db.session.add(category)
            db.session.commit()

        recipe = Recipe(
            title='Pancakes',
            category_id=category.id,
            ingredients='Flour, Eggs, Milk, Sugar, Baking Powder',
            instructions='1. Mix dry ingredients. 2. Add wet ingredients and mix until smooth. 3. Cook on griddle until golden brown.',
            prep_time=30,
            servings=4,
            user_id=user.id
        )
        db.session.add(recipe)
        db.session.commit()
        
        return recipe.id

#fixture to login the test user for testing the dashboard page
@pytest.fixture
def logged_in_client(client, test_user):
    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password': 'testpassword'
    }, follow_redirects=True)
    return client

# Fixture to create a test client for making requests to the app
@pytest.fixture
def client(app):
    return app.test_client()