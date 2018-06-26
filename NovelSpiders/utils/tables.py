from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base

import datetime

Base = declarative_base()


class Novel(Base):
    __tablename__ = 'novel'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(64))
    type = Column('type', String(32))
    author = Column('author', String(32))
    status = Column('status', String(16))
    background = Column('background', String(128))
    length = Column('length', Integer)
    last_update = Column('last_update', DateTime)
    content = Column('content', Text)

    def change_item_to_cow(self, item):
        self.id = int(item['id'])
        self.title = item['title']
        self.type = item['type']
        self.author = item['author']
        self.status = item['status']
        self.background = item['background']
        self.length = int(item['length'])
        self.last_update = datetime.datetime.strptime(item['last_update'], "%Y-%m-%d %H:%M:%S")
        self.content = item['content']

    def update_novel(self, new_novel):
        self.title = new_novel.title
        self.type = new_novel.type
        self.author = new_novel.author
        self.status = new_novel.status
        self.background = new_novel.background
        self.length = new_novel.length
        self.last_update = new_novel.last_update
        self.content = new_novel.content
