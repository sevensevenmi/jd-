"""
const $ = new Env("曹操出行");
曹操出行

cron:
0 7 * * * qd_cc.py
"""


import requests

cookies = {
    'Cookie:SERVERID': '5e540e56723423239908cecb9ef9c619|1645151870|1645151869',
}

def sign():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'Connection': 'keep-alive',
        'Content-Length': '259',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://mobile.caocaokeji.cn',
        'X-Requested-With': 'cn.caocaokeji.user',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A?uid=184929328&phone=18729469208&token=CwOTpEprEODE569U&cityCode=028&locPreferCityCode=028&appVersion=5.3.7&isNewWebview=1&pageStyle=3&liveCityCode=028',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
      'appCode': '5JJBA5NUDJWG',
      'clientType': '3',
      'appVersion': '5.3.7',
      'uid': '184929328',
      'token': 'CwOTpEprEODE569U',
      'userNo': '184929328',
      'userType': '2',
      'terminal': '1',
      'cityCode': '028',
      'phone': '18729469208',
      'activityId': '38',
      'deviceId': 'f97c5f79d935c52b',
      'timestamp': '1645151870152',
      'sign': '4DCB77ED4BD21BBADE916CD59E25104F'
    }

    response = requests.post('https://mobile.caocaokeji.cn/cap/ump-ygo/applyCycleAndSign/1.0', headers=headers, cookies=cookies, data=data)
    print(response.json())


def sign1():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'Connection': 'keep-alive',
        'Content-Length': '139',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://mobile.caocaokeji.cn',
        'X-Requested-With': 'cn.caocaokeji.user',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A?uid=184929328&phone=18729469208&token=CwOTpEprEODE569U&cityCode=028&locPreferCityCode=028&appVersion=5.3.7&isNewWebview=1&pageStyle=3&liveCityCode=028',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'appCode': '5JJBA5NUDJWG',
        'clientType': '3',
        'appVersion': '1.0.0',
        'activityId': '38',
        'pageCode': '101',
        'timestamp': '1645151870143',
        'sign': 'E114397E5F04D7F9D277D41E98E857B7'
    }
    response1 = requests.post('https://mobile.caocaokeji.cn/cap/ump-ygo/querySignPageConfig/1.0', headers=headers, cookies=cookies, data=data)
    print(response1.json())

if __name__=='__main__':
    sign()
    sign1()