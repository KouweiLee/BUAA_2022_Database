from django.views import View
from utils.sqlHelper import SqlHelper
from django.http import JsonResponse
from utils.funcs import *
class Login(View):
    def post(self, request):
        # 仅在登录成功时返回200
        res = {'code':400, 'msg': '登录成功', 'data':[]}
        request = str(request.body).replace("true", "True")
        request = eval(eval(request))
        print(request)
        username = request.get("username")
        password = request.get("password")
        try:
            sqlHelper = SqlHelper()
            result = sqlHelper.select('tb_user', ["password", "user_type"], {"username":username})
            if result:
                key = result[0][0]
                if key == password:
                    res['code']=200
                    res['data'].append({"user_type":result[0][1]})
                    return JsonResponse(res)
                else :
                    res['msg'] = "密码错误"
                    return JsonResponse(res)
            res['msg'] = "用户名不存在"
        except Exception as e:
            print(e)
            res['msg'] = "未知错误"
        return JsonResponse(res)

class Register(View):
    def post(self, request):
        res = {'code':400, 'msg': '注册成功', 'data':[]}
        request = getRequest(request)
        username = request.get("username")
        password = request.get("password")
        try:
            sqlHelper = SqlHelper()
            result = sqlHelper.select('tb_user', ["*"], cond_dict={"username":username})
            print(result)
            if result:
                res['msg'] = "用户名重复"
                return JsonResponse(res)
            dic = {"username":username, "password":password}
            sqlHelper.insert("tb_user", dic)
        except Exception as e:
            print(e)
            res['msg'] = "未知错误"
            return JsonResponse(res)
        res['code'] = 200
        return JsonResponse(res)

class ChangePassWord(View):
    def post(self, request):
        res = {'code': 400, 'msg': '修改成功', 'data': []}
        request = eval(request.body)
        username = request.get("username")
        pre_password = request.get("pre_password")
        new_password = request.get("now_password")
        try:
            sqlHelper = SqlHelper()
            result = sqlHelper.select('tb_user', listnames=["password"], cond_dict={"username":username})
            if result:
                result = result[0]
                if result[0]==pre_password:
                    sqlHelper.update('tb_user', attrs_dict={"password":new_password}, cond_dict={"username":username})
                    res['code']=200
                else :
                    res['msg']="原密码错误"
                return JsonResponse(res)
            else :
                res['msg']="用户名不存在"
        except Exception as e:
            print(e)
            res['msg'] = "未知错误"
        return JsonResponse(res)


# Create your views here.
