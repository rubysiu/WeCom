import requests
import json

def GET(url):
    #get请求
    req = requests.get(url)
    #输出返回内容
    return req.json()

def POST(url,data,cookie):
    #post 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
        "Cookie": cookie}
    # req = requests.post(url,data=post_data,headers=headers)
    
    #注意：如果post_data是字典json形式的，如下，参数一般用json=
    post_data = data
    req = requests.post(url,json=post_data,headers=headers)
    
    #如果req返回的json数据，则可以用json的一个函数转换
    data = json.loads(req.text)
    return req.text