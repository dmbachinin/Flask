from sqlalchemy import Column, Integer, String, Text, ForeignKey
from blog.models.database import db


class Articles(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author = Column(Integer, ForeignKey("users.id"))
    title = Column(String(80))
    text = Column(Text)

    def __repr__(self):
        return f"<ARTICLE {self.author} - {self.title}>"
