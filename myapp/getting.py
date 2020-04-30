# import hashlib
import json
# import random
# import string
# import time
import requests

# from utils.credentials import *


#  TODO 暂时没有twitter application，官网因为新冠延迟申请，不使用SDK要求下，我准备用requests去请求
# def get_token(keyword, count):
    # timestamp = str(time.time())
    # noncestr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))  # 创建随机字符串
    # string1 = 'GET&https://twitter.com/oauth/request_token&oauth_consumer_key=%s&oauth_nonce=%s&oauth_signature_method=HMAC-SHA1&oauth_timestamp=%s&oauth_version=1.0' \
    #         % (CONSUMER_KEY, noncestr, timestamp)
    # signature = (hashlib.sha1(string1.encode())).hexdigest()  # 对字符串进行sha1加密
    # url = 'https://api.twitter.com/1.1/search/tweets.json?q=%s?' \
    #       '&result_type=mixed' \
    #       '&count=%s' \
    #       '&oauth_consumer_key=%s' \
    #       '&oauth_signature_method=HMAC-SHA1' \
    #       '&oauth_signature=%s' \
    #       '&oauth_timestamp%s' \
    #       '&oauth_token%s' \
    #       '&oauth_nonce%s' \
    #       '&oauth_version=1.0' % (keyword, count, CONSUMER_KEY, signature, timestamp, ACCESS_TOKEN, noncestr)
    # 本地网络代理
    # proxies = {
    #     'https': 'http://127.0.0.1:1087'
    # }
    # response = requests.get(url, proxies=proxies)


def user_twitter(name, count):
    """
    获取指定用户的twitter
    模拟的接口数据
    :param name: 输入的用户名
    :param count:  limit数据条数
    :return:
    """
    url = 'http://rap2.taobao.org:38080/app/mock/252795/search/222?hashtag=%s&limit=%s' % (name, count)
    response = requests.get(url)
    temp_data = json.loads(response.text)
    # 模拟limit
    data = temp_data['statuses'][:int(count)]
    return data


def get_hashtag(hashtag, count):
    """
    获取twitter的search result
    模拟的接口数据
    :param hashtag: 输入的标签
    :param count:  limit数据条数
    :return:
    """
    # 用rap2的模拟接口数据
    url = 'http://rap2.taobao.org:38080/app/mock/252795/search/1111?hashtag=%s&limit=%s' % ('#' + hashtag, count)
    response = requests.get(url)
    temp_data = json.loads(response.text)
    # 模拟limit
    data = temp_data['statuses'][:int(count)]
    return data

