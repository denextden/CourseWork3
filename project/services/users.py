import jwt
from flask_restx import abort

from project.dao.users import UserDAO
from project.dao.auth import AuthDao
from project.services.base import BaseService
from project.services.auth import AuthService
from flask import current_app


class UserService(BaseService):
    def get_user(self, token):
        data = jwt.decode(jwt=token, key=current_app.config['SECRET_KEY'],
                          algorithms=current_app.config['JWT_ALGO'])
        email = data.get("email")
        user = AuthDao(self._db_session).get_user_by_email(email=email, self=self)
        return user

    def get_user_for_update(self, token):
        data = jwt.decode(jwt=token, key=current_app.config['SECRET_KEY'],
                          algorithms=current_app.config['JWT_ALGO'])
        email = data.get("email")
        user = AuthDao(self._db_session).get_user_by_email2(email=email, self=self)
        return user

    def update_user(self, data, token):
        user = self.get_user_for_update(token)
        return UserDAO(self._db_session).update_user(user=user, data=data)

    def update_passwords(self, password_1, password_2, token):
        user = self.get_user_for_update(token)
        password_1_hash = AuthService.get_hash(password_1)
        if not AuthService.compare_passwords(password_1_hash, user.password_hash):
            abort(400)
        password_2_hash = AuthService.get_hash(password_2)
        return UserDAO(self._db_session).update_password(password_hash=password_2_hash, user=user)
