import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

# Ensure that the .env file is loaded and correct DATABASE_URL is used
load_dotenv(override=True)

# Initialize Flask extensions
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app():
    # Create the Flask application instance
    app = Flask(__name__, instance_relative_config=True)

    # Set the secret key for session management
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    # Database configuration
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    # Set the SQLALCHEMY_DATABASE_URI configuration,
    # defaulting to a local SQLite database if DATABASE_URL is not set
    app.config["SQLALCHEMY_DATABASE_URI"] = uri or "sqlite:///project.db"
    print(f"Using database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # File upload configuration, uploaded files
    # will be stored in 'static/uploads' directory
    app.config["UPLOAD_FOLDER"] = os.path.join(app.static_folder, "uploads")
    # 16 MB limit for uploaded files
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

    db.init_app(app)

    # Initialize Flask-Login
    login_manager.init_app(app)
    # Configure Flask-Login
    login_manager.login_view = "main.login"
    login_manager.login_message_category = "warning"
    login_manager.login_message = "Please log in to access this page."

    # Initialize and configure Flask-Mail
    app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT", 587))
    app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS", "true").lower() == "true"
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
    app.config["ADMIN_EMAIL"] = os.getenv("ADMIN_EMAIL")

    mail.init_app(app)

    # Initialize Flask-Migrate
    migrate.init_app(app, db)

    from .routes import main

    app.register_blueprint(main)

    return app
