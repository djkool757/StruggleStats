from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  Column, Integer, String, ForeignKey
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    CORS(app)

    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app