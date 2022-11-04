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
                dic = {"id": ares[0], "name": ares[1], "isChoosed": 1}  # 用0/1传
                res['data'].append(dic)
            # sql = "select id, name from cl_class where id not in " \
            #       "(select class_id from cl_class_user where username = \'%s\')" % username
            # results = sqlHelper.executeSql(sql)
            results = sqlHelper.executeProcedure("selectAllClasses", [username, False])
            for ares in results:
                dic = {"id": ares[0], "name": ares[1], "isChoosed": 0}  # 用0/1传
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


class ChooseCourse(View):
    def post(self, request):
        res = {'code': 400, 'msg': '选课成功', 'data': []}
        request = getRequest(request)
        username = request.get("username")
        class_id = int(request.get("class_id"))
        try:
            sqlHelper = SqlHelper()
            sqlHelper.insert(CLASS_USER, {"username": username, "class_id": class_id})
            res['code'] = 200
        except Exception as e:
            putError(e)
            res['msg'] = "选课失败"
        return JsonResponse(res)