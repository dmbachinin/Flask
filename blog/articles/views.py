from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.forms.article import ArticleCreateForm
from blog.models import Articles, Author, Tag
from blog.models.database import db
from blog.models.tag import article_tag_associations_table

article = Blueprint('article', __name__, url_prefix="/article", static_folder="../static")


@article.route('/list', methods=["GET"])
def article_list():
    return render_template("articles/list.html", articles=Articles.query.all())


@article.route('/', methods=["GET"])
@login_required
def article_create_form():
    form = ArticleCreateForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    return render_template("articles/create.html", form=form)

@article.route('/', methods=["POST"])
@login_required
def article_create():
    form = ArticleCreateForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if form.validate_on_submit():
        _article = Articles(title=form.title.data, text=form.text.data)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tags.append(tag)

        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)

        _article.author_id = current_user.id
        db.session.add(_article)

        db.session.commit()

        return redirect(url_for("article.article_current", pk=_article.id))

    return redirect(url_for("article.article_create_form"))



@article.route('/list/<int:pk>')
def article_current(pk: int):
    current_article = Articles.query.filter_by(id=pk).options(joinedload(Articles.tags)).one_or_none()
    if current_article:
        return render_template("articles/current.html", article=current_article)
    raise NotFound(f"Article with id = {pk} not found")

@article.route('/list/tag/<string:tag_name>')
def article_by_tag(tag_name: str):
    tag = Tag.query.filter_by(name=tag_name).one_or_none()
    if tag:
        all_article = Articles.query.all()
        article_with_tag = []
        for article in all_article:
            if tag in article.tags:
                article_with_tag.append(article)

        return render_template("articles/list.html", articles=article_with_tag)
    # raise NotFound(f"Article with tag = {tag_name} not found")
    raise NotFound(f"Tag with name = {tag_name} not found")
