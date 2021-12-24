"""
const $ = new Env("屈臣氏签到");
屈臣氏签到

cron:
0 7 * * * qd_qcs.py
"""



import requests

def test():

    headers = {
        'Host': 'iws.watsonsvip.com.cn',
        'Connection': 'keep-alive',
        'Content-Length': '2',
        'authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJ1bmlvbklkIjoib1dIZFl3UmRLVEdySERHT0U4RU1Qaks5UjY5RSIsInNlc3Npb25LZXkiOiJqbC9yaVVEblBtSU9PT2JOTElybXZBPT0iLCJsb2dpblR5cGUiOiJ3eCIsInBob25lIjoiMTg3Mjk0NjkyMDgiLCJvcGVuSWQiOiJvWVlUOTQxRkVFMEZvWXMwa19HNGw5QUktYXhvIiwibG9naW5CeSI6InBob25lIiwiYXBwSWQiOiJibXBmZGVjMjFmYTk1IiwibWFpbk1lbWJlcklkIjoiMTkwMzkxNzQwNTYiLCJsb2dpblBob25lIjoiMTg3Mjk0NjkyMDgiLCJwaG9uZU1haW5NZW1iZXJJZCI6IjE5MDM5MTc0MDU2IiwiaWQiOjIyNjgyODUxLCJtZW1iZXJJZCI6IjE5MDM5MTc0MDU2IiwiZXhwIjoxNjQyMTc1MzM3fQ.DXqrfRzqWv8e8ceBSMoSz03rWGKSAsDuzx47pekdyvXiujbxEJs0V3eluk6L-BWxV-n03Yg0S_h5KiMRbpcFCA',
        'charset': 'utf-8',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3171 MMWEBSDK/20211001 Mobile Safari/537.36 MMWEBID/7998 MicroMessenger/8.0.16.2040(0x280010B0) Process/appbrand2 WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'content-type': 'application/json',
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'Referer': 'https://servicewechat.com/wxa828a9623404f124/264/page-frame.html',
    }

    data = '{}'

    response1 = requests.post('https://iws.watsonsvip.com.cn/watsons-member-center/mp/checkin/user/doCheckIn', headers=headers, data=data).text
    print(response1)


if __name__=='__main__':
    test()