from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

# Globally accessible libraries
db = SQLAlchemy()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                             'postgresql+psycopg2://test:test@0.0.0.0:5401/test')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        migrate = Migrate(app, db)

        return app
