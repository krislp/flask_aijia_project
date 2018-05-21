
SUCCESS = {'code': 200, 'msg': '请求成功'}

# 用户模块
USER_REGISTER_PARAMS_ERROR = {'code':  1000, 'msg': '注册信息参数填写不完整'}
USER_REGISTER_PHONE_ERROR = {'code': 1001, 'msg': '手机号码有误'}
USER_REGISTER_PHONE_IS_EXSITS = {'code': 1002, 'msg': '该手机号码已经被注册'}
USER_REGISTER_PASSWORD_IS_NOT_EQUAL = {'code': 1003, 'msg': '两次密码输入不一致'}
USER_REGISTER_DATABASE_ERROR = {'code': 1004, 'msg': '数据库请求不成功'}

USER_LOGIN_PARAMS_ERROR = {'code': 1005, 'msg': '登陆信息参数填写不完整'}
USER_LOGIN_PHONE_ERROR = {'code': 1006, 'msg': '手机号有误'}
USER_LOGIN_USER_IS_NOT_EXSITS = {'code': 1007, 'msg': '用户不存在'}
USER_LOGIN_PASSWORD_ERROR = {'code': 1008, 'msg': '密码错误'}