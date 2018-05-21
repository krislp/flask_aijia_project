import redis

from utils.settings import SQLALCHEMY_DATABASE_URI


class Config():

    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session 配置
    SECRET_KEY = '<111111>'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379)
    SESSION_KEY_PREFIX = 's_aj_'
