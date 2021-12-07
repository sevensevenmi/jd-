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

def sign(traceID):
    headers = {
        'authority': 'm.ctrip.com',
        'sec-ch-ua': '""',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '""',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2011K2C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36/TcTravel/10.2.2 Edg/96.0.4664.55',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'nfes_isSupportWebP=1; GUID=09031019310226741690; _abtest_userid=f75c32cf-d111-494a-8ec7-d32410d96641; nfes_isSupportWebP=1; MKT_Pagesource=H5; Union=OUID=&AllianceID=66672&SID=1693366&SourceID=&AppID=&OpenID=&exmktID=&createtime=1638842407&Expires=1639447207034; _RF1=171.217.52.70; _RSG=kq4jSd_25h5ciuauQg3LUB; _RDG=283585be2c2871270b27e9ee11a1744501; _RGUID=5ac50bf9-dcb4-4d2e-b795-0ea6b8938b26; mktDpLinkSource=ullink; _bfs=1.1; _bfaStatusPVSend=1; _bfi=p1%3D10650068916%26p2%3D0%26v1%3D4%26v2%3D0; _bfaStatus=send; login_type=0; login_uid=DE27A6C50D7E4A691372019AFA22C2E9; cticket=4493CB6DEE67AE79793E1FF8960254518CDE0913E4D5657C3C9A2DE661F20A8E; DUID=u=FB134433B4FBE5C27FBFE9C0C54664C9DDCF829A7C8A8555F5476D446C163B5C&v=0; AHeadUserInfo=VipGrade=10&VipGradeName=%BB%C6%BD%F0%B9%F3%B1%F6&UserName=%D5%D4%C7%C5%C7%C5&NoReadMessageCount=0; UUID=13D22DC87C7642C3A7C435B70F3F232B; _pd=%7B%22r%22%3A1%2C%22d%22%3A68%2C%22_d%22%3A67%2C%22p%22%3A68%2C%22_p%22%3A0%2C%22o%22%3A69%2C%22_o%22%3A1%2C%22s%22%3A70%2C%22_s%22%3A1%7D; _bfa=1.1638842403793.3y0aoq.1.1638842430738.1638842536396.2.10.10650029789',
    }

    params = (
        ('_fxpcqlniredt', '32001043510277064413'),
        ('x-traceID', traceID),
    )

    response = requests.get('https://m.ctrip.com/restapi/soa2/22598/todoTask', headers=headers, params=params).text

    print(response)

if __name__=='__main__':
    start()
    traceID_list = [32001043510277064413 - 1638842021774 - 5215742,32001043510277064413 - 1638842215767 - 7820223,32001043510277064413 - 1638842214393 - 7959989,32001043510277064413 - 1638842212796 - 8404736,32001043510277064413 - 1638842209651 - 1213574,32001043510277064413 - 1638842206654 - 2306991]
    for i in traceID_list:
        sign(traceID_list.index(i))
