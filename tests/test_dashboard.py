from unicodedata import category

from app import create_app, db
from app.models import User, Category, Recipe
from werkzeug.security import generate_password_hash

from tests.conftest import app, test_user, client, test_recipe

#test to ensure dashboard page requires login
def test_dashboard_requires_login(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please log in to access this page.' in response.data
    
# Test to ensure that the dashboard page loads correctly
def test_dashboard_page(client, test_user):
    # Log in the user
    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Welcome to your dashboard!' in response.data

# Test to ensure that the dashboard page displays recipe categories section
def test_dashboard_displays_recipe_categories(client, test_user, test_recipe):
    # Log in the user
    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Breakfast' in response.data
    
# test to ensure that if there are no recipes, the appropriate message is displayed
def test_dashboard_no_recipes_message(client, test_user):
    # Log in the user
    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    # Access the dashboard page
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'You haven\'t added any recipes yet.' in response.data

# test to ensure category counts are displayed correctly on the dashboard page
def test_dashboard_category_counts(client, test_user, test_recipe):
    # Log in the user
    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    # Access the dashboard page
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'1' in response.data  # there is 1 recipe in the 'Breakfast' category

#test empty category has 0 count
def test_dashboard_empty_category_message(client, test_user):
    # Log in the user
    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    # Access the dashboard page
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'0' in response.data  # there are 0 recipes in the 'Lunch' category

# test to ensure that user can access only their own recipes on the dashboard page
def test_dashboard_user_recipes(client, test_user, test_recipe):
    # Log in the user
    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@test.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    # Access the dashboard page
    response = client.get('/dashboard')
    assert response.status_code == 200