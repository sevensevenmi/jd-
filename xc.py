"""
const $ = new Env("携程签到");

携程签到

cron:
56 7 * * * xc.py
"""

# -*- coding: utf8 -*-
import time

import requests
import json

ts = str(int(round(time.time()*1000)))

url1 = "https://m.ctrip.com/restapi/soa2/22769/signToday?_fxpcqlniredt=32001043510277064413&x-traceID=32001043510277064413-"+ts+"-3995645"
def start():
    headers={
        "Content-Type": "application/json; charset=UTF-8"
    }
    url = url1
    pyload = {"platform":"APP","openId":"","rmsToken":"","head":{"cid":"32001043510277064413","ctok":"","cver":"842.004","lang":"01","sid":"8913","syscode":"32","auth":"4493CB6DEE67AE79793E1FF896025451459F0A8A6781D2E17383D65CE06068F7","xsid":"","extension":[]}}
    response = requests.post(url, data=json.dumps(pyload), headers=headers).text

    if "当日已签到" in response:
        print("当日已签到")
    else:
        print(response)
def main_handler(event, context):
    return start()
if __name__=='__main__':
    start();
