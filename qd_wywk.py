"""
const $ = new Env("网鱼网咖签到");
网鱼网咖签到

cron:
0 7 * * * qd_wywk.py
"""



import requests

headers = {
    'Host': 'vip-gateway.wywk.cn',
    'content-length': '32',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 wywk/',
    'x-authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJzdGFfd2ViIiwiaWF0IjoxNjQ2MTEzNTMxLCJzdWIiOiI4YWQxMmQ1ZDZlYjBhMmZmMDE2ZWNmYzg2YTFkMjUxYSIsImV4cCI6MTY1MTI5NzUzMX0.rAmzl3UzYG2U8cbkdmE6r0uJ1Huv0K98GRYv3UEnBks',
    'accept': '*/*',
    'origin': 'https://wechat.wywk.cn',
    'x-requested-with': 'cn.wywk.app',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wechat.wywk.cn/',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

params = (
    ('uid', '89fbae768230dc93b111c49dea5c66a35f295872635db71b4aee27fc6f9898e7'),
)

json_data = {
    'iosSwitch': 1,
    'platform': 'app',
}

#response = requests.post('https://vip-gateway.wywk.cn/operate-growth-web/api/v1/sign/action', headers=headers, params=params, json=json_data)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
def sign():
    response = requests.post('https://vip-gateway.wywk.cn/operate-growth-web/api/v1/sign/action?uid=89fbae768230dc93b111c49dea5c66a35f295872635db71b4aee27fc6f9898e7', headers=headers, json=json_data)

    print(response.json())
    
if __name__=='__main__':
    sign()
