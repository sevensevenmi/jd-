


"""
const $ = new Env("同程签到");

同程签到

cron:
56 7 * * * tc.py
"""

# -*- coding: utf8 -*-
import time

import requests
import json

ts = str(int(round(time.time()*1000)))

url1 = "http://amdc.m.taobao.com/amdc/mobileDispatch?appkey=12663307&deviceId=YY6IFVTYD8cDADKlmrQjUvC%2F&platform=android&v=5.0"
def start():
    headers={
        "Content-Type": "application/json; charset=UTF-8"
    }
    url = url1
    pyload = "appVersion=9.9.6.106&mnc=wifi&lng=0.0&netType=WIFI&bssid=02%3A00%3A00%3A00%3A00%3A00&appName=travel_android&channel=700169&sign=57b41698809567989bfe56b176ffbbcb2424a156&sid=864645313&carrier=wifi&cv=-1&t=1638703485548&platformVersion=12&domain=accscdn.m.taobao.com&signType=sec&stackType=4&lat=0.0"
    response = requests.post(url, data=pyload, headers=headers).text

    if "请求成功" in response:
        print("签到成功")
    else:
        print(response)
def main_handler(event, context):
    return start()
if __name__=='__main__':
    start();
