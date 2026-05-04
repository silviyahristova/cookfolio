from app import create_app, db
from app.models import User, Category, Recipe
from werkzeug.security import generate_password_hash
from tests.conftest import app, test_user, test_recipe, client, logged_in_client, db_session

# Test to ensure that the home page loads correctly
def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Cookfolio' in response.data

# Test to ensure that login page loads correctly
def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

# Test to ensure that register page loads correctly
def test_register_page(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b'Register' in response.data

# Test to ensure that the dashboard page loads correctly for logged in users
def test_dashboard_page_logged_in(logged_in_client):
    response = logged_in_client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data

# Test to ensure that the dashboard page redirects to login for non-logged in users
def test_dashboard_page_not_logged_in(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

# Test logout functionality
def test_logout(client, logged_in_client):
    response = logged_in_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

#my reicpes page requires login
def test_my_recipes_page_requires_login(client):
    response = client.get('/my-recipes', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

#test to ensure that the my recipes page loads correctly for logged in users
def test_my_recipes_page_logged_in(logged_in_client):
    response = logged_in_client.get('/my-recipes')
    assert response.status_code == 200
    assert b'My Recipes' in response.data

#test to ensure that the view recipe page loads for logged in users
def test_view_recipe_page_logged_in(logged_in_client, test_recipe):
    response = logged_in_client.get(f'/recipes/{test_recipe}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Pancakes' in response.data

#test to ensure that the view recipe page loads for non-logged in users
def test_view_recipe_page_not_logged_in(client, test_recipe):
    response = client.get(f'/recipes/{test_recipe}')
    assert response.status_code == 302

#test to ensure that the add recipe page loads correctly for logged in users
def test_add_recipe_page_logged_in(logged_in_client):
    response = logged_in_client.get('/add-recipe')
    assert response.status_code == 200
    assert b'Add Recipe' in response.data

#test to ensure that the add recipe page redirects to login for non-logged in users
def test_add_recipe_page_not_logged_in(client): 
    response = client.get('/add-recipe', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data

#test to ensure that the edit recipe page loads correctly for logged in users
def test_edit_recipe_page_logged_in(logged_in_client, test_recipe):
    response = logged_in_client.get(f'/recipes/{test_recipe}/edit')
    assert response.status_code == 200
    assert b'Edit Recipe' in response.data

#test to ensure that the edit recipe page redirects to login for non-logged in users
def test_edit_recipe_page_not_logged_in(client, test_recipe):
    response = client.get(f'/recipes/{test_recipe}/edit', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data    

#test delete recipe functionality for logged in users
def test_delete_recipe_logged_in(logged_in_client, test_recipe):
    response = logged_in_client.post(f'/recipes/{test_recipe}/delete', follow_redirects=True)
    assert response.status_code == 200

#test delete recipe functionality redirects to login for non-logged in users
def test_delete_recipe_not_logged_in(client, test_recipe):
    response = client.post(f'/recipes/{test_recipe}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' in response.data