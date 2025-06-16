from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    # ✅ Create tables inside app context (fixes "no such table" error)
    with app.app_context():
        db.create_all()

    return app
