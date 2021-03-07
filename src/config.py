import os


class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = \
        "mysql+pymysql://{}:{}@{}/{}?charset=utf8".format(
            os.getenv('MYSQL_USER'),
            os.getenv('MYSQL_PASSWORD'),
            os.getenv('DATABASE_CONTAINER_NAME'),
            os.getenv('MYSQL_DATABASE'),
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
