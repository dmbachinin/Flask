from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from blog.models.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(80), nullable=False)
    email = Column(String(255), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    articles = relationship("Articles")

    def __repr__(self):
        return f"<USER {self.id} - {self.user_name}>"

