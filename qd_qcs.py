"""
const $ = new Env("屈臣氏签到");
屈臣氏签到

cron:
0 7 * * * qd_qcs.py
"""



import requests,time

t = time.time()

tamp = int(round(t * 1000))
headers = {
    'Host': 'mystore-gw.watsonsvip.com.cn',
    'Connection': 'keep-alive',
    # 'Content-Length': '101',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 watsons/5.19.0/199',
    'Origin': 'https://mystore-h5.watsonsvip.com.cn',
    'X-Requested-With': 'com.watsons.mobile',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://mystore-h5.watsonsvip.com.cn/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = {
    'serverName': 'APPSIGN',
    'method': 'post',
    'uri': 'appsign//v2/signin',
    'access_token': 'G35e1f7af6cc7f8b483ccd953c0b4ad7',
}


def test():
    response = requests.post('https://mystore-gw.watsonsvip.com.cn/peapod/common_api?device_id=dad962b4c8f8d633e971f1003bb92afa×tamp=%s'%(tamp)+'&session_token=G35e1f7af6cc7f8b483ccd953c0b4ad7&app_key=7DgWtsq0yGuvG26UPMdHKXRk4wVLTp52&store_no=9114&access_token=7unEUATilUrJ5sNmiSEpPhmknNs&api_sign=eb71fbe59f5b3660698362297801bc3c', headers=headers, data=data)
    print(response.json())

if __name__=='__main__':
    test()