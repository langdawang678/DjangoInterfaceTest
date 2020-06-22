#coding:utf-8
from unittest import mock
#模拟mock 封装
def mock_test(mock_method,request_data,url,method,response_data):
	mock_method = mock.Mock(return_value=response_data)  # 这里的方法返回值被固定（mock）
	res = mock_method(url,method,request_data)
	return res


'''
Mock是Python中一个用于支持单元测试的库，它的主要功能是使用mock对象替代掉指定的Python对象，以达到模拟对象的行为。

Python 2.7
mock还未加入标准库。
http://www.voidspace.org.uk/python/mock/index.html

Python 3.4
mock已经加入了标准库。
https://docs.python.org/3.4/library/unittest.mock-examples.html
https://docs.python.org/3.4/library/unittest.mock.html
'''