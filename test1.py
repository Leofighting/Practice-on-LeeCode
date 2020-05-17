# import unittest
# from unittest import mock
# import client
#
#
# class TestClient(unittest.TestCase):
#     def test_success_request(self):
#         success_send = mock.Mock(return_value="200")
#         client.send_request = success_send
#         self.assertEqual(client.visit_baidu(), "200")
#
#     def test_fail_request(self):
#         fail_send = mock.Mock(return_value="404")
#         client.send_request = fail_send
#         self.assertEqual(client.visit_baidu(), "404")
#
#
# if __name__ == '__main__':
#     unittest.main()

import re

p = re.compile("\w+@\w+.com")
result = p.match("qwe123@qq.com").group()
print(result)