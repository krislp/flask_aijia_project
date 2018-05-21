
### 登陆接口

#### request请求
    POST /user/login

##### params参数：
    mobile 手机号码
    password 密码

#### response响应

##### 失败响应1：
    {
        'code': 1005,
        'msg': '登陆信息参数填写不完整'
    }

##### 失败响应2：
    {
        'code': 1006,
        'msg': '手机号有误'
    }

##### 失败响应3：
    {
        'code': 1007,
        'msg': '用户不存在'
    }

##### 失败响应4：
    {
        'code': 1008,
        'msg': '密码错误'
    }