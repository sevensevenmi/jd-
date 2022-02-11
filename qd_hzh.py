"""
const $ = new Env("华住会签到测试");
华住会签到测试

cron:
0 7 * * * qd_hzh.py
"""


import requests

cookies = {
    '_hudVID': '554d4fa9-8dc8-cbbe-9b09-87a01ebc3457',
    '_hudSID': '1644561914774_1',
    '_hudSource': '',
    '_ga': 'GA1.2.370782862.1644561919',
    'ec': 'BwtD51aE-1644561921265-179bb5786059e662351977',
    'userToken': '2f9f5d17d20345b3853d5b579486c0a2139581209',
    'SK': '2f9f5d17d20345b3853d5b579486c0a2139581209',
    '_hudPVID': '6',
    '_hudSID_TS': '1644561964367',
    '_efmdata': 'qlwMXme24NrQQZgEb2ZKOv3vomJEalQHsrXMpdZ4m74Q6g5Uy87dGTIKmU1k3bvqiTR6TeQioU3ep1t%2BPP5IGgiLhO%2B5TSTPLQfx8%2FGizB4%3D',
    '_exid': '%2BPxBh6pit%2BNwd5PBAK08Bm%2BSiF4PrS0OHvmkdcOJzKSywC5jLu9hOKDTusqHlWJqzbVU%2Fv3X4DY1P1%2FlJ0pIKQ%3D%3D',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '""',
    'Client-Platform': 'WEB-APP',
    'DNT': '1',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; MI 9 Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36 XiaoMi/MiuiBrowser/2.1.1 Edg/97.0.4692.99',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json, text/plain, */*',
    'User-Token': '2f9f5d17d20345b3853d5b579486c0a2139581209',
    'sec-ch-ua-platform': '',
    'Origin': 'https://campaign.huazhu.com',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://campaign.huazhu.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = {
  'state': '30',
  'day': '30'
}

response = requests.post('https://hweb-mbf.huazhu.com/api/signIn', headers=headers, cookies=cookies, data=data)
print(response.text)