#coding:utf-8
import unittest,json,HTMLTestRunner
from demo import RunMain
from mock import mock
from mock_demo import mock_test


class TestMethod(unittest.TestCase):
    #创建测试类的时候要继承unittest类
    def setUp(self):
        self.run = RunMain()
    def test_01(self):
        #所有的case要以test开头
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1111111111',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'
        }

        #self.run.run_main= mock.Mock(return_value=data)
        res = mock_test(self.run.run_main, data, url, "POST", data)

        # res =self.run.run_main(url,'POST',data)
        print (res)

        #若01的某个值在后面的case要被用到，可以声明为全局变量 globals()，见5-4 6分钟
        #testcase的执行顺序是按照字母的（非上下顺序），有依赖时注意（尽量别依赖）
    #跳过case执行，@unittest.skip('test_02')
    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '2222222',
            'uid': '5249192',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'
        }
        res=self.run.run_main(url, 'POST', data)
        print (res)
        print('直接返回的res类型：',type(res))
        res = json.loads(res) #loads反序列化，把json字符串变为字典
        print('处理后的的res类型：',type(res))
        self.assertEqual(res['errorCode'],1007,"msg ceode err")
if __name__ == '__main__':
    filepath= "../report/htmlreport.html"
    fp= open(filepath,'wb')
    # 执行方式1：unittest.main()
    # 执行方式2：申明容器
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_01'))
    #容器加case
    # unittest.TextTestRunner().run(suite)
    #运行case
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="this is my first report")
    runner.run(suite)
    fp.close()


    #？当case 不同的py文件里，把不同py里的case加进来
#0314 home tested