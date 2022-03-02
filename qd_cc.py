"""
const $ = new Env("曹操出行");
曹操出行

cron:
0 7 * * * qd_cc.py
"""


import requests

import time, datetime
t=int(round(time.time() * 1000))

#cookie='SERVERID=5e540e56723423239908cecb9ef9c619|1646190867|1646190167'
cookie='SERVERID=5e540e56723423239908cecb9ef9c619'
def sign():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'content-length': '259',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.8',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://mobile.caocaokeji.cn',
        'x-requested-with': 'cn.caocaokeji.user',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A?uid=184929328&phone=18729469208&token=CwOTpEprEODSwR0q&cityCode=028&locPreferCityCode=028&appVersion=5.3.8&isNewWebview=1&pageStyle=3&liveCityCode=028',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookie,
    }

    data = {
        'appCode': '5K89N0WUDYWW',
        'clientType': '3',
        'appVersion': '5.3.8',
        'uid': '184929328',
        'token': 'CwOTpEprEODSwR0q',
        'userNo': '184929328',
        'userType': '2',
        'terminal': '1',
        'cityCode': '028',
        'phone': '18729469208',
        'activityId': '38',
        'deviceId': '7a399b63d07b8186',
        #'timestamp': '1646190867540',
        'timestamp': '1646190867540',
        'sign': '5D93F7A3DC01A7D3E89940265367FDAB'
    }

    response = requests.post('https://mobile.caocaokeji.cn/cap/ump-ygo/applyCycleAndSign/1.0', headers=headers,  data=data)
    print(response.json())


def sign1():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'content-length': '139',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.8',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://mobile.caocaokeji.cn',
        'x-requested-with': 'cn.caocaokeji.user',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A?uid=184929328&phone=18729469208&token=CwOTpEprEODSwR0q&cityCode=028&locPreferCityCode=028&appVersion=5.3.8&isNewWebview=1&pageStyle=3&liveCityCode=028',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': cookie,
    }

    data = {
        'appCode': '5K89N0WUDYWW',
        'clientType': '3',
        'appVersion': '1.0.0',
        'activityId': '38',
        'pageCode': '101',
        'timestamp': '1646190867521',
        'sign': 'D1EF89E4748A9EF9731A20ABC4FD651D'
    }

    response1 = requests.post('https://mobile.caocaokeji.cn/cap/ump-ygo/querySignPageConfig/1.0', headers=headers, data=data)
    print(response1.json())

if __name__=='__main__':
    sign()
    sign1()