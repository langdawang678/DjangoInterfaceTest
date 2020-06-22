#7-9 主流程封装及错误解决调试
# #coding:utf-8
import sys,requests
sys.path.append(r"../DjangoInterfaceTest")
sys.path.append(r'../DjangoInterface/data')
from base.runmethod import RunMethod
from data.get_data import GetData
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    # 程序执行的
    def go_on_run(self):
        res =None
        #10  0,1,2,3
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            if is_run:
                #method,url,data=None,header=None
                res = self.run_method.run_main(method,url,data,header)
                print(res)

if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()