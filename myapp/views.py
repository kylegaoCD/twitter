from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.getting import *


@api_view(['GET'])
def users(request, name):
    """
    获取指定用户名推特数据
    :param request:
    :param name: 用户名
    :return:
    """
    # print(name)
    limit = request.GET.get('limit', 30)
    res = get_hashtag(name, limit)
    return Response(res)


@api_view(['GET'])
def hashtags(request, hashtag):
    """
    搜索指定tag内容
    :param request:
    :param hashtag:
    :return:
    """
    # print(hashtag)
    limit = request.GET.get('limit', 30)
    res = get_hashtag(hashtag, limit)
    return Response(res)

