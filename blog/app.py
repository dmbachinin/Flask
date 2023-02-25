from flask import Flask, Response, request
from blog.user.views import user
from blog.report.views import report
import json
from blog.models.database import db


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_file('settings.json', load=json.load)
    db.init_app(app)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)

#
# @app.route('/', methods=["GET"])
# def index():
#     return f"Вы находитесь в корне сайта", 200
#
#
# @app.errorhandler(404)
# def error_404(error):
#     return "Страничка не найдена :("
