from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import User


user = Blueprint('user', __name__, url_prefix="/users", static_folder="../static")



@user.route('/')
@login_required
def users_list():
    return render_template("users/list.html", users=User.query.all())


@user.route('/<int:pk>')
@login_required
def get_user(pk: int):
    _user_correct = User.query.filter_by(id=pk).one_or_none()
    if not _user_correct:
        raise NotFound(f"User with id = {pk} not found")
    return render_template("users/profile.html", user=_user_correct)


