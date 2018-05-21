from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from utils.functions import db


class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def add_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(BaseModel, db.Model):

    __tablename__ = 'ihome_user'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11), unique=True)
    pwd_hash = db.Column(db.String(200))
    name = db.Column(db.String(30), unique=True)
    avatar = db.Column(db.String(100))  # 头像
    id_name = db.Column(db.String(30))  # 实名认证姓名
    id_card = db.Column(db.String(18), unique=True)  # 实名认证身份证号码

    @property
    def password(self):
        """读取密码"""
        return ''

    @password.setter
    def password(self, pwd):
        """给密码加密存入数据库"""
        self.pwd_hash = generate_password_hash(pwd)

    def check_password(self, pwd):
        """校验密码"""
        return check_password_hash(self.pwd_hash, pwd)

    def to_basic_dict(self):
        """json格式返回用户信息"""
        return {
                'id': self.id,
                'name': self.name,
                'phone': self.phone,
                'avatar': self.avatar if self.avatar else ''
        }