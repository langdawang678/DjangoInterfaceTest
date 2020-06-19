#7-8 post、get基类的封装
import requests
import json
class RunMethod:
    def post_main(self,url,date,header=None):
        res =None
        if header != None:
            res = requests.post(url=url, date=data, heades=header)
        else:
            res = requests.post(url=url, date=data)
        return  res.json()

    def get_main(self,url,date=None,header=None):
        res =None
        if header != None:
            res = requests.get(url=url, date=data, heades=header).json()
        else:
            res = requests.get(url=url, date=data).json()
        return  res

    def run_main(self,method,url,data=None,header=None):
        res =None
        if method == "post":
            res =self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res
