from datetime import datetime, timedelta

from django.http import StreamingHttpResponse, JsonResponse
from django.utils.encoding import escape_uri_path
import jwt


def result(code=200, message="", data=None, kwargs=None):
    json_dict = {"code": code, "message": message, "data": data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


def user_authenticate():
    def decorator(view_func):
        def _wrapped_view(self, request, *args, **kwargs):
            try:
                # print("request", request)
                # print("hele", request.META is None)
                auth = request.META.get('HTTP_AUTHORIZATION').split()
            except AttributeError as e:
                print(e)
                return result(400, "No authenticate header")

            if auth[0].lower() == 'token':
                try:
                    dict = jwt.decode(auth[1], "123456", algorithms=['HS256'])
                except jwt.ExpiredSignatureError:
                    return result(400, "Token expired")
                except jwt.InvalidTokenError:
                    return result(400, "Invalid token")
                except Exception as e:
                    return result(400, "未知错误")

            return view_func(self, request, *args, **kwargs)
        return _wrapped_view
    return decorator


def getJwt():
    """产生jwt"""
    pay_load = {"user_id": "db",
                'exp': datetime.utcnow() + timedelta(days=1),# 这个地方设置token的过期时间。
                'iat': datetime.utcnow()}
    token = jwt.encode(payload=pay_load, key="123456", algorithm='HS256')  # 秘钥为123456
    return token


def getNowTime():
    """
    获取当前时间
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def getRequest(request):
    """
    获取预处理后的request
    """
    request = str(request.body).replace("true", "True").replace("false", "False")

    return eval(eval(request))


def putError(e):
    """输出红色错误信息
    """
    err = "Error:"
    print("\033[0;31;40m", err, e, "\033[0m")


def file_iterator(file_path, chunk_size=512):
    """
    文件生成器,防止文件过大，导致内存溢出
    :param file_path: 文件绝对路径
    :param chunk_size: 块大小
    :return: 生成器
    """
    with open(file_path, mode='rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def big_file_download(download_file_path, filename):
    try:
        response = StreamingHttpResponse(file_iterator(download_file_path))
        # 增加headers
        response['Content-Type'] = 'application/octet-stream'
        response['Access-Control-Expose-Headers'] = "Content-Disposition, Content-Type"
        response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path(filename))
        return response
    except Exception:
        return JsonResponse({'code': 400, 'msg': '下载文件失败', 'data': []})
