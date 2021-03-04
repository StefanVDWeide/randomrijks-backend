from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app(config_class=Config):
    """
    Flask application factory which is responsible for building and
    initilizaing the Flask app object

    Parameters
    ----------
    config_class
        Class object containing all the nessacry configuration variables
        to setup the tapp

    Returns
    -------
    Object
        The app object used to start an instance of the application
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        cors.init_app(app)

        from app.errors import bp as errors_bp
        app.register_blueprint(errors_bp)

        from app.main import bp as main_bp
        app.register_blueprint(main_bp, url_prefix="/api")

    return app
