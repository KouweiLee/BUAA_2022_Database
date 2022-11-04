import os.path

from django.views import View
from utils.sqlHelper import SqlHelper
from django.http import JsonResponse
from utils.funcs import *
from utils.Def import *


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
            ares = sqlHelper.select(TB_HOMEWORK, cond_dict={"id": id}, all=True)[0]
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
            sqlHelper.update(TB_HOMEWORK, attr_dict, {"id": id})
            res['code'] = 200
        except Exception as e:
            print("Error: ", e)
            res['msg'] = "修改作业失败"
        return JsonResponse(res)


class DeleteWork(View):
    """删除作业信息
    """

    def post(self, request):
        res = {'code': 400, 'msg': '删除作业成功', 'data': []}
        request = getRequest(request)
        id = request.get("id")  # 作业id
        try:
            sqlHelper = SqlHelper()
            sqlHelper.delete(TB_HOMEWORK, {"id": id})
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
                dic = {"id": ares[0],
                       "name": ares[1]}
                res['data'].append(dic)
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "获取所有作业失败"
        return JsonResponse(res)


class UploadWork(View):
    """用户上传自己的作业
    """

    def post(self, request):
        res = {'code': 400, 'msg': '上传作业成功', 'data': []}
        try:
            file = request.FILES.get('file')
            username = request.POST.get('username')
            homework_id = request.POST.get('homework_id')
            head_path = HOMEWORK_ROOT
            print("head_path", head_path)
            if not os.path.exists(head_path):
                os.makedirs(head_path)
            # 文件名由username和homework_id来组成
            file_name = username + "_" + homework_id + file.name.split(".")[1]
            file_path = head_path + "\\" + file_name
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            sqlHelper = SqlHelper()
            sqlHelper.executeProcedure()
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "上传作业失败"
        return JsonResponse(res)


"""
def upload(request):
    # 获取相对路径
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if request.method == 'POST':
        file = request.FILES.get('file', None)
        # 设置文件上传文件夹
        head_path = BASE_DIR + "\\upload\\json"
        print("head_path", head_path)
        # 判断是否存在文件夹, 如果没有就创建文件路径
        if not os.path.exists(head_path):
            os.makedirs(head_path)
        file_suffix = file.name.split(".")[1]  # 获取文件后缀
        # 储存路径
        file_path = head_path + "\\{}".format("head." + file_suffix)
        file_path = file_path.replace(" ", "")
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        message = {}
        message['code'] = 200
        # 返回图片路径
        message['fileurl'] = file_path
        return JsonResponse(message)
"""""
