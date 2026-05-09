from app import create_app, db
from app.models import User, Category, Recipe
from werkzeug.security import generate_password_hash
from tests.conftest import app, test_user, test_recipe, client, logged_in_client, db_session

# test 404 error page is displayed when a non-existent route is accessed
def test_404_error_page(client):
    response = client.get('/non-existent-page')
    assert response.status_code == 404
    assert b'Page Not Found' in response.data

#test 403 error page is displayed when a user tries to access a forbidden page
def test_403_error_page(client, logged_in_client):
    response = client.get('/admin')
    assert response.status_code == 403
    assert b'Access Denied' in response.data

# test 500 error page is displayed when an unhandled exception occurs
def test_500_error_page(client):
    @client.application.route('/test-error')
    def test_error():
        # This route is for testing the 500 Internal Server Error page
        raise Exception('This is a test exception to trigger the 500 error page.')
    
    response = client.get('/test-error')
    assert response.status_code == 500
    assert b'Internal Server Error' in response.data