import time

from django.views import View
from utils.sqlHelper import SqlHelper
from django.http import JsonResponse
from utils.funcs import *
import os
from utils.Def import *
from django.contrib.auth.hashers import make_password, check_password

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
                if check_password(password, key):
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
            encrypt_password = make_password(password, None, "pbkdf2_sha1")
            dic = {"username":username, "password":encrypt_password}
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
                if check_password(pre_password, result[0]):
                    encrypt_password = make_password(new_password, None, "pbkdf2_sha1")
                    sqlHelper.update('tb_user', attrs_dict={"password":encrypt_password}, cond_dict={"username":username})
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


class UploadHeader(View):
    """上传用户头像
    """
    def post(self, request):
        res = {'code': 400, 'msg': '上传头像成功', 'data': []}
        try:
            file = request.FILES.get('file')
            username = request.POST.get('username')
            print("username", username)
            head_path = HEADER_ROOT
            print("head_path", head_path)
            if not os.path.exists(head_path):
                os.makedirs(head_path)
            file_name = username + ".jpg"
            file_path = head_path + "\\" + file_name
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "上传作业失败"
        return JsonResponse(res)

class GetAllPics(View):
    """获取用户所有图片的url
    """
    def post(self, request):
        res = {'code': 400, 'msg': '获取所有图片成功', 'data': []}
        request = getRequest(request)
        username = request.get("username")
        try:
            sqlHelper = SqlHelper()
            result = sqlHelper.select(TB_PICS, ["position"], {"username":username})
            for ares in result:
                res['data'].append(ares[0])
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = '获取所有图片失败'
        return JsonResponse(res)

class AddPic(View):
    """
    上传用户的图片
    """
    def post(self, request):
        res = {'code': 400, 'msg': '上传图片成功', 'data': []}
        try:
            file = request.FILES.get('file')
            username = request.POST.get('username')
            print("username", username)
            pic_path = PIC_ROOT
            if not os.path.exists(pic_path):
                os.makedirs(pic_path)
            file_name = file.name
            filedate = int(time.time())
            file_name = str(filedate) + file_name
            file_path = pic_path + "\\" + file_name
            with open(file_path, 'wb') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            #开始插入数据库
            sqlHelper = SqlHelper()
            position = PIC_PREFIX + file_name
            sqlHelper.insert(TB_PICS, {"position": position, "username":username})
            res['code'] = 200
        except BaseException as e:
            print(e)
            res['msg'] = "上传图片失败"
        return JsonResponse(res)
