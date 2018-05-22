from flask import Blueprint, render_template, session, jsonify, request, abort

from app.models import User, Area, Facility, House
from utils import status_code
from utils.functions import is_login

house_blueprint = Blueprint('house', __name__)


"""
我的房源页面
"""
@house_blueprint.route('/myhouse/', methods=['GET'])
@is_login
def myhouse():
    return render_template('myhouse.html')


"""
验证是否实名认证
"""
@house_blueprint.route('/auth_house/', methods=['GET'])
def auth_house():
    user = User.query.get(session['user_id'])

    if user.id_card:
        return jsonify(status_code.USER_HAD_AUTH)
    else:
        return jsonify(status_code.USER_IS_NOT_AUTH)


"""
添加新房源页面
"""
@house_blueprint.route('/newhouse/', methods=['GET'])
def new_house():
    return render_template('newhouse.html')


"""
获取所有城区、设备信息
"""
@house_blueprint.route('/area_facility/', methods=['GET'])
def area_facility():
    areas = Area.query.all()
    area_list = [area.to_dict() for area in areas]

    facilitys = Facility.query.all()
    facility_list = [facility.to_dict() for facility in facilitys]

    return jsonify(area_list=area_list, facility_list=facility_list)


"""
发布房源信息
"""
@house_blueprint.route('/newhouse/', methods=['POST'])
def user_new_house():
    new_house_dict = request.form

    # 创建house
    house = House()
    house.title = new_house_dict['title']
    house.price = new_house_dict['price']
    house.area_id = new_house_dict['area_id']
    house.address = new_house_dict['address']
    house.room_count = new_house_dict['room_count']
    house.acreage = new_house_dict['acreage']
    house.unit = new_house_dict['unit']
    house.capacity = new_house_dict['capacity']
    house.beds = new_house_dict['beds']
    house.deposit = new_house_dict['deposit']
    house.min_days = new_house_dict['min_days']
    house.max_days = new_house_dict['max_days']

    # 判断数据是否填写完整

    # 创建
    try:
        house.add_update()
    except:
        return jsonify(status_code.ERRORS)

    # 创建ihome_house_facility
    facility_ids = new_house_dict['facilites']
    for facility_id in facility_ids:
        facility = Facility.query.get(facility_id)
        house.facilities.add(facility)
        house.add_update()

    return jsonify(status_code.SUCCESS)

