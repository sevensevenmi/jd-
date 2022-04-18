"""
const $ = new Env("屈臣氏签到");
屈臣氏签到

cron:
0 7 * * * qd_qcs.py
"""



import requests

headers = {
    'Host': 'iws.watsonsvip.com.cn',
    'Connection': 'keep-alive',
    'Content-Length': '2',
    'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1bmlvbklkIjoib1dIZFl3UmRLVEdySERHT0U4RU1Qaks5UjY5RSIsInNlc3Npb25LZXkiOiI2ZFFESzl5c21EYlYyZXQvZGk5SWp3PT0iLCJsb2dpblR5cGUiOiJ3eCIsInBob25lIjoiMTg3Mjk0NjkyMDgiLCJvcGVuSWQiOiJvWVlUOTQxRkVFMEZvWXMwa19HNGw5QUktYXhvIiwibG9naW5CeSI6InBob25lIiwiYXBwSWQiOiJibXBmZGVjMjFmYTk1IiwibWFpbk1lbWJlcklkIjoiMTkwMzkxNzQwNTYiLCJsb2dpblBob25lIjoiMTg3Mjk0NjkyMDgiLCJwaG9uZU1haW5NZW1iZXJJZCI6IjE5MDM5MTc0MDU2IiwiaWQiOjIyNjgyODUxLCJtZW1iZXJJZCI6IjE5MDM5MTc0MDU2IiwiZXhwIjoxNjUxMTA0MTE0fQ.aIdudAeq5RIR2NqWYOx2k-3DeTywOPsOA5xUYq82SIYl4-gMHPGgxHsqaK4fv_gyfQ8DDNvABNHV0Qp5lghOGw',
    'charset': 'utf-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3193 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/7998 MicroMessenger/8.0.20.2100(0x28001439) Process/appbrand1 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'Referer': 'https://servicewechat.com/wxa828a9623404f124/269/page-frame.html',
}
json_data = {}

def test():
    response = requests.post('https://iws.watsonsvip.com.cn/watsons-member-center/mp/checkin/user/doCheckIn', headers=headers, json=json_data)
    print(response.json())

if __name__=='__main__':
    test()