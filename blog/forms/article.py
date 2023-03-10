from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, validators, TextAreaField


class ArticleCreateForm(FlaskForm):
    title = StringField("Загаловок", [validators.DataRequired()])
    text = TextAreaField("Содержание", [validators.DataRequired()])

    submit = SubmitField('Создать')