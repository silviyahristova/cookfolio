from werkzeug.security import generate_password_hash
from app.models import User
from app import db

#test if the register page loads correctly
def test_register_page_loads(client):
    response = client.get('/register')

    assert response.status_code == 200
    assert b'Register' in response.data

#test for empty fields
def test_register_empty_fields(client):
    response = client.post('/register', data={
        'username': '',
        'email': '',
        'password': '',
        'confirm_password': ''
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'All fields are required.' in response.data

#test for password mismatch
def test_register_password_mismatch(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123',
        'confirm_password': 'password456'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Passwords do not match.' in response.data

#test for invalid email
def test_register_invalid_email(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'invalidemail',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Please enter a valid email address.' in response.data

#test for duplicate username or email
def test_register_duplicate_username_email(client, app):
    with app.app_context():
        user = User(username='testuser', email='testuser@example.com', password=generate_password_hash('password123'))
        db.session.add(user)
        db.session.commit()

    response = client.post('/register', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Username or email already exists.' in response.data