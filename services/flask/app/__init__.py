from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate
# from . import routes, models

# Globally accessible libraries
db = SQLAlchemy()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes

        # Migration
        migrate = Migrate(app, db)

        return app