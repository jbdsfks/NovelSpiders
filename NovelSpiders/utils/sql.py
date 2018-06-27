# _*_encoding:utf-8_*_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Novel, Chapter


class Sql():

    def __init__(self):
        self.engine = create_engine('mysql+mysqldb://lzj:jbdsfks@localhost:3306/novel?charset=utf8', encoding='utf-8')
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def save_novel(self, item, spider):

        novel = Novel()
        novel.change_item_to_cow(item)

        try:
            old_novel = self.session.query(Novel).filter(Novel.id == novel.id).first()
            if old_novel:
                old_novel.update_novel(new_novel=novel)
            else:
                self.session.add(novel)
            self.session.commit()
        except Exception, e:
            spider.logger.error(e)
            self.session.rollback()
        finally:
            self.session.close()

    def save_chapter(self, item, spider):

        chapter = Chapter()
        chapter.change_item_to_cow(item)

        try:
            old_chapter = self.session.query(Chapter).filter(Chapter.id == chapter.id).first()
            if old_chapter:
                old_chapter.update_chapter(new_chapter=chapter)
            else:
                self.session.add(chapter)
            self.session.commit()
        except Exception, e:
            spider.logger.error(e)
            self.session.rollback()
        finally:
            self.session.close()



