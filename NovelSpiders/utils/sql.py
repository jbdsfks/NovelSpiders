# _*_encoding:utf-8_*_
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Novel


class Sql():

    def __init__(self):
        self.engine = create_engine('mysql+mysqldb://lzj:jbdsfks@localhost:3306/novel?charset=utf8', encoding='utf-8')
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def save_novel(self, item):

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
            print e
            self.session.rollback()
        finally:
            self.session.close()



