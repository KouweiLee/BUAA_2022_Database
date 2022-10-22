from django.views import View
from utils.sqlHelper import SqlHelper
from django.http import JsonResponse
from utils.funcs import *


class AddTitle(View):
    def post(self, request):
        res = {'code': 400, 'msg': '插入主题帖成功', 'data': []}
        request = getRequest(request)
        title = request.get("title")
        content = request.get("content")
        username = request.get("name")
        try:
            sqlHelper = SqlHelper()
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dic = {"title": title, "content": content, "username": username,
                   "time": now}
            sqlHelper.insert("dc_title", dic)
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "插入主题帖失败"
        return JsonResponse(res)


class DeleteTitle(View):
    def post(self, request):
        res = {'code': 400, 'msg': '删除主题帖成功', 'data': []}
        request = getRequest(request)
        title_id = int(request.get("title_id"))
        try:
            sqlHelper = SqlHelper()
            cond = {"id": title_id}
            sqlHelper.delete("dc_title", cond)
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "删除主题帖失败"
        return JsonResponse(res)


class AddComment(View):
    def post(self, request):
        res = {'code': 400, 'msg': '增加评论成功', 'data': {}}
        request = getRequest(request)
        title_id = request.get("title_id")
        content = request.get("content")
        username = request.get("commentator_id")
        commentatee_name = request.get("beCommentator_name")
        try:
            sqlHelper = SqlHelper()
            nowtime = getNowTime()
            params = [title_id, content, username, nowtime, commentatee_name]
            sqlHelper.executeProcedure("addcomment", params)
            res['code'] = 200
            res['data']["time"]= nowtime
        except:
            res['msg'] = "增加评论失败"
        return JsonResponse(res)

class DeleteComment(View):
    def post(self, request):
        res = {'code': 400, 'msg': '删除评论成功', 'data': []}
        request = getRequest(request)
        comment_id = int(request.get("comment_id"))
        try:
            sqlHelper = SqlHelper()
            cond = {"id":comment_id}
            sqlHelper.delete("dc_comment", cond)
            res['code'] = 200
        except:
            res['msg'] = "删除评论失败"
        return JsonResponse(res)

class QueryOneTitle(View):
    def post(self, request):
        res = {'code': 400, 'msg': '进入主题帖成功', 'data': []}
        request = getRequest(request)
        title_id = int(request.get("title_id"))
        try:
            sqlHelper = SqlHelper()
            sql = "select t.id, t.title, t.content, date_format(t.time,'%Y-%m-%d %H:%i:%s'), u.name, u.user_type " \
                  "from dc_title as t, tb_user as u " + \
                  ("where t.id = %d and t.username = u.username" % title_id)
            ares = sqlHelper.executeSql(sql)[0]
            dic = {"title_id": ares[0],
                   "title": ares[1],
                   "content": ares[2],
                   "time": ares[3],
                   "member_name": ares[4],
                   "member_type": ares[5]}
            res['data'] = dic
            sql = "select c.id, c.content, date_format(c.time,'%Y-%m-%d %H:%i:%s'), u.name, u.user_type, c.commentatee_name " \
                  "from dc_comment as c, tb_user as u " + \
                  ("where c.id in (select comment_id from dc_com2title where title_id = %d) and c.username = u.username" % title_id)
            results = sqlHelper.executeSql(sql)
            comments = []
            for ares in results:
                dic = {"comment_id": ares[0],
                       "content": ares[1],
                       "time": ares[2],
                       "commentator_name": ares[3],
                       "member_type": ares[4],
                       "beCommentator_name":ares[5]
                       }
                comments.append(dic)
            res['data']['comments'] = comments
            res['code'] = 200
            print(res)
        except Exception as e:
            print(e)
            res['msg'] = "进入单个主题帖失败"
        return JsonResponse(res)


class QueryTitle(View):
    def post(self, request):
        res = {'code': 400, 'msg': '按名查询主题帖成功', 'data': []}
        query_string = eval(request.body)
        if query_string == "":
            return self.getAllTitle()
        print("queryString", query_string)
        try:
            sqlHelper = SqlHelper()
            sql = "select t.id, t.title, t.content, date_format(t.time,'%Y-%m-%d %H:%i:%s'), u.name, u.user_type " \
                  "from dc_title as t, tb_user as u " + (
                              "where t.username = u.username and t.title like \'%%%s%%\'" % query_string)
            results = sqlHelper.executeSql(sql)
            for ares in results:
                dic = {"id": ares[0],
                       "title": ares[1],
                       "content": ares[2],
                       "time": ares[3],
                       "name": ares[4]
                       # "member_type": ares[5]
                       }
                res['data'].append(dic)
            print(res['data'])
            res['code'] = 200
        except Exception as e:
            print(e)
            res['msg'] = "按名查询主题帖失败"
        return JsonResponse(res)

    def getAllTitle(self):
        res = {'code': 400, 'msg': '查询所有主题帖成功', 'data': []}
        try:
            sqlHelper = SqlHelper()
            sql = "select t.id, t.title, t.content, date_format(t.time,'%Y-%m-%d %H:%i:%s'), u.name, u.user_type " \
                  "from dc_title as t, tb_user as u " \
                  "where t.username = u.username"
            results = sqlHelper.executeSql(sql)
            for ares in results:
                dic = {"id": ares[0],
                       "isTop": 'false',
                       "isOver": 'true',
                       "submitNumber": 100,
                       "replyNumber": 25,
                       "title": ares[1],
                       "url": "404",
                       "content": ares[2],
                       "tags": ['P7'],
                       "time": ares[3],
                       "name": ares[4]
                       # "member_type":ares[5]
                       }
                print(dic)
                res['data'].append(dic)
            res['code'] = 200
        except Exception as e:
            res['msg'] = "查询所有主题帖失败"
        return JsonResponse(res)
