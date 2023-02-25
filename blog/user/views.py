from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix="/users", static_folder="../static")

USERS = {
    1: 'Dima',
    2: 'Anna',
    3: 'Sasha',
    4: 'Anton'
}


@user.route('/')
def users_list():
    return render_template("users/list.html", users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_correct = USERS[pk]
    except KeyError:
        raise NotFound(f"User with id = {pk} not found")
    return render_template("users/details.html", user=user_correct)


