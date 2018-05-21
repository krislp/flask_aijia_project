import re

from flask import Blueprint, render_template, request, jsonify, session

from app.models import db, User
from utils import status_code

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
def index():
    return 'Hello World!'


@user_blueprint.route('/createtable/')
def create_table():
    db.create_all()
    return '创建数据库成功'

'''
请求注册页面
'''
@user_blueprint.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')


'''
用户注册
'''
@user_blueprint.route('/register/', methods=['POST'])
def user_regist():
    regist_dict = request.form

    phone = regist_dict.get('mobile')
    pwd = regist_dict.get('password')
    pwd2 = regist_dict.get('password2')

    if not all([phone, pwd, pwd2]):
        """验证注册参数是否填写完整"""
        return jsonify(status_code.USER_REGISTER_PARAMS_ERROR)

    if not re.match(r'^1[345789]\d{9}$', phone):
        """验证手机号码是否正确"""
        return jsonify(status_code.USER_REGISTER_PHONE_ERROR)

    if User.query.filter(User.phone == phone).count():
        """验证手机号码是否已经注册"""
        return jsonify(status_code.USER_REGISTER_PHONE_IS_EXSITS)

    if pwd != pwd2 :
        """验证两次输入的密码是否一致"""
        return jsonify(status_code.USER_REGISTER_PASSWORD_IS_NOT_EQUAL)

    user = User()
    user.phone = phone
    user.name = phone
    user.password = pwd
    try:
        user.add_update()
    except Exception as e:
        return jsonify(status_code.USER_REGISTER_DATABASE_ERROR)

    return jsonify(status_code.SUCCESS)


'''
请求登陆页面
'''
@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


'''
用户登陆
'''
@user_blueprint.route('/login/', methods=['POST'])
def user_login():
    login_dict = request.form

    phone = login_dict.get('mobile')
    password = login_dict.get('password')

    if not all([phone, password]):
        return jsonify(status_code.USER_LOGIN_PARAMS_ERROR)

    if not re.match(r'^1[345789]\d{9}$', phone):
        return jsonify(status_code.USER_LOGIN_PHONE_ERROR)

    user = User.query.filter(User.phone == phone).first()
    if user:
        if user.check_password(password):
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.USER_LOGIN_PASSWORD_ERROR)
    else:
        return jsonify(status_code.USER_LOGIN_USER_IS_NOT_EXSITS)


"""个人中心页面"""
@user_blueprint.route('/my/', methods=['GET'])
def my():
    return render_template('my.html')


"""获取登陆用户信息"""
@user_blueprint.route('/user/', methods=['GET'])
def get_user_profile():

    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()

    return jsonify(user=user.to_basic_dict(), code=200)


"""修改个人信息"""
@user_blueprint.route('/profile/', methods=['GET'])
def profile():
    return render_template('profile.html')


"""获取修改信息"""
@user_blueprint.route('/user/', methods=['PUT'])
def user_profile():

    profile_dict = request.files

    if 'avatar' in profile_dict:
        f1 = profile_dict('avatar')
        if re.match(r'^image/*$', f1.filename):
            avatar = ''
    return profile_dict
