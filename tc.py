"""
const $ = new Env("同程签到");

携程签到

cron:
56 7 * * * tc.py
"""

# -*- coding: utf8 -*-
import time

import requests
import json

ts = str(int(round(time.time()*1000)))

url1 = "https://tcmobileapi.17usoft.com/platformsign/sign/signIndex"
def start():
    headers={
        "Content-Type": "application/json; charset=UTF-8"
    }
    url = url1
    pyload = {"isReceive":1,"memberId":"c9d47dd6f69f3d31ca49f7d0a936a945","platId":100,"reqFrom":"app","regid":"","deviceId":"208dd19477e57379"}
    response = requests.post(url, data=json.dumps(pyload), headers=headers).text

    if "请求成功" in response:
        print("签到成功")
    else:
        print(response)
def main_handler(event, context):
    return start()
if __name__=='__main__':
    start();
