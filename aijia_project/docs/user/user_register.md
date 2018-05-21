### 注册接口

#### request请求
    POST /user/register

##### params参数:
    mabile str 电话号码
    password 密码
    password2 确认密码

#### response响应
##### 失败响应1：
    {
        'code':  1000,
        'msg': '注册信息参数填写不完整'
    }

##### 失败响应2：
    {
        'code': 1001,
        'msg': '手机号码有误'
    }

##### 失败响应3：
    {
        'code': 1002,
        'msg': '该手机号码已经被注册'
    }

##### 失败响应4：
    {
        'code': 1003,
        'msg': '两次密码输入不一致'
    }

##### 失败响应5：
    {
        'code': 1004,
        'msg': '数据库请求不成功'
    }

