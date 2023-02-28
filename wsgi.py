from flask import redirect
from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.models.database import db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("done!")


@app.cli.command('delete-db')
def init_db():
    db.drop_all()
    print("done!")


@app.cli.command('create-users')
def create_users():
    from blog.models import User
    user1 = User(id=1, user_name="Dima", email='dm@yandex.ru', is_staff=True, password=generate_password_hash('Dima'))
    user2 = User(id=2, user_name="Anna", email='neAnna@mail.ru', is_staff=False,
                 password=generate_password_hash('Anna'))
    user3 = User(id=3, user_name="Viva", email='viva@google.com', is_staff=False,
                 password=generate_password_hash('Viva'))

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    print(f"done! create users: {user1.user_name}, {user2.user_name}, {user3.user_name}")


@app.cli.command('create-articles')
def create_users():
    from blog.models import Articles
    article1 = Articles(id=1, author=1, title='Как жить?', text="Никак :(")
    article2 = Articles(id=2, author=2, title='Лучшие люди', text="Все!")

    db.session.add(article1)
    db.session.add(article2)
    db.session.commit()

    print(f"done! create articles: {article1.title}, {article2.title}")

@app.route('/', methods=["GET"])
def index():
    return redirect('/auth'), 200
