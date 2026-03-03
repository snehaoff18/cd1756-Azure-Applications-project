"""
The flask application package.
"""
import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# -----------------------------------
# Create Flask App
# -----------------------------------
app = Flask(__name__)
app.config.from_object(Config)

# 🔥 Enable Debug Mode (FOR DEVELOPMENT ONLY)
app.config["DEBUG"] = True

# -----------------------------------
# Logging Configuration
# -----------------------------------
if not app.debug:

    app.logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] in %(module)s: %(message)s'
    )

    # Console logging (important for Azure)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(stream_handler)

    # File logging (local use)
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler(
        'logs/flask_app.log',
        maxBytes=10240,
        backupCount=10
    )
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

    app.logger.info('Flask application startup')

# -----------------------------------
# Extensions
# -----------------------------------
Session(app)
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

# -----------------------------------
# Import Views
# -----------------------------------
import FlaskWebProject.views