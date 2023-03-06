from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


# Форма регистарции пользователя
class UserRegisterForm(FlaskForm):
    first_name = StringField("Имя", [validators.DataRequired()])
    last_name = StringField("Фамилия", [validators.DataRequired()])
    email = StringField("Почта", [validators.DataRequired(), validators.Email(message="Неправильный ввод Email-адресса")])
    password = PasswordField("Пароль", [validators.DataRequired(), validators.EqualTo("confirm_password", message="Пароли не совпадают")])
    confirm_password = PasswordField("Повторите пароль", [validators.DataRequired()])

    submit = SubmitField('Регистрация')
