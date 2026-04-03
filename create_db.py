from app import create_app, db

app = create_app()

with app.app_context():
    from app.models import User
    db.create_all()