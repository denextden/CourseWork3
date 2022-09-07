from flask_restx import Namespace, Resource, abort

from project.dao.serealization.auth import AuthRegisterRequest
from project.setup_db import db
from project.services.auth import AuthService
from flask import request

auth_ns = Namespace('auth')


@auth_ns.route("/register/")
class RegisterView(Resource):
    def post(self):
        data = request.json
        new_data = AuthRegisterRequest().load(data)
        AuthService(db.session).register(
            email=new_data['email'],
            password=new_data['password'],
        )
        return "", 200


@auth_ns.route("/login/")
class LoginView(Resource):
    def post(self):
        data = request.json
        new_data = AuthRegisterRequest().load(data)
        tokens = AuthService(db.session).login(
            email=new_data['email'],
            password=new_data['password'],
        )
        return tokens, 200

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token')
        if refresh_token is None:
            abort(400)
        tokens = AuthService(db.session).refresh_token(refresh_token)
        return tokens, 200


# from typing import Dict
#
# from flask_restx import Resource, Namespace, fields
# from project.container import auth_service
# from flask import request
#
# from project.dao.serealization.auth import AuthRegisterRequest
#
# auth_ns = Namespace('auth')
#
# docs_models = auth_ns.model('AuthRegisterRequest', {
#     'email': fields.String,
#     'password': fields.String
# })
#
# output_model = auth_ns.model('TokensResponse', {
#     'access_token': fields.String,
#     'refresh_token': fields.String
# })
#
#
# @auth_ns.route('register/')
# class RegisterView(Resource):
#     @auth_ns.expect(docs_models)
#     def post(self):
#         data = request.json
#         validated_data = AuthRegisterRequest().load(data)
#
#         auth_service.register(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#
#         return '', 200
#
#
# @auth_ns.route('/login/')
# class LoginView(Resource):
#     @auth_ns.expect(200, descriprion='Токены для авторизации', model=output_model)
#     def post(self):
#         data = request.json
#         validated_data = AuthRegisterRequest().load(data)
#
#         tokens: Dict[str, str] = auth_service.login(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#
#         return tokens, 200
#
