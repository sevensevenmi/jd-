"""
const $ = new Env("和彩云签到测试");
和彩云签到测试

cron:
0 7 * * * qd_hcy.py
"""


import requests

cookies = {
    'SESSION': 'NGQ4ZGQ4YTgtNmQ2Mi00OTU5LTliY2MtMTNkMjdiYmI0YWRm',
    'WAPJSESSIONID': '4d8dd8a8-6d62-4959-9bcc-13d27bbb4adf',
    'bc_mo': '"MTg3Mjk0NjkyMDg="',
    'bc_to': '"a2U0azZWNm58MXxSQ1N8MTY1MDU0MjE5MTY1NHxKMHlIQmdxOWc4a1RSNHd6MFN2Lk9JZHNIaTRQakc1RkUxMS5pb2JqOHZNRnlncVpFcHNYbkpKTkFKU05FX1hjS21RV1FvWlIwXzQzSTlDZFNuQkJ4M05vYXNuUHFoeGlkRGJQWElwdHAwM2NZd2Rkb0VqX0YyVlBOU1QuNVouMGhhUTBueEZBUFp3N1FTMmJjNVN1T3Z2VDU3VE9yV1lzUkd0am53OTYueTQt"',
    'bc_ps': '"NTI4OTU5ODIy"',
    'defaultloginuser_p': 'izr73fwOUuimT7R+YElqbvQdIEKrmWCpu49KY4pe7cglQnOlbxDN0nqcpR0yt5wiDSOPqpAhg4a3OUkDSMhMpCMTsRVyT13VInOal6sQlEY+dvBVErR/ksPv5W6XILGzNIChi3gihwmhVzzoGOae/eb3Sl6SEc5MCtX8hRwjRnaNwSyqpJkEqg/LuT1QHsyO',
    'CmLocation': '290|916',
    'CmProvid': 'bj',
    'WT_FPC': 'id=22ddc5c1d337f7209941638182562618:lv=1644549849244:ss=1644548700296',
    'sajssdk_2015_cross_new_user': '1',
    'SESSION': 'NGQ4ZGQ4YTgtNmQ2Mi00OTU5LTliY2MtMTNkMjdiYmI0YWRm',
    'sensors_stay_url': 'https%3A%2F%2Fcaiyun.feixin.10086.cn%3A7071%2Fportal%2FclientDL%2Findex.html%3Fv%3DmCloud_1331',
    'sensors_stay_time': '1647950469401',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2217fb17bf89ad71-0f27ac5101f4ae-3d76632c-370944-17fb17bf89be6d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22phoneNumber%22%3A%22MTg3Mjk0NjkyMDg%3D%22%2C%22platForm%22%3A%22activity_marketing%22%2C%22activityName%22%3A%22clientDLnew%22%2C%22channel%22%3A%221331%22%7D%2C%22%24device_id%22%3A%2217fb17bf89ad71-0f27ac5101f4ae-3d76632c-370944-17fb17bf89be6d%22%7D',
}

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
}

def sign():
    response = requests.get('https://caiyun.feixin.10086.cn/market/signin/page/info', headers=headers, cookies=cookies)
    print(response.json())

if __name__=='__main__':
    sign()
