from flask import Blueprint, render_template, asd

user = Blueprint('user', __name__, url_prefix="/users", static_folder="../static")

USERS = ['Dima', 'Anna', 'Sasha', 'Anton']


@user.route('/')
def user_list():
    return render_template("users/user_list.html")


@user.route('/<pk>')
def get_users(pk: int):
    return f"{pk}"
