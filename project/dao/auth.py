from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.user import User
from project.dao.serealization.auth import AuthUserSchema


class AuthDao():
    def __init__(self, session: scoped_session):
        self._db_session = session

    def create(self, email: str, password_hash: str):
        new_user = User(email=email, password_hash=password_hash)
        self._db_session.add(new_user)
        self._db_session.commit()

        return AuthUserSchema().dump(new_user)

    @staticmethod
    def get_user_by_email(self, email: str):
        user = self._db_session.query(User).filter(User.email == email).one_or_none()
        if user is not None:
            return AuthUserSchema().dump(user)

        return None

    @staticmethod
    def get_user_by_email2(self, email: str):
        user = self._db_session.query(User).filter(User.email == email).one_or_none()
        if user is not None:
            return user

        return None

