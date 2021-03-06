import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

from flask_bootstrap import Bootstrap
from flask import Flask, request, current_app
from config import Config


bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
