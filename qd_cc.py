"""
const $ = new Env("曹操出行");
曹操出行

cron:
0 7 * * * qd_cc.py
"""

# -*- coding: utf8 -*-

import requests

def test():
    headers = {
        'ctag': '{smdid:DuoymE0lF_0nY-Ze_SiQQg7K908Hx7-OYMbcM2QMWwENxFQfl8vus6FwWNmkEu-JLGn88Aa9aM-mVgw-5V5dkD0g}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '201',
        'Host': 'frontend.caocaokeji.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0',
    }

    data = {
      'uid': '184929328',
      'patchId': '406',
      'appVersion': '5.3.1',
      'clientType': '2',
      'sign': 'F5A1C92101831FD6939289697C26D62A',
      'appCode': '5BPSOX95E680',
      'version': '5.3.1',
      'deviceId': '9ac0b089edab1282',
      'timestamp': '1639029910712',
      'token': 'CwOTpEprEOD55X7M'
    }

    response = requests.post('https://frontend.caocaokeji.cn/hot-patch-service/setupSuccess2', headers=headers, data=data).text
    print(response)



def test1():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'content-length': '142',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2011K2C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.1',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://mobile.caocaokeji.cn',
        'x-requested-with': 'cn.caocaokeji.user',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A?uid=184929328&phone=18729469208&token=CwOTpEprEOD55X7M&cityCode=028&locPreferCityCode=028&appVersion=5.3.1&isNewWebview=1&pageStyle=3&liveCityCode=028',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'SERVERID=f9aaea2e8f0d40a1b6f9bcdc4f97f1bd|1639029939|1639029939',
    }

    data = {
      'appCode': '3SHWZXJEY3GG',
      'clientType': '3',
      'appVersion': '1.0.0',
      'encryptionId': 'C3570DEA3AFA788A',
      'timestamp': '1639029941188',
      'sign': '14B4C982F0F36D890D8087C8BDAB22E9'
    }

    response = requests.post('https://mobile.caocaokeji.cn/cap/ump-activity/acquirePageConfigByEncryptionId/1.0', headers=headers, data=data).text
    print(response)

if __name__=='__main__':
    test()
    test1()