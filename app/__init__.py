from flask import Flask, blueprints
from .main import view, post
from app import config
from .exts import db
from flask_cors import CORS


def create_app():
    app = Flask("app")
    CORS(app, supports_credentials=True)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_blueprints(app):

    app.register_blueprint(view.view_bp)
    app.register_blueprint(post.post_bp, url_prefix="/post")


def register_extensions(app):
    db.init_app(app)