from app import db
from app.models import SupportMessage, User
from flask_mail import Mail
from werkzeug.security import generate_password_hash
from app import create_app
from conftest import app, admin_user, test_support_message

# test support page loading


def test_support_page(client):
    response = client.get('/support')
    assert response.status_code == 200
    assert b'Support' in response.data

# test support form submission


def test_support_form_submission(client, app):
    response = client.post('/support', data={
        'name': 'Test User',
        'email': 'testuser@example.com',
        'subject': 'Test Support Message',
        'message': 'This is a test support message.'
    }, follow_redirects=True)

    assert response.status_code == 200  # Redirect after successful submission
    assert b'Your message has been sent. We will get back to you shortly' in response.data

    with app.app_context():
        # Verify that the support message was saved in the database
        support_message = SupportMessage.query.filter_by(
            email='testuser@example.com'
        ).first()

        assert support_message is not None
        assert support_message.name == 'Test User'
        assert support_message.message == 'This is a test support message.'

# test support form submission with empty fields


def test_support_form_submission_empty_fields(client):
    response = client.post('/support', data={
        'name': '',
        'email': '',
        'subject': '',
        'message': ''
    }, follow_redirects=True)

    assert response.status_code == 200  # Form should be re-rendered with errors
    assert b'All fields are required' in response.data

# test support form submission with invalid email


def test_support_form_submission_invalid_email(client):
    response = client.post('/support', data={
        'name': 'Test User',
        'email': 'invalid-email',
        'subject': 'Test Support Message',
        'message': 'This is a test support message.'
    }, follow_redirects=True)

    assert response.status_code == 200  # Form should be re-rendered with errors
    assert b'Please enter a valid email address' in response.data

# test admin can view support messages


def test_admin_view_support_messages(client, app, admin_user, test_support_message):

    # Log in as admin user
    client.post('/login', data={
        'username': 'admin',
        'password': 'adminpassword'
    }, follow_redirects=True)

    response = client.get('/admin/support-messages', follow_redirects=True)
    assert response.status_code == 200
    assert b'This is a test support message.' in response.data
