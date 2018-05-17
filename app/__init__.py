from flask import Flask
from config import Config
import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


def create_app():
    a = Flask(__name__)
    a.config.from_object(Config)
    return a


from app import routes, models