# turn testing mode and create test version for the app
import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app()
    app.config.update({
        'TESTING': True
        })
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
    
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()