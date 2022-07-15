#cInitializes and ties everything together for the application

# where application is initialized
from flask import Flask
# To use Sass compiler
from flask_assets import Environment, Bundle
#sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] ='5e5d7fe67000e6af38191fdf09f998da'
#sqlite3 database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///quiz.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view = 'login'

from application import routes

# setting up sass compiler
assets     = Environment(app)
assets.url = app.static_url_path
scss       = Bundle('style.scss', filters='pyscss', output='all.css')
assets.config['SECRET_KEY'] = 'secret!'
assets.config['PYSCSS_LOAD_PATHS'] = assets.load_path
assets.config['PYSCSS_STATIC_URL'] = assets.url
assets.config['PYSCSS_STATIC_ROOT'] = assets.directory
assets.config['PYSCSS_ASSETS_URL'] = assets.url
assets.config['PYSCSS_ASSETS_ROOT'] = assets.directory
assets.register('scss_all', scss)
