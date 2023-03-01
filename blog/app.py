from flask import Flask
from flask_login import LoginManager
import json
import os

from blog.models.database import db


login_manager = LoginManager()
def create_app() -> Flask:
    app = Flask(__name__)

    cfg_name = os.environ.get("CONFIG_NAME") or "BaseConfig"
    app.config.from_object(f"blog.configs.{cfg_name}")
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    from blog.user.views import user
    from blog.report.views import report
    from blog.auth.views import auth

    app.register_blueprint(user)
    app.register_blueprint(report)
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
