from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return f"Вы находитесь в корне сайта", 200

@app.errorhandler(404)
def error_404(error):
    return "Страничка не найдена :("