"""
const $ = new Env("屈臣氏签到");
屈臣氏签到

cron:
0 7 * * * qd_qcs.py
"""



import requests

def test():
    headers = {
        'Host': 'mystore-gw.watsonsvip.com.cn',
        'Connection': 'keep-alive',
        'Content-Length': '110',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 watsons/5.13.1/190',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://mystore-h5.watsonsvip.com.cn',
        'X-Requested-With': 'com.watsons.mobile',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mystore-h5.watsonsvip.com.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('device_id', '943498f7e44d17a8c8fc806ff3dc107e'),
        ('timestamp', '1645008380584'),
        ('session_token', 'Gfe643b44a80fde807898b50334d6dea'),
        ('app_key', '7DgWtsq0yGuvG26UPMdHKXRk4wVLTp52'),
        ('store_no', '9114'),
        ('access_token', 'DDm9bAT1xgZJ7Wz345kQh7kJ'),
        ('api_sign', '223fc3a50c09e1daf981270b00e73ace'),
    )
    data = {
        'serverName': 'APPSIGN',
        'method': 'get',
        'uri': 'appsign/v1/redEnvelopeConfig/get',
        'access_token': 'DDm9bAT1xgZJ7Wz345kQh7kJ'
    }
    #response = requests.post('https://mystore-gw.watsonsvip.com.cn/peapod/common_api', headers=headers, params=params,data=data)
    #response = requests.post('https://mystore-gw.watsonsvip.com.cn/peapod/common_api?device_id=943498f7e44d17a8c8fc806ff3dc107e&timestamp=1645008380585&session_token=Gfe643b44a80fde807898b50334d6dea&app_key=7DgWtsq0yGuvG26UPMdHKXRk4wVLTp52&store_no=9114&access_token=DDm9bAT1xgZJ7Wz345kQh7kJ&api_sign=51c273808ce8a7982df92da71494d8ac', headers=headers, data=data)
    response = requests.post('https://mystore-gw.watsonsvip.com.cn/peapod/common_api?device_id=943498f7e44d17a8c8fc806ff3dc107e&timestamp=1645008380584&session_token=Gfe643b44a80fde807898b50334d6dea&app_key=7DgWtsq0yGuvG26UPMdHKXRk4wVLTp52&store_no=9114&access_token=DDm9bAT1xgZJ7Wz345kQh7kJ&api_sign=223fc3a50c09e1daf981270b00e73ace', headers=headers, data=data)
    print(response.text)


if __name__=='__main__':
    test()