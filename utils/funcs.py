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
