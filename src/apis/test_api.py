from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
import polyline


from models import Test, TestSchema, User, UserSchema
from database import db


class TestAPI(Resource):
    """
    動作確認用のクラス
    TODO: 削除する
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        super(TestAPI, self).__init__()

    @jwt_required
    def get(self):
        print(get_jwt_identity())
        results = Test.query.all()
        json_data = TestSchema(many=True).dump(results)
        return jsonify({"tests": json_data})

    def post(self):
        test = Test("日本語テスト")
        db.session.add(test)
        db.session.commit()
        res = TestSchema().dump(test)
        return res, 201

    def delete(self):
        endoded_route = polyline.encode(
            [(38.5, -120.2), (40.7, -120.9), (43.2, -126.4)], 5)
        return endoded_route

    def test_exaple(self):
        pass
