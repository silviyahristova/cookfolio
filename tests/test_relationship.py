from app import create_app, db
from app.models import User, Recipe, Category
from werkzeug.security import generate_password_hash
from tests.conftest import app, test_user, test_recipe, client, logged_in_client, db_session

# Test relationships between User, Recipe, and Category models
#user can have many recipes
def test_user_can_have_many_recipes(db_session, test_user, test_recipe):
    user = db_session.get(User, test_user)
    recipe = db_session.get(Recipe, test_recipe)
    
    assert recipe in user.recipes
    assert user is not None
    assert recipe is not None
    
#recipe belongs to one user
def test_recipe_belongs_to_one_user(db_session, test_user, test_recipe):
    user = db_session.get(User, test_user)
    recipe = db_session.get(Recipe, test_recipe)

    assert recipe.user_id == test_user
    assert recipe.user == user

#recipe belongs to one category
def test_recipe_belongs_to_one_category(db_session, test_recipe):
    
    recipe = db_session.get(Recipe, test_recipe)
    category = Category(name='Test Category', order=1)

    recipe.category = category

    db_session.add(category)
    db_session.add(recipe)
    db_session.commit()

    assert recipe.category == category
    assert recipe is not None
    assert category is not None

#category can have many recipes
def test_category_can_have_many_recipes(db_session, test_recipe):    
    recipe1 = db_session.get(Recipe, test_recipe)
    category = recipe1.category
    recipe2 = Recipe(
        title='Test Recipe 2',
        category=category,
        ingredients='Test Ingredients',
        instructions='Test Instructions',
        prep_time=30,
        servings=4,
        user_id=recipe1.user_id
    )

    db_session.add(recipe2)
    db_session.commit()

    assert recipe1 in category.recipes
    assert recipe2 in category.recipes
    assert len(category.recipes) == 2