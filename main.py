import requests
import json
from datetime import datetime, timezone, timedelta
baseUrl = "https://qyapi.weixin.qq.com/cgi-bin"
sendTextUri = "/message/send"
corpId = "ww4d015215e8671ab3"
corpSecret = "7mw3SwixYj92hBF-_Ah6RimhPX8N8UPbgT5M5kqkPUA"
agentId = 1000002
msgType = "text"

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

def getAccessToken():
    url = baseUrl+"/gettoken?corpid="+corpId+"&corpsecret="+corpSecret
    fileContent = GET(url)
    sendText(fileContent['access_token'])
def sendText(accessToken):
    v1 = GET("https://v1.hitokoto.cn/?c=f")
    data = {}
    data["touser"] = "@all"
    data['msgtype'] = msgType
    data['agentid'] = agentId
    data['text'] = {}
    data['text']['content'] = "【摸鱼办公室】 \n"+datetime.now().astimezone(timezone(timedelta(hours=+8))).strftime('%m月%d日')+"早上好，工作再累，一定不要忘记摸鱼哦\n【每日一言】\n"+v1['hitokoto']+"\n【提醒】\n多喝水 注意身体！"
    data['safe'] = 0
    data['enable_id_trans'] = 0
    data['enable_duplicate_check'] = 0
    data['duplicate_check_interval'] = 1800
    url = baseUrl+sendTextUri+"?access_token="+accessToken+"&debug=1"
    res = POST(url,data,"")
if __name__ == '__main__':
    getAccessToken()
    print("运行成功")
