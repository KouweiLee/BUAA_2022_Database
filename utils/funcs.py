import datetime


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
