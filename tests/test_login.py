from app.models import User
from app import db
from werkzeug.security import generate_password_hash

#test if the login page loads correctly
def test_login_page_loads(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data

#test if the login is successful with correct credentials
def test_login_success(client, app):
    with app.app_context():
        user = User(username='testuser', email='testuser@example.com', password=generate_password_hash('testpassword'))
        db.session.add(user)
        db.session.commit()

    response = client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Logged in successfully.' in response.data

#test if login with wrong password
def test_login_wrong_password(client, app):
    with app.app_context():
        user = User(username='testuser', email='testuser@example.com', password=generate_password_hash('testpassword'))
        db.session.add(user)
        db.session.commit()

    response = client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'wrongpassword'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

#test if login with user that does not exist
def test_login_user_not_found(client, app):
    with app.app_context():
        user = User(username='testuser', email='testuser@example.com', password=generate_password_hash('testpassword'))
        db.session.add(user)
        db.session.commit()

    response = client.post('/login', data={
        'username': 'nouser',
        'email': 'nouser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Invalid username or password' in response.data

#test if login with empty fields
def test_login_empty_fields(client):
    response = client.post('/login', data={
        'username': '',
        'email': '',
        'password': ''
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Login' in response.data

#test if route is protected
def test_protected_route_requires_login(client):
    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please log in to access this page' in response.data

#test if user can access protected route after login
def test_access_protected_route_after_login(client, app):
    with app.app_context():
        user = User(username='testuser', email='testuser@example.com', password=generate_password_hash('testpassword'))
        db.session.add(user)
        db.session.commit()

    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    response = client.get('/dashboard', follow_redirects=True)
    assert response.status_code == 200
    assert b'dashboard' in response.data

#test if the logout functionality works correctly
def test_logout(client, app):
    with app.app_context():
        user = User(username='testuser', email='testuser@example.com', password=generate_password_hash('testpassword'))
        db.session.add(user)
        db.session.commit()

    client.post('/login', data={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }, follow_redirects=True)

    response = client.get('/logout', follow_redirects=True)

    assert response.status_code == 200
    assert b'You have been logged out' in response.data