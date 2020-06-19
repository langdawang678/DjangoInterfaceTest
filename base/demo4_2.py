import  requests
import json
'''
4-2 requests简单使用-post.mp4
request.post访问login地址，
login.html调用login方法（login方法在views.py中实现）
即：Django_imooc\web\views.py的login方法
'''
data={
    'username':'11',
    'password':'22'
}

res =requests.post(url="http://127.0.0.1:8000/login/",data=data)
print(res)
print('res的类型是',type(res),"\n")

# str
print(res.text)
print('res.text的类型是',type(res.text),"\n")

# dict
print(res.json())
print('res.json()的类型是',type(res.json()),"\n")
