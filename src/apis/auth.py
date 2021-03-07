from functools import wraps

from flask import jsonify, request
from flask_jwt_extended import (
    JWTManager, verify_jwt_in_request, get_jwt_claims, get_jwt_identity,
    jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    set_access_cookies, set_refresh_cookies, unset_jwt_cookies
)
from flask_restful import Resource, reqparse

from database import db
from models import User, UserSchema


parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("password", type=str)
parser.add_argument("email", type=str)

jwt = JWTManager()


class Auth(Resource):

    def post(self):
        args = parser.parse_args()
        print("==============")
        print(args)
        print(type(args))
        print(vars(args))
        print("==============")
        user = User(args.name,
                    args.email,
                    args.password)
        print("==============")
        print(vars(user))
        print("==============")
        db.session.add(user)
        db.session.commit()
        json_data = UserSchema().dump(user)
        return jsonify(json_data)

    def put(self):
        args = parser.parse_args()
        print(args.get("email"))
        user = User.query.filter(User.email == args.email).one_or_none()

        print("-------------------------")
        print(vars(user))
        print("-------------------------")

        if user is None:
            # TODO: 401を返却する
            pass

        if user.check_password(args.password):
            access_token = create_access_token(identity=args.email)
            # login成功
            return jsonify(access_token=access_token)
