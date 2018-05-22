
### 修改头像、用户名接口

#### request请求
    PUT /user/user/

#### params参数：
    avatar 上传图片
    name 用户名

#### response响应

##### 失败响应1：
    {
        'code': 1009,
        'msg': '上传文件类型错误'
    }

##### 失败响应2：
    {
        'code': 1010,
        'msg': '用户名已经存在'
    }

##### 失败响应3：
    {
        'code': 1011,
        'msg': '缺少修改参数'
    }