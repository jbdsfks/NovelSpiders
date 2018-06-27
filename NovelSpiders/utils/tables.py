from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
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
    url = Column('url', String(128))

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
        self.url = item['url']

    def update_novel(self, new_novel):
        self.title = new_novel.title
        self.type = new_novel.type
        self.author = new_novel.author
        self.status = new_novel.status
        self.background = new_novel.background
        self.length = new_novel.length
        self.last_update = new_novel.last_update
        self.content = new_novel.content
        self.url = new_novel.url


class Chapter(Base):
    __tablename__ = 'chapter'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(64))
    novel_id = Column('novel_id', Integer, ForeignKey('novel.id'))
    content = Column('content', Text)
    url = Column('url', String(128))

    def change_item_to_cow(self, item):
        self.id = int(item['id'])
        self.name = item['name']
        self.novel_id = int(item['novel_id'])
        self.content = item['content']
        self.url = item['url']

    def update_chapter(self, new_chapter):
        self.id = new_chapter.id
        self.novel_id = new_chapter.novel_id
        self.name = new_chapter.name
        self.content = new_chapter.content
        self.url = new_chapter.url
