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


