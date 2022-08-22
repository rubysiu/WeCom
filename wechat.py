from request import GET,POST
from datetime import datetime, timezone, timedelta
accessToken = ''
templateId = ''
birthday = ''
curCity = ''
week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]

def getAccessToken(appid,secret):
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
    res = GET(url)
    return res['access_token']
def v1():
    v1 = GET("https://v1.hitokoto.cn/?c=f")
    return v1['hitokoto']
def sendText(openId):
    url =  'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token='+accessToken
    now = datetime.now()
    formatDate = now.astimezone(timezone(timedelta(hours=+8))).strftime('%Y年%m月%d日')
    weekday = week_list[now.weekday()]
    weather =  getWeather()
    todayWeather = weather['forecast'][0]
    birthdayNum = (birthday - datetime.now()).days
    if(birthdayNum < 0):
        birthdayNum = 365 + birthdayNum
    data = {
        'touser': openId,
        'template_id': templateId
    }
    params = {}
    params['keyword1'] = {
        "value":formatDate+" "+weekday,
        "color":"#0097A7"
    }
    params['keyword2'] ={
        "value":todayWeather['type'],
        "color":"#512DA8"
    }
    params['keyword3'] ={
        "value":todayWeather['low'],
        "color":"#8BC34A"
    }
    params['keyword4'] ={
        "value":todayWeather['high'],
        "color":"#FFB300"
    }
    params['keyword5'] ={
        "value":birthdayNum,
        "color":"#9C27B0"
    }
    params['keyword6'] ={
        "value":v1(),
        "color":"#0277BD"
    }

    data['data'] = params
    res = POST(url,data,'')
    print(res)
def getAllUser(openId):
    url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='+accessToken+'&next_openid='+openId
    res = GET(url)
    return res['data']['openid']
def getWeather():
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+curCity
    res =  GET(url)
    return res['data']
if __name__ == '__main__':
    appid = 'wx36b4e3606d46939d'
    secret = 'a4dbba420069a003fae476ea74604d5d'
    templateId = '_lHNoRVxxX96FOrMCA8Ft_93QbHGdFwpp6l7FYR-tfM'
    curCity = '林州市'
    birthday = datetime(int(datetime.now().year),10,6)
    accessToken = getAccessToken(appid,secret)
    openId = getAllUser('')
    for e in openId:
        sendText(e)    
    print("运行成功")