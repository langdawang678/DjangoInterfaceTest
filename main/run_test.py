#7-9 主流程封装及错误解决调试
# #coding:utf-8
import sys,requests
sys.path.append("E:\\111\\Py\\Py_code\\6Python接口测试框架实战与自动化进阶\\DjangoInterface")
sys.path.append('//Users//chenxuanhuai//Documents//PycharmProjects//Py//Py_code//6Python接口测试框架实战与自动化进阶//DjangoInterface//data')
sys.path.append('//Users//chenxuanhuai//Documents//PycharmProjects//Py//Py_code//6Python接口测试框架实战与自动化进阶//DjangoInterface')
from base.runmethod import RunMethod
from data.get_data import GetData
class RunTest:
    def __init__(self):
        self.run_method  = RunMethod
        self.data = GetData()

    # 程序执行的
    def go_on_run(self):
        #10  0,1,2,3
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            url = self.data.get_request_url(i)
            print(url)
            method = self.data.get_request_method(i)
            print(method)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            if is_run:
                #method,url,data=None,header=None
                res = self.run_method.run_main(method,url,data,header)
            return res
            continue

if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()