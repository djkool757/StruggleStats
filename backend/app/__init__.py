from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    CORS(app)

    from .routes import api
    app.register_blueprint(api, url_prefix='/api')
    with app.app_context():
        db.create_all()
    return app