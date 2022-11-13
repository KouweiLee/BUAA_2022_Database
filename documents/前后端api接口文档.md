# 前后端api接口文档

## 课程区

### 用户选课

- [x] `http://localhost:8000/course/course/choose/`

  前端向后端传:

  ```
  {
  	username:用户账号,
  	class_id:课程id
  }
  ```

  后端向前端传200/400

### 用户退课

- [ ] `http://localhost:8000/course/course/quit/`

前端向后端传:

```
{
	username:用户账号,
	class_id:课程id
}
```

后端向前端传200/400

### 获取所有课程

- [ ] 已实现用存储过程

- [ ] `http://localhost:8000/course/course/all/`

* 前端向后端传

  ```json
  {
  	username: 用户账号
  }
  ```

* 后端向前端返回

  ```json
  {
      [
      	{
              id:课程id,
              name:课程名称,
              isChoosed:是否已经选课
      	},...,{...}
  	]
  }
  ```

### 添加课程

- [ ] `http://localhost:8000/course/course/addone/`

* 前端向后端传

```
{
	class_name:课程名称
}
```

* 后端返回: 200/400



### 点击单个课程

- [x] `http://localhost:8000/course/course/single/`

* 前端向后端传

```
{
	id: 课程id,
	username: 用户账号
}
```

* 后端返回

```
{
	id: 课程id,
	name: 课程名称,
	isChoosed: false,
	time: "周一???",
	position: "地点",
	description: "markdown渲染",
	exam: 50,
	pingshi: 50
}
```

### 获取所有作业

- [x] http://localhost:8000/course/work/all/


* 前端向后端

```
{
	id:课程id
}
```

* 后端返回

```
{
	[
		{
			id:作业id,
			name: 作业名称
		}...,{}
	]
}
```

### 添加作业

- [x] http://localhost:8000/course/work/addone/


* 前端向后端传

```
{
	name:作业名称,
	class_id:所属课程id
}
```

* 后端返回200/400

### 点击具体作业

- [x] http://localhost:8000/course/work/single/


* 前端向后端传:

```
{
	id:作业id
}
```

* 后端向前端传:

```
{
	id:作业id,
	name: 作业名称,
	content: 作业内容描述,
	begin_time: 作业开始时间(Datatime格式),
	end_time: 作业结束时间.
}
```

### 上传作业

- [x] http://localhost:8000/course/work/upload/

* 前端向后端

```json
{
	username: 用户账号,
    homework_id: 当前所属作业的id
}
```

* 后端向前端200/400

homework_path应该是不要了

### 点击作业管理栏

- [x] http://localhost:8000/course/work/single/


* 前端向后端

```
{
	id: 作业id	
}
```

* 后端向前端传

```
{
	id:作业id,
	name:作业名称,
	begin_time:作业开始时间,
	end_time:作业结束时间,
	content:作业描述
}
```

### 点击确认修改作业按钮

- [x] http://localhost:8000/course/work/change/


* 前端向后端传

```
{
	id:作业id,
	name:作业名称,
    begin_time:作业开始时间,
	end_time:作业结束时间,
	content:作业描述
}
```

* 后端返回200/400

### 点击删除作业按钮

- [x] http://localhost:8000/course/work/delete/

* 前端向后端传

```
{
	id:作业id
}
```

* 后端返回200/400

### 点击作业提交情况(批改作业)按钮

- [x] http://localhost:8000/course/work/correcting/


展示作业的提交列表

* 前端向后端传

```
{
	id:作业类的id
}
```

* 后端向前端返回

```json
{
    id:作业类的id,
    attachments:
    [
	    {
            attachment_id:学生提交的作业附件id,
            username:学生学号,
            name: 学生姓名.
            filename:文件名,
            time:最后提交时间,
            score:分数
    	},...,
    	{...}
    ]
}
```



#### 下载作业压缩包

- [ ] http://localhost:8000/course/work/downloadAll/

```
{
	id: 作业类的id
}
```

此操作会下载所有人提交的作业

#### 下载单个作业

- [ ] http://localhost:8000/course/work/downloadOne/

```
{
	id: 作业附件id
}
```

此操作会下载指定人提交的作业

#### 删除作业记录

- [x] http://localhost:8000/course/work/deleteRecord/


* 前端向后端传:

```
{
	id:作业附件的id
}
```

#### 批改

- [x] http://localhost:8000/course/work/score/


批改会给作业一个分数

* 前端向后端传

```
{
	id:作业附件id,
	score:作业评判分数
}
```

### 点击课程管理按钮

- [x] `http://localhost:8000/course/course/single/`

* 前端向后端传

```
{
	id:课程id
}
```

* 后端向前端传

```
{
	id:课程id,
	name:课程名称,
	time: "周一???",
	position: "地点",
	description: "markdown",
	exam: 50,
	pingshi: 50
}
```

#### 点击修改按钮

- [x] http://localhost:8000/course/course/change/


* 前端向后端传

```
{
	id:课程id,
	name:课程名称,
	time: "周一???",
	position: "地点",
	description: "markdown",
	exam: 50,
	pingshi: 50
}
```

#### 点击删除课程

- [x] http://localhost:8000/course/course/delete/


* 前端向后端传

```
{
	id:课程id
}
```

### 点击课程附件区

- [x] http://localhost:8000/course/attachment/all/


* 前端向后端传

```
{
	id:课程id
}
```

* 后端向前端返回

```
{
	id:课程id,
	attachments:
	[
		{
			attachment_id: 课程附件id,
			name: 材料名称,
			time: 上传时间
		}...,
		{}
	]
}
```

#### 上传课程附件

- [x] http://localhost:8000/course/attachment/upload/


* 前端向后端传

```
{
	class_id: 课程id
}
```

* 后端向前端200/400

#### 下载单个课程附件

- [ ] http://localhost:8000/course/attachment/downloadOne/

* 前端向后端

```
{
	id: 课程附件的id
}
```



#### 删除单个课程附件

- [x] http://localhost:8000/course/attachment/delete/

前端向后端传:

```
{
	id:要删除的课程附件id
}
```



## 代做事项

- [x] cl_homework_user的设计, 若select为空, 则插入insert; 否则, 则update
- [x] 如何获取el-upload的data数据, 直接request.POST.get('username')

- [x] 获取所有课程的时候, 用存储过程获取
- [ ] 增加课程信息

- [x] 存储过程执行的时候是互斥的吗?

是互斥的, 因为并发控制

- [x] 看触发器如何实现添加作业后添加课程??? 好像不大行

存储过程:

* 作业平均分

* 模糊搜索

  <img src="D:/Typora/img/image-20221103202126167.png" alt="image-20221103202126167" style="zoom:33%;" />

触发器:

* 学生选课数, 

* 教师发帖数

* 作业平均分的统计

  <img src="D:/Typora/img/image-20221103202300595.png" alt="image-20221103202300595" style="zoom:33%;" />

* 保证数据完整性, 评论对应的主题帖要存在.

- [ ] 索引
