from django.utils.deprecation import MiddlewareMixin
import re
from utils.funcs import *

exclued_path = ["/login/login/"]
class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        url_path = request.path
        print(url_path)

        # 如果请求在白名单里，则通过，不进行操作
        for each in exclued_path:
            if re.match(each, url_path):
                print("match")
                return

        try:
            auth = request.META.get('HTTP_AUTHORIZATION').split()
        except AttributeError as e:
            print(e)
            return result(400, "No authenticate header")

        if auth[0].lower() == 'token':
            try:
                dict = jwt.decode(auth[1], "123456", algorithms=['HS256'])
            except jwt.ExpiredSignatureError as e:
                print(e)
                return result(400, "Token expired")
            except jwt.InvalidTokenError as e:
                print(e)
                return result(400, "Invalid token")
            except Exception as e:
                return result(400, "未知错误")
        return