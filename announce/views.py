from django.views import View
from utils.sqlHelper import SqlHelper
from django.http import JsonResponse
from utils.funcs import *
from utils.Def import *

class GetAllDevelops(View):
    """获取所有社团发展历史信息"""
    def post(self, request):
        res = {'code': 400, 'msg': '获取全部历史信息成功', 'data': []}
        try:
            sqlHelper = SqlHelper()
            result = sqlHelper.select(AN_DEVELOPS, all=True)
            message_dict = {}
            for ares in result:
                res_dict = {"id":ares[0],
                            "year":ares[1],
                            "overview":ares[2],
                            "pics":[]}
                message_dict[ares[0]] = res_dict
            result = sqlHelper.select(AN_PICS, all=True)
            for ares in result:
                res_dict = message_dict.get(ares[1])
                res_dict["pics"].append(ares[0])
            message_list = list(message_dict.values())
            print(message_list)
            #TODO: 这里可能要加个排序
            res['data'] = message_list
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "获取全部历史信息失败"
        return JsonResponse(res)

class AddDevelop(View):
    """创建社团发展历史信息"""
    def post(self, request):
        res = {'code': 400, 'msg': '创建社团历史信息成功', 'data': []}
        request = getRequest(request)
        year = request.get("year")
        overview = request.get("overview")
        pics = request.get("pics")
        print(pics)
        try:
            sqlHelper = SqlHelper()
            sqlHelper.insert(AN_DEVELOPS, {"time":year, "overview":overview})
            ares = sqlHelper.select(AN_DEVELOPS, listnames=['id'], cond_dict={"time":year})[0][0]
            for pic in pics:
                sqlHelper.insert(AN_PICS, {"develop_id":ares, "pic_url":pic})
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "创建社团历史信息失败"
        return JsonResponse(res)

class ChangeDevelop(View):
    """修改社团发展信息"""
    def post(self,request):
        res = {'code': 400, 'msg': '修改社团历史信息成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        year = request.get("year")
        overview = request.get("overview")
        pics = request.get("pics")
        try:
            sqlHelper = SqlHelper()
            sqlHelper.update(AN_DEVELOPS, {"time":year, "overview":overview}, {"id":id})
            for pic in pics:
                sqlHelper.insert(AN_PICS, {"pic_url":pic, "develop_id":id})
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "修改社团历史信息失败"
        return JsonResponse(res)

class GetAllMembers(View):
    """获取所有成员信息"""
    def post(self, request):
        res = {'code': 400, 'msg': '获取所有成员信息成功', 'data': []}
        request = getRequest(request)
        id = int(request.get("id"))
        try:
            sqlHelper = SqlHelper()
            result = sqlHelper.executeProcedure("selectAllMembers", [id])
            for ares in result:
                dic = {"name": ares[0],
                       "profile": ares[1],
                       "pic": ares[2]}
                res['data'].append(dic)
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = '获取所有成员信息失败'
        return JsonResponse(res)

class AddMember(View):
    """增加成员信息"""
    def post(self, request):
        res = {'code': 400, 'msg': '增加成员信息成功', 'data': []}
        request = getRequest(request)
        develop_id = int(request.get("develop_id"))
        username = request.get("username")
        try:
            sqlHelper = SqlHelper()
            sqlHelper.insert(AN_DEVELOP_MEMBER, {"develop_id":develop_id, 'username':username})
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = '增加成员信息失败'
        return JsonResponse(res)
