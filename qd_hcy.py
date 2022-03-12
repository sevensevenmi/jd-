"""
const $ = new Env("和彩云签到测试");
和彩云签到测试

cron:
0 7 * * * qd_hcy.py
"""


import requests

headers = {
    'Host': 'caiyun.feixin.10086.cn:7071',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 MCloudApp/8.11.0',
    'token': 'SZwSYuBTpxg5ImH6gs2b2x47BGjfqzTIt4MmwBTA0tzL9G7jiICsxw9DJFWrQ0gydbo7T/NI3RHAkGO5/+gdOXWo/L9sR0aQqysbt/SjomqlTXihswCH7sE75HCGNY8DFmF1a36iD15dmWqeRFcYYH+yHX+zEKi0SaIgswd39KU=',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://caiyun.feixin.10086.cn:7071/portal/newsignin/index.html?sourceid=1004&token=',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'sajssdk_2015_cross_new_user=1',
}
def sign():
    response = requests.get('https://caiyun.feixin.10086.cn/market/signin/page/info', headers=headers)
    print(response.json())

if __name__=='__main__':
    sign()
