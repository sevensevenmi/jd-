"""
const $ = new Env("同程签到");
同程签到

cron:
0 7 * * * qd_tc.py
"""

# -*- coding: utf8 -*-
import time

import requests


ts = str(int(round(time.time()*1000)))
headers = {
    'Host': 'tcmobileapi.17usoft.com',
    'Connection': 'keep-alive',
    'Content-Length': '249',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2011K2C Build/SKQ1.220201.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36/TcTravel/10.3.0',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://appnew.ly.com',
    'X-Requested-With': 'com.tongcheng.android',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://appnew.ly.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = '{"isReceive":1,"memberId":"c9d47dd6f69f3d31ca49f7d0a936a945","platId":100,"reqFrom":"app","regid":"","deviceId":"208dd19477e57379","jy_project_id":"tcwireless_net_activityplatform_new","jy_type":"sm"}'

url1 = "https://tcmobileapi.17usoft.com/platformsign/sign/signIndex"
def start():

    response = requests.post('https://tcmobileapi.17usoft.com/platformsign/sign/signIndex', headers=headers, data=data)
    print(response.json())



if __name__=='__main__':
    start()
