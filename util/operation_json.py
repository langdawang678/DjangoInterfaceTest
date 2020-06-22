#coding:utf-8
#7-5 重构json工具类,跟随视频的code和code压缩包中的不一致。解压后如下：
import json
class OperetionJson:
	def __init__(self,file_path=None):
		if file_path  == None:
			self.file_path = '../dataconfig/user.json'
		else:
			self.file_path = file_path
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open(self.file_path) as fp:
			data = json.load(fp)  # data是<class 'dict'>
			return data

	#根据关键字获取数据
	def get_data(self,id):
		# return self.data[id]
		return self.data.get(id)  # 字典的get方法

	#写json
	def write_data(self,data):
		with open('../dataconfig/cookie.json','w') as fp:
			fp.write(json.dumps(data))



if __name__ == '__main__':
	opjson = OperetionJson()
	print (opjson.get_data('shop'))