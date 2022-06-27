"""
const $ = new Env("爱快签到");
爱快签到

cron:
0 7 * * * qd_ikuai.py
"""

import requests

headers = {
    # 'Content-Length': '48',
    'Host': 'mini.ikuai8.com',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.2.0',
}

data = {
    'clientId': 'aed2d21ebbd067e06a9dbd43aedc634d',
    'type': '1',
}

response = requests.post('https://mini.ikuai8.com/api/getSignInfo', headers=headers, data=data)


print(response.json())