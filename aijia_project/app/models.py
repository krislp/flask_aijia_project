from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from utils.functions import db


"""
基础模型
"""
class BaseModel(object):
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def add_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


"""
用户模型
"""
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


ihome_house_facility = db.Table(
    'ihome_house_facility',
    db.Column('house_id', db.Integer, db.ForeignKey('ihome_house.id'), primary_key=True),
    db.Column('facility_id', db.Integer, db.ForeignKey('ihome_facility.id'), primary_key=True)
    )


"""
发布房屋模型
"""
class House(BaseModel, db.Model):

    __tablename__ = 'ihome_house'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('ihome_user.id'), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('ihome_area.id'), nullable=False)
    title = db.Column(db.String(64), nullable=False)  # 标题
    price = db.Column(db.Integer, default=0)  # 房间单价
    address = db.Column(db.String(512), default='')  # 房间地址
    room_count = db.Column(db.Integer, default=1)  # 房间数目
    acreage = db.Column(db.Integer, default=0)  # 房屋面积
    unit = db.Column(db.String(32), default='')  # 房屋套型 几室几厅
    capacity = db.Column(db.Integer, default=1)  # 房屋容纳人数
    beds = db.Column(db.String(64), default='')  # 床铺配置
    deposit = db.Column(db.Integer, default=0)  # 押金
    min_days = db.Column(db.Integer, default=1)  # 最少入住天数
    max_days = db.Column(db.Integer, default=0)  # 最多入住天数 0表示不限制
    order_count = db.Column(db.Integer, default=0)  # 预定完成的房屋数量
    index_image_url = db.Column(db.String(256), default='')  # 房屋主图片的路径

    facilities = db.relationship('Facility', secondary=ihome_house_facility)
    images = db.relationship('HouseImage')
    orders = db.relationship('Order', backref='house')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.index_image_url if self.index_image_url else '',
            'area': self.area.name,
            'price': self.price,
            'create_time': self.create_time,
            'room': self.room_count,
            'order_count': self.order_count,
            'address': self.address
        }

    def to_fill_dict(self):
        return {
            'id': self.id,
            'user_avatar': self.user.avatar if self.user.avatar else '',
            'user_name': self.user.name,
            'title': self.title,
            'price': self.price,
            'address': self.area.name + self.address,
            'room_count': self.room_count,
            'acreage': self.acreage,
            'unit': self.unit,
            'capacity': self.capacity,
            'beds': self.beds,
            'deposit': self.deposit,
            'min_days': self.min_days,
            'max_days': self.max_days,
            'order_count': self.order_count,
            'images': [image.url for image in self.images],
            'facilities': [facility.to_dict() for facility in self.facilities],
        }


"""
房屋图片模型
"""
class HouseImage(BaseModel, db.Model):

    __tablename__ = 'ihome_house_image'

    id = db.Column(db.Integer, primary_key=True)
    house_id = db.Column(db.Integer, db.ForeignKey('ihome_house.id'), nullable=False)
    url = db.Column(db.String(256), nullable=False)


"""
设备信息 房屋规格
"""
class Facility(BaseModel, db.Model):

    __tablename__ = 'ihome_facility'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)  # 设备名称
    css = db.Column(db.String(30), nullable=True)  # 设施展示的图标

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'css': self.css
        }

    def to_house_dict(self):
        return {'id': self.id}


"""
城区
"""
class Area(BaseModel, db.Model):

    __tablename__ = 'ihome_area'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    houses = db.relationship('House', backref='area')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }


"""
订单模型
"""
class Order(BaseModel, db.Model):

    __tablename__ = 'ihome_order'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("ihome_user.id"), nullable=False)
    house_id = db.Column(db.Integer, db.ForeignKey("ihome_house.id"), nullable=False)
    begin_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    days = db.Column(db.Integer, nullable=False)
    house_price = db.Column(db.Integer, nullable=False)  # 订单总价
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(
        db.Enum(
            'WAIT_ACCEPT',  # 待结单
            'WAIT_PAYMENT',  # 待支付
            'PAID',  # 已支付
            'WAIT_COMMENT'  # 待评价
            'COMPLETE',  # 已完成
            'CANCELED',  # 已取消
        ),
        default='WAIT_ACCEPT', index=True
    )
    comment = db.Column(db.Text)

    def to_dict(self):
        return {
            'order_id': self.od,
            'houser_title': self.house.title,
            'image': self.house.index_image_url if self.house.index_image_url else '',
            'create_date': self.create_time.strftime('%Y-%m-%d'),
            'begin_date': self.begin_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'amount': self.amount,
            'days': self.days,
            'status': self.status,
            'comment': self.comment
        }


