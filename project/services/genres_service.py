from project.dao import GenreDAO
from project.exceptions import ItemNotFound
from project.dao.serealization.genre import GenreSchema
from project.services.base import BaseService


class GenresService(BaseService):
    def get_item_by_id(self, pk):
        genre = GenreDAO(self._db_session).get_by_id(pk)
        if not genre:
            raise ItemNotFound
        return GenreSchema().dump(genre)

    def get_all_genres(self):
        genres = GenreDAO(self._db_session).get_all()
        return GenreSchema(many=True).dump(genres)

# from typing import Optional
#
# from project.dao.base import BaseDAO
# from project.exceptions import ItemNotFound
# from project.models import Genre
#
#
# class GenresService:
#     def __init__(self, dao: BaseDAO) -> None:
#         self.dao = dao
#
#     def get_item(self, pk: int) -> Genre:
#         if genre := self.dao.get_by_id(pk):
#             return genre
#         raise ItemNotFound(f'Genre with pk={pk} not exists.')
#
#     def get_all(self, page: Optional[int] = None) -> list[Genre]:
#         return self.dao.get_all(page=page)


# from project.dao.genre import GenreDAO
#
#
# class GenreService:
#     def __init__(self, dao: GenreDAO):
#         self.dao = dao
#
#     def get_one(self, bid):
#         return self.dao.get_one(bid)
#
#     def get_all(self):
#         return self.dao.get_all()
#
#     def create(self, genre_d):
#         return self.dao.create(genre_d)
#
#     def update(self, genre_d):
#         self.dao.update(genre_d)
#         return self.dao
#
#     def delete(self, rid):
#         self.dao.delete(rid)
