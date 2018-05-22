import functools

from flask import session, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_database_uri(DATABASE):
    db = DATABASE.get('db')
    driver = DATABASE.get('driver')
    user = DATABASE.get('user')
    password = DATABASE.get('password')
    host = DATABASE.get('host')
    port = DATABASE.get('port')
    name = DATABASE.get('name')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver, user, password, host, port, name)


def init_ext(app):

    db.init_app(app=app)


def is_login(view_fun):
    """
    装饰器
    验证是否登陆
    """
    @functools.wraps(view_fun)
    def decorator():
        try:
            if session['user_id']:
                return view_fun()
            else:
                return redirect('/user/login/')
        except:
            return redirect('/user/login/')
    return decorator
