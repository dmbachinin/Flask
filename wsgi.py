from blog.app import create_app
from blog.models.database import db

app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("done!")


@app.cli.command('create-users')
def create_users():
    from blog.models import User
    user1 = User(id=1, user_name="Dima", email='dm@yandex.ru', is_staff=True)
    user2 = User(id=2, user_name="Anna", email='neAnna@mail.ru', is_staff=False)
    user3 = User(id=3, user_name="Viva", email='viva@google.com', is_staff=False)

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    print(f"done! create users: {user1.user_name}, {user2.user_name}, {user3.user_name}")
