from django.views import View
from utils.sqlHelper import SqlHelper
from django.http import JsonResponse
from utils.funcs import *
from utils.Def import *


class GetAllCourses(View):
    def post(self, request):
        res = {'code': 400, 'msg': '获取全部课程成功', 'data': []}
        request = getRequest(request)
        username = request.get("username")
        try:
            sqlHelper = SqlHelper()
            # sql = "select id, name from cl_class where id in " \
            #       "(select class_id from cl_class_user where username = \'%s\')" % username
            # results = sqlHelper.executeSql(sql)
            results = sqlHelper.executeProcedure("selectAllClasses", [username, True])

            for ares in results:
                dic = {"id": ares[0], "name": ares[1], "isChoosed": 1}#用0/1传
                res['data'].append(dic)
            # sql = "select id, name from cl_class where id not in " \
            #       "(select class_id from cl_class_user where username = \'%s\')" % username
            # results = sqlHelper.executeSql(sql)
            results = sqlHelper.executeProcedure("selectAllClasses", [username, False])
            for ares in results:
                dic = {"id": ares[0], "name": ares[1], "isChoosed": 0}#用0/1传
                res['data'].append(dic)
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "获取全部课程失败"
        return JsonResponse(res)


class AddCourse(View):
    def post(self, request):
        res = {'code': 400, 'msg': '添加课程成功', 'data': []}
        request = getRequest(request)
        class_name = request.get("class_name")
        try:
            sqlHelper = SqlHelper()
            sqlHelper.insert('cl_class', {'name': class_name})
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = '添加课程失败'
        return JsonResponse(res)


class ClickCourse(View):
    """点击单个课程时, 传当前课程的所有信息给前端. 也用于点击课程管理栏"""

    def post(self, request):
        res = {'code': 400, 'msg': '进入课程成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        try:
            sqlHelper = SqlHelper()
            ares = sqlHelper.select(CLASS, cond_dict={"id": id}, all=True)[0]
            dic = {"id": ares[0],
                   "name": ares[1],
                   "description": ares[2],
                   "pingshi": ares[3],
                   "exam": ares[4],
                   "time": ares[5],
                   "position": ares[6]}
            res['data'] = dic
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "进入课程失败"
        return JsonResponse(res)


class ChangeCourse(View):
    """
    修改课程, 前端向后端传要修改的内容
    """

    def post(self, request):
        res = {'code': 400, 'msg': '修改课程成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        name = request.get("name")
        time = request.get("time")
        position = request.get("position")
        description = request.get("description")
        exam = int(request.get("exam"))
        pingshi = int(request.get("pingshi"))
        try:
            sqlHelper = SqlHelper()
            attr_dict = {
                "name": name,
                "time": time,
                "position": position,
                "description": description,
                "exam": exam,
                "pingshi": pingshi}
            cond = {"id": id}
            sqlHelper.update(CLASS, attr_dict, cond)
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "修改课程失败"
        return JsonResponse(res)


class DeleteCourse(View):
    """
    删除课程, 前端传id
    """

    def post(self, request):
        res = {'code': 400, 'msg': '删除课程成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        try:
            sqlHelper = SqlHelper()
            sqlHelper.delete(CLASS, {"id": id})
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "删除课程失败"
        return JsonResponse(res)


##########################作业区####################################
class AddWork(View):
    """
    添加作业, 前端传作业名和课程id
    """

    def post(self, request):
        res = {'code': 400, 'msg': '添加作业成功', 'data': []}
        request = getRequest(request)
        name = request.get("name")
        class_id = int(request.get("class_id"))
        try:
            sqlHelper = SqlHelper()
            params = [class_id, name]
            sqlHelper.executeProcedure("addwork", params)
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "添加作业失败"
        return JsonResponse(res)


class ClickWork(View):  # 还未验证
    """
    点击具体作业, 前端向后端传作业id, 后端返回该作业的具体信息
    """

    def post(self, request):
        res = {'code': 400, 'msg': '点击具体作业成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        try:
            sqlHelper = SqlHelper()
            ares = sqlHelper.select(HOMEWORK, cond_dict={"id": id}, all=True)[0]
            res['data'] = {"id": ares[0],
                           "name": ares[1],
                           "content": ares[2],
                           "begin_time": ares[3],
                           "end_time": ares[4]}
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "点击具体作业失败"
        return JsonResponse(res)


class ChangeWork(View):
    """修改作业
    """

    def post(self, request):
        res = {'code': 400, 'msg': '修改作业成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        name = request.get("name")
        begin_time = request.get("begin_time")
        end_time = request.get("end_time")
        content = request.get("content")
        try:
            sqlHelper = SqlHelper()
            attr_dict = {"name": name,
                         "begin_time": begin_time,
                         "end_time": end_time,
                         "content": content}
            sqlHelper.update(HOMEWORK, attr_dict, {"id": id})
            res['code'] = 200
        except Exception as e:
            print("Error: ", e)
            res['msg'] = "修改作业失败"
        return JsonResponse(res)


class DeleteWork(View):
    def post(self, request):
        res = {'code': 400, 'msg': '删除作业成功', 'data': []}
        request = getRequest(request)
        id = request.get("id")  # 作业id
        try:
            sqlHelper = SqlHelper()
            sqlHelper.delete(HOMEWORK, {"id": id})
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "删除作业失败"
        return JsonResponse(res)

class GetAllWorks(View):
    """获取所有作业
        前端: 课程id
        后端: 所有作业id+姓名
    """
    def post(self, request):
        res = {'code': 400, 'msg': '获取所有作业成功', 'data': []}
        request = getRequest(request)
        class_id = int(request.get("id"))
        try:
            sqlHelper = SqlHelper()
            results = sqlHelper.executeProcedure("selectAllWorks", [class_id])
            for ares in results:
                dic = {"id":ares[0],
                       "name":ares[1]}
                res['data'].append(dic)
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "获取所有作业失败"
        return JsonResponse(res)