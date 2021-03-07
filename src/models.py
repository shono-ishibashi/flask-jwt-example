import uuid

from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from sqlalchemy_utils import UUIDType
from werkzeug.security import generate_password_hash, check_password_hash

from database import db

ma = Marshmallow()


class Test(db.Model):
    __tabletest__ = "tests"

    id = db.Column(UUIDType(binary=False),
                   primary_key=True, default=uuid.uuid4)
    test = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.test = name


class TestSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Test


class User(db.Model):
    __tabletest__ = "users"

    id = db.Column(UUIDType(binary=False),
                   primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.set_password(password)

    def __dict__(self):
        data = {
            "user_id": self.id,
            "name": self.name_edited,
            "email": self.email
        }
        return data

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password, password)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field()
    test = auto_field()
    email = auto_field()
    password = ma.auto_field(load_only=True)
