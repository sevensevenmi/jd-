"""
const $ = new Env("去哪儿签到");
去哪儿签到

cron:
0 7 * * * qd_.py
"""


import requests
def start():
    headers = {
        'Host': 'user.qunar.com',
        'accept': 'application/json; charset=UTF-8',
        'user-agent': 'QunaraPhone',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'content-length': '57',
        'accept-encoding': 'gzip',
        'cookie': 'QN1=0000858041383a2871b0b5fc; _q=U.hrvbzwq0217; _v=uAf5WC3Stg2apfNmbL3c6w4raEgFfgj78llmQaMldSY9ZMLcaBO5QGlrcudd92NVnbEFuBdRAltDYRqm-2y9LtLHcBTgpeHJumloG5Fz8DGI_cjgVNG9kCyxwVI97Lmp8ZITD0IZdPNn8E5bTlIBos4jLizPhTSVUEQ1_CbSO4Sg; _t=27777089; _s=s_UL3NQAIBQQ4SPTEB23ELJO7KI4; QN300=organic; QN48=00008d802f103a2872202040; QN601=a0de52268324c9e37bf019074f107476; QN290=Mj54gxNjgwNTU3MTVlYzliYiUyQzYwMDAxNDY4JTJDQzU0OTAlMkMzNTc2RDcxQy03RDE0LTJBRjMtMjc5Mi1CRkVENDU5MjkzMzMlMkMxMDAxMCUyQzY5ODA5YTJlLWZhNDgtNGNjYy1hOGNjLWJhZmE0YTkxN2FjNyUyQzI4MTY4MDU1NzE1ZWM5YmI=; QN241=; csrfToken=yk4MwFrbU1htH7w',
    }

    data = {
      'channel': 'app',
      'platform': 'android',
      'slideSessionId': '',
      'qpVersion': '63'
    }

    response = requests.post('https://user.qunar.com/webapi/member/signIndexV2.htm', headers=headers, data=data).text
    if "每日签到" in response:
        print("去哪儿签到成功")
    else:
        print(response)

if __name__=='__main__':
    start()