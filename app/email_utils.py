#Email helper function for Flask-Mail

from flask_mail import Message
from app import mail
from flask import current_app, render_template
from datetime import datetime

# Email helper function to send notifications to the admin email address
def send_admin_notification(name, email, subject, message, user_status, created_at):
    """Send an email notification to the admin email address."""
    admin_email = current_app.config.get('ADMIN_EMAIL')

    if not admin_email:
        current_app.logger.warning("Admin email not configured. Cannot send notification.")
        return False # Early return if admin email is not configured
    
    user_status = user_status if user_status else "Guest User"
    current_year = datetime.now().year
    html_body = render_template("emails/send_admin_notification.html", name=name, email=email, subject=subject, message=message, user_status=user_status, created_at=created_at, current_year=current_year)
    # Create the email message with the provided details
    msg = Message(subject=f" New Cookfolio support message: {subject}", recipients=[admin_email], body=f""" New support message received. User ID: {user_status} Name: {name} Email: {email} Subject: {subject} Message: {message}""", html=html_body)
    
    # Attempt to send the email and log the result
    try:
        mail.send(msg)
        current_app.logger.info(f"Notification sent to admin.")
        return True
    # Catch any exceptions that occur during email sending and log the error
    except Exception as e:
        current_app.logger.error(f"Failed to send notification: {e}")
        return False