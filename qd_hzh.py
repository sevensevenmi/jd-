"""
const $ = new Env("华住会签到测试");
华住会签到测试

cron:
0 7 * * * qd_hzh.py
"""

import requests

cookies = {
    'Cookie:userToken': 'ed667ecdc3e5486da5733afa33b6743e139581209',
    'Domain': '.huazhu.com',
    'Path': '/',
    'expires': 'Thu Mar 31 13:55:28 GMT+08:00 2022',
    '_hudVID': '7549a502-aa81-ee55-1e77-776481c65c07',
    '_hudPVID': '2',
    '_hudSID_TS': '1646114130009',
    '_hudSID': '1646114130009_1',
    '_hudSource': '',
    'gr_user_id': 'f45c2a40-c6c6-4315-8e1f-29dac60481dc',
    'gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd': '207cf5eb-3f04-4d10-bb76-b660e0d3a477',
    'gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd_207cf5eb-3f04-4d10-bb76-b660e0d3a477': 'true',
    'SK': 'ed667ecdc3e5486da5733afa33b6743e139581209',
    'ec': 'oMErIu33-1646114130746-158c8a2f07534-1350139280',
    '_efmdata': 'pEUR9y6IbxkDQbBGWSFhgxWrrODd0qOaFAtPjIlUP0kVD85ACofUtW6EANz9LLgZ3YiKkBCg3DmItqvBznXd8S6lXBSBi0b21CPrGz1YQzI%3D',
    '_exid': 'zQHbfVN4FH3x56DrpKNuDSoPygs%2FAQQDpMguv54Ijb1TqZGKEFR61IjKGALiRnRoJ%2BCCw19pB%2FbRRhOWk9QNzQ%3D%3D',
}


def sign():
    headers = {
        'Host': 'hweb-mbf.huazhu.com',
        'Connection': 'keep-alive',
        'Content-Length': '14',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/plain, */*',
        'Client-Platform': 'APP-ANDROID',
        'User-Agent': 'HUAZHU/android/M2012K10C/12/8.6.2/Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://campaign.huazhu.com',
        'X-Requested-With': 'com.htinns',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://campaign.huazhu.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'state': '1',
        'day': '01'
    }

    response = requests.post('https://hweb-mbf.huazhu.com/api/signIn', headers=headers, cookies=cookies, data=data)
    print(response.text)

def sign1():
    headers = {
        'Host': 'hweb-mbf.huazhu.com',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/plain, */*',
        'Client-Platform': 'APP-ANDROID',
        'User-Agent': 'HUAZHU/android/M2012K10C/12/8.6.2/Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36',
        'Origin': 'https://campaign.huazhu.com',
        'X-Requested-With': 'com.htinns',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://campaign.huazhu.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response1 = requests.get('https://hweb-mbf.huazhu.com/api/singInIndex', headers=headers, cookies=cookies)
    print(response1.text)

if __name__=='__main__':
    sign()
    sign1()
