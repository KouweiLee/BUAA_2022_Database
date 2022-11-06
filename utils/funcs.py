import datetime

from django.http import StreamingHttpResponse, JsonResponse
from django.utils.encoding import escape_uri_path

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