# 用户区url文档12.3

**未经说明, 后端向前端传的就是和之前一样的东西, 包括200和400等**

已修改登录,  是管理员的就data就返回true, 否则false

### 修改姓名

- [x] http://localhost:8000/login/user/changeName/

* 前端向后端传

```json
{
	username: 用户账号,
	name: 用户名字
}
```

### 修改描述

- [x] http://localhost:8000/login/user/changeProfile/

* 前端向后端传

```
{
	username: 用户账号,
	profile: 用户描述
}
```

### 修改权限

- [ ] http://localhost:8000/login/user/changeSuper/

* 前端向后端传

```
{
	username: 要修改的用户账号,
	isSuperUser: 布尔值, true代表管理员, false代表普通用户
}
```

### 设置头像

- [ ] http://localhost:8000/login/user/setphoto/

* 前端向后端传

```
{
	username: 用户账号,
	photo: 头像的url
}
```

### 修改密码

复用之前的即可.

### 获取用户头像

- [ ] http://localhost:8000/login/user/getphoto/

```
{
	username: 用户账号
}
```

后端返回

```
res = {'code': 400, 'msg': '删除图片成功', 'data': "url"}
```



### 获取用户描述

- [ ] http://localhost:8000/login/user/getprofile/

前端传

```
{
	username: 用户账号
}
```

后端返回:

```
res = {'code': 400, 'msg': '删除图片成功', 'data': "用户描述"}
```

