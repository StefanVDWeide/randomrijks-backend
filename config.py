import os
from dotenv import load_dotenv

# Set base directory of the app
basedir = os.path.abspath(os.path.dirname(__file__))

# Load the .env and .flaskenv variables
load_dotenv(os.path.join(basedir, ".env"))


# Set configuration variables used in the app
class Config(object):

    # General secret key
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # SQL Config
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Rijks Museum API key
    RIJKSMUSEUM_KEY = os.environ.get("RIJKSMUSEUM_KEY")
