import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('cookfolio_secret_key')

    from .routes import main
    app.register_blueprint(main)

    return app