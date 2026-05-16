from datetime import datetime, timedelta
import pytest
from werkzeug.security import generate_password_hash
from app.models import User, Category, Recipe, MealPlan

from tests.conftest import db_session, test_user, test_recipe, app, logged_in_client, client, test_meal_plan

# test add meal plan successfully
def test_add_meal_plan(logged_in_client, test_recipe):
    meal_date = (datetime.now() + timedelta(days=2)) # Set meal date to 2 days in the future to avoid validation errors
    response = logged_in_client.post('/meal-plans/add', data={
        'meal_date': meal_date.strftime('%Y-%m-%d'),
        'meal_type': 'Dinner',
        'recipe_id': test_recipe
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Meal plan added successfully!' in response.data

# test edit meal plan successfully
def test_edit_meal_plan(logged_in_client, test_meal_plan, test_recipe):
    meal_plan_id = test_meal_plan
    meal_date = (datetime.now() + timedelta(days=3)) # Set meal date to 3 days in the future to avoid validation errors
    response = logged_in_client.post(f'/meal-plans/{meal_plan_id}/edit', data={
        'meal_date': meal_date.strftime('%Y-%m-%d'),
        'meal_type': 'Lunch',
        'recipe_id': test_recipe
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Meal plan updated successfully!' in response.data

# test delete meal plan successfully
def test_delete_meal_plan(logged_in_client, test_meal_plan):
    meal_plan_id = test_meal_plan
    response = logged_in_client.post(f'/meal-plans/{meal_plan_id}/delete', follow_redirects=True)

    assert response.status_code == 200
    assert b'Meal plan deleted successfully!' in response.data