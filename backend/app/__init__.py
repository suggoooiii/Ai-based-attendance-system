from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize the database
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize plugins
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # Optional: Configure logging
    if not app.debug and not app.testing:
        # Setup your logging here (to file, logging service, etc.)
        pass

    return app
