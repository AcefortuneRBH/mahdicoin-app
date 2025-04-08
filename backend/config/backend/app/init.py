import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from .routes import bp as api_bp
from .health import bp as health_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.config.Config")

    CORS(app)
    Migrate(app, db=None)  # Set your SQLAlchemy db instance if needed

    log_handler = RotatingFileHandler('logs/backend.log', maxBytes=10*1024*1024, backupCount=5)
    log_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    app.logger.addHandler(log_handler)

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(health_bp, url_prefix="/health")

    return app
