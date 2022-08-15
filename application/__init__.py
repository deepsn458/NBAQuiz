# Initializes and ties everything together for the application
# where application is initialized
from flask import Flask
# To use Sass compiler
from flask_assets import Environment, Bundle
#sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from application.config import Config
#creation of extension objects
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    # imports all the 3 blueprints
    from application.main.routes import main
    from application.quiz.routes import Quiz
    from application.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(Quiz)
    app.register_blueprint(errors)
    # extension objects applied to each application
    db.init_app(app)
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

    return app
