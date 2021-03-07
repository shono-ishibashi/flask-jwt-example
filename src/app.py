from flask import Flask, jsonify
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from flask_restful import Api

from apis import auth, test_api
from database import init_db

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object("config.Config")

# TODO: 変更する
app.config["JWT_SECRET_KEY"] = "super-secret"

jwt = JWTManager(app)

# dbの初期化
init_db(app)


@app.route('/')
def hello_world():
    data = {"message": "hello world edited"}
    return jsonify(data)


api = Api(app)
api.add_resource(test_api.TestAPI, "/test")
api.add_resource(auth.Auth, "/auth")

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
