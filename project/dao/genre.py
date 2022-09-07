from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(Genre).filter(Genre.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(Genre).all()

# from project.dao.models.genre import Genre
#
#
# class GenreDAO:
#     def __init__(self, session):
#         self.session = session
#
#     def get_one(self, bid):
#         return self.session.query(Genre).get(bid)
#
#     def get_all(self):
#         return self.session.query(Genre).all()
#
#     def create(self, genre_d):
#         ent = Genre(**genre_d)
#         self.session.add(ent)
#         self.session.commit()
#         return ent
#
#     def delete(self, rid):
#         genre = self.get_one(rid)
#         self.session.delete(genre)
#         self.session.commit()
#
#     def update(self, genre_d):
#         genre = self.get_one(genre_d.get("id"))
#         genre.name = genre_d.get("name")
#
#         self.session.add(genre)
#         self.session.commit()
