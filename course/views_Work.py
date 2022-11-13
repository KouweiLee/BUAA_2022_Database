import os.path

from django.views import View
from utils.sqlHelper import SqlHelper
from django.http import JsonResponse
from utils.funcs import *
from utils.Def import *

from rest_framework.views import APIView

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
        content = content.replace('\'', '\\\'')
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
    """用户上传自己的作业, 作业名命名格式: username_workId_filename
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
            file_name = username + "_" + str(homework_id) + "_" + file.name
            file_path = head_path + "\\" + file_name
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            sqlHelper = SqlHelper()
            sqlHelper.executeProcedure("addHomeWorkRecord", [username, homework_id, getNowTime(), file_name])
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "上传作业失败"
        return JsonResponse(res)

class CorrectWorks(View):
    """获取所有作业附件
    """
    def post(self, request):
        res = {'code': 400, 'msg': '获取所有作业附件成功', 'data': []}
        request = getRequest(request)
        homework_id = int(request.get("id"))
        try:
            sqlHelper = SqlHelper()
            attachments = []
            results = sqlHelper.select(VIEW_HOMEWORK_USER, cond_dict={"homework_id":homework_id},all =True)
            for ares in results:
                adic = {"attachment_id":ares[0],
                        "username":ares[2],
                        "name":ares[3],
                        "time":ares[4],
                        "score":ares[5],
                        "filename": ares[6]}
                attachments.append(adic)
            res['data'] = {"id":homework_id,
                           "attachments":attachments}
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "获取所有作业附件失败"
        return JsonResponse(res)

class DeleteWorkRecord(View):
    def post(self, request):
        res = {'code': 400, 'msg': '删除作业附件成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        try:
            sqlHelper = SqlHelper()
            sqlHelper.delete(TB_HOMEWORK_USER, {"id":id})
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "删除作业附件成功"
        return JsonResponse(res)

class GiveScore2Work(View):
    """给作业一个分数
    """
    def post(self, request):
        res = {'code': 400, 'msg': '批改作业成功', 'data': []}
        request = getRequest(request)
        id = request.get("id")
        score = request.get("score")
        try:
            sqlHelper = SqlHelper()
            sqlHelper.update(TB_HOMEWORK_USER, {"score":score}, {"id":id})
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "批改作业失败"
        return JsonResponse(res)

class DownloadOne(APIView):
    """下载单个作业附件"""
    def post(self, request):
        res = {'code': 400, 'msg': '下载作业失败', 'data': []}
        id = int(request.data.get("id"))
        print(id)
        filename = ""
        try:
            sqlHelper = SqlHelper()
            filename = sqlHelper.select(TB_HOMEWORK_USER, ["name"], {"id":id})[0][0]
            print(filename)
        except BaseException as e:
            print(e)
            return JsonResponse(res)
        file_path = os.path.join(HOMEWORK_ROOT, filename)
        response = big_file_download(file_path, filename)
        if response:
            return response
        return JsonResponse(res)
