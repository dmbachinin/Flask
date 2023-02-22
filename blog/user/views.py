from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix="/users", static_folder="../static")

USERS = ['Dima', 'Anna', 'Sasha', 'Anton']


@user.route('/')
def user_list():
    return render_template("users/list.html", users=USERS)


@user.route('/<pk>')
def get_users(pk: int):
    return f"{pk}"
