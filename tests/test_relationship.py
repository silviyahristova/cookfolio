from app import create_app, db
from app.models import User, Recipe, Category, SupportMessage
from werkzeug.security import generate_password_hash
from tests.conftest import app, test_user, test_recipe, client, logged_in_client, db_session

# Test relationships between User, Recipe, and Category and SupportMessage models
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

#support message belongs to one user (or can be null for non-logged in users)
def test_support_message_belongs_to_one_user(db_session, test_user):
    user = db_session.get(User, test_user)

    support_message = SupportMessage(
        name='Test User',
        email='test@example.com',
        subject='Test Subject',
        message='Test Message',
        user=user
    )

    db_session.add(support_message)
    db_session.commit()

    assert support_message.user == user

#one user can have many support messages
def test_user_can_have_many_support_messages(db_session, test_user):
    user = db_session.get(User, test_user)

    support_message1 = SupportMessage(
        name='Test User',
        email='test@example.com',
        subject='Test Subject 1',
        message='Test Message 1',
        user=user
    )

    support_message2 = SupportMessage(
        name='Test User',
        email='test@example.com',
        subject='Test Subject 2',
        message='Test Message 2',
        user=user
    )

    db_session.add(support_message1)
    db_session.add(support_message2)
    db_session.commit()

    assert support_message1.user == user
    assert support_message2.user == user
    assert len(user.support_messages) == 2

#support messages for guest users
def test_support_message_for_guest_user(db_session):
    support_message = SupportMessage(
        name='Guest User',
        email='guest@example.com',
        subject='Guest Subject',
        message='Guest Message'
    )

    db_session.add(support_message)
    db_session.commit()

    assert support_message.user is None

#deleting user deletes associated recipes and support messages
def test_deleting_user_deletes_associated_recipes_and_support_messages(db_session, test_user):
    user = db_session.get(User, test_user)

    support_message = SupportMessage(
        name='Test User',
        email='test@example.com',
        subject='Test Subject',
        message='Test Message',
        user=user
    )

    db_session.add(support_message)
    db_session.commit()

    db_session.delete(user)
    db_session.commit()

    deleted_user = db_session.get(User, test_user)
    deleted_recipe = db_session.query(Recipe).filter_by(user_id=test_user).first()
    deleted_support_message = db_session.query(SupportMessage).filter_by(user_id=test_user).first()

    assert deleted_user is None
    assert deleted_recipe is None
    assert deleted_support_message is None