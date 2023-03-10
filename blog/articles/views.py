from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.forms.article import ArticleCreateForm
from blog.models import Articles, Author
from blog.models.database import db

article = Blueprint('article', __name__, url_prefix="/article", static_folder="../static")


@article.route('/list', methods=["GET"])
def article_list():
    return render_template("articles/list.html", articles=Articles.query.all())


@article.route('/', methods=["GET"])
@login_required
def article_create_form():
    form = ArticleCreateForm(request.form)
    return render_template("articles/create.html", form=form)

@article.route('/', methods=["POST"])
@login_required
def article_create():
    form = ArticleCreateForm(request.form)
    if form.validate_on_submit():
        _article = Articles(title=form.title.data, text=form.text.data)
        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)

        _article.author_id = current_user.id
        db.session.add(_article)

        db.session.commit()

        return redirect(url_for("article.article_current", pk=_article.id))

    return render_template("articles/create.html", form=form)



@article.route('/list/<int:pk>')
def article_current(pk: int):
    current_article = Articles.query.filter_by(id=pk).one_or_none()
    if current_article:
        return render_template("articles/current.html", article=current_article)
    raise NotFound(f"Article with id = {pk} not found")
