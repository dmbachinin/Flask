from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate


from blog.configs import BaseConfig
from blog.models.database import db
from flask_wtf import CSRFProtect

login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(BaseConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from blog.user.views import user
    from blog.auth.views import auth
    from blog.author.views import author
    from blog.articles.views import article

    app.register_blueprint(user)
    app.register_blueprint(author)
    app.register_blueprint(article)
    app.register_blueprint(auth)

#
# @app.route('/', methods=["GET"])
# def index():
#     return f"Вы находитесь в корне сайта", 200
#
#
# @app.errorhandler(404)
# def error_404(error):
#     return "Страничка не найдена :("
