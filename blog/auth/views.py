from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import logout_user, login_user, login_required

from blog.app import login_manager
from blog.models import User

auth = Blueprint('auth', __name__, url_prefix="/auth", static_folder='../static')


@auth.route('/', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template('/auth/login.html')
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('login or password error')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('user.get_user', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@login_manager.user_loader
def user_loader(user_id: int) -> User:
    return User.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))
