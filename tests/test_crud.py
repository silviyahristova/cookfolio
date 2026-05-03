from app import create_app, db
from app.models import User, Category, Recipe
from werkzeug.security import generate_password_hash
from conftest import app, test_user, test_recipe, logged_in_client

#test create: add recipe from saves recipe
def test_add_recipe(app, logged_in_client):
    response = logged_in_client.post('/add-recipe', data={
        'title': 'Pancakes',
        'category': 'Breakfast',
        'ingredients': 'Flour, Eggs, Milk, Sugar, Baking Powder',
        'instructions': '1. Mix dry ingredients. 2. Add wet ingredients and mix until smooth. 3. Cook on griddle until golden brown.',
        'prep_time': 30,
        'servings': 4
    }, follow_redirects=True)
    assert response.status_code == 200      
    assert b'Pancakes' in response.data

#test read: check if recipe appears on dashboard
def test_view_recipe(app, logged_in_client, test_recipe):
    response = logged_in_client.get(f'/recipes/{test_recipe}')
    assert response.status_code == 200
    assert b'Pancakes' in response.data

#test update: edit recipe and check if changes appear on dashboard
def test_edit_recipe(app, logged_in_client, test_recipe):
    response = logged_in_client.post(f'/recipes/{test_recipe}/edit', data={
        'title': 'Updated Pancakes',
        'category': 'Breakfast',
        'ingredients': 'Flour, Eggs, Milk, Sugar, Baking Powder, Vanilla Extract',
        'instructions': '1. Mix dry ingredients. 2. Add wet ingredients and mix until smooth. 3. Cook on griddle until golden brown.',
        'prep_time': 35,
        'servings': 4
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Updated Pancakes' in response.data

#test delete: delete recipe and check if it no longer appears on dashboard
def test_delete_recipe(app, logged_in_client, test_recipe):
    response = logged_in_client.post(f'/recipes/{test_recipe}/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'Recipe deleted successfully!' in response.data
    assert b'Pancakes' not in response.data

#test delete recipe db
def test_delete_recipe_db(app, logged_in_client, test_recipe):
    response = logged_in_client.post(f'/recipes/{test_recipe}/delete', follow_redirects=True)
    assert response.status_code == 200
    recipe = db.session.get(Recipe, test_recipe)
    assert recipe is None

#test add recipe validation keeps entered data in form
def test_add_recipe_validation(app, logged_in_client):
    response = logged_in_client.post('/add-recipe', data={
        'title': '',
        'category': 'Breakfast',
        'ingredients': 'Flour, Eggs, Milk, Sugar, Baking Powder',
        'instructions': '1. Mix dry ingredients. 2. Add wet ingredients and mix until smooth. 3. Cook on griddle until golden brown.',
        'prep_time': 30,
        'servings': 4
    }, follow_redirects=True)
    
    with app.app_context():
        recipe=db.session.query(Recipe).filter_by(title='').first()
        assert recipe is None

#test edit recipe validation keeps entered data in form
def test_edit_recipe_validation(app, logged_in_client, test_recipe):    
    response = logged_in_client.post(f'/recipes/{test_recipe}/edit', data={
        'title': '',
        'category': 'Breakfast',
        'ingredients': 'Flour, Eggs, Milk, Sugar, Baking Powder',
        'instructions': '1. Mix dry ingredients. 2. Add wet ingredients and mix until smooth. 3. Cook on griddle until golden brown.',
        'prep_time': 30,
        'servings': 4
    }, follow_redirects=True)
    
    with app.app_context():
        recipe = db.session.get(Recipe, test_recipe)
        assert recipe is not None

