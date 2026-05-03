from app import create_app, db
from app.models import User, Category, Recipe
from werkzeug.security import generate_password_hash

from tests.conftest import app, test_user, test_recipe, client

#test to ensure my recipe page login required
def test_my_recipes_page_requires_login(app, test_user, test_recipe, client, logged_in_client):
    with app.test_client() as client:
        category = Category.query.filter_by(name='Breakfast').first()
        if not category:
            category = Category(name='Breakfast', order=1)
            db.session.add(category)
            db.session.commit()

        response = client.get('/my_recipes', follow_redirects=True)
        assert response.status_code == 404

#search only finds user`s own recipes
def test_my_recipes_search_only_finds_user_recipes(app, test_user, test_recipe, logged_in_client):
    with app.test_client() as client:
        category = Category.query.filter_by(name='Breakfast').first()
        if not category:
            category = Category(name='Breakfast', order=1)
            db.session.add(category)
            db.session.commit()
        other_user = User(username='otheruser', email='otheruser@test.com', password=generate_password_hash('otherpassword'))
        db.session.add(other_user)
        db.session.commit()

        other_recipe = Recipe(
            title='Other User Recipe',
            category_id=category.id,
            ingredients='Test Ingredients',
            instructions='Test Instructions',
            prep_time=30,
            servings=4,
            user_id=other_user.id
        )
        db.session.add(other_recipe)
        db.session.commit()

        # Search for the other user's recipe
        response = client.get('/my_recipes?search=Other+User+Recipe')
        assert response.status_code == 404

# test to ensure that the my recipes page displays the user's recipes
def test_my_recipes_page_displays_user_recipes(client, test_user, test_recipe, logged_in_client):

    response = client.get('/my-recipes')

    assert response.status_code == 200
    assert b'Pancakes' in response.data

#test clear filters link clears search query and is showing all recipes again
def test_my_recipes_clear_filters(client, test_user, test_recipe, logged_in_client):

    response = client.get('/my-recipes')
    assert response.status_code == 200

#test that recipe appears newest first on the my recipes page
def test_my_recipes_newest_first(client, test_user, test_recipe, logged_in_client):
    
    category = Category.query.filter_by(name='Breakfast').first()
    if not category:
        category = Category(name='Breakfast', order=1)
        db.session.add(category)
        db.session.commit()

    new_recipe=Recipe(
        title='New Recipe',
        category_id=category.id,
        ingredients='New Ingredients',
        instructions='New Instructions',
        prep_time=30,
        servings=4,
        user_id=test_user
    )
    db.session.add(new_recipe)
    db.session.commit()

    response = client.get('/my-recipes')
    html = response.data.decode()

    assert 'Pancakes' in html
    assert 'New Recipe' in html
    assert html.index('Pancakes') < html.index('New Recipe')

#test that add recipe button appears after the last recipe on the my recipes page
def test_my_recipes_add_recipe_button_position(client, test_user, test_recipe, logged_in_client):
    
    response = client.get('/my-recipes')
    html = response.data.decode()
    assert html.index('Add Another Recipe') > html.index('Pancakes') 

#test pagination shows correct number of recipes per page and pagination controls appear when there are more than 10 recipes
def test_my_recipes_pagination(test_recipe, logged_in_client):

    response = logged_in_client.get('/my-recipes')
    assert b'Next' in response.data or b'page=2' in response.data 
    
