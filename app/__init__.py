import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('cookfolio_secret_key')

    # Database configuration#
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app