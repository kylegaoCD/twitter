"""
测试特性:
    测试FVB下的两个接口函数是否正常
-----------------------------------------------------
测试思路:
    主要分两个：
        1、是正常参数访问；
        2、测试默认数据限制条件
        3、测试参数长度（略）
测试结果:
    pass:
    failed:
-----------------------------------------------------
"""
from django.test import TestCase, Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_users(self):
        """测试通过用户搜索接口的正常参数访问"""
        response = self.client.get('/users/AAA?limit=10')

        # check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # check that the response context contains 10 twitters
        self.assertEqual(len(response.data), 10)

    def test_users_default_limit(self):
        """检查接口的默认数据长度，默认为30条数据"""
        response = self.client.get('/users/AAA')

        # check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # check that the response context contains 30 twitters
        self.assertEqual(len(response.data), 30)

    def test_hashtags(self):
        """测试通过标签搜索接口的正常参数访问"""
        response = self.client.get('/hashtags/AAA?limit=10')

        # 测试接口是否访问成功
        assert(response.status_code == 200)

        # 测试接口响应是否有数据
        assert(len(response.data) > 0)

    def test_test_hashtags_default_limit(self):
        """检查接口的默认数据长度，默认为30条数据"""
        response = self.client.get('/hashtags/AAA')

        # check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # check that the response context contains 30 twitters
        self.assertEqual(len(response.data), 30)

        print("pass")
