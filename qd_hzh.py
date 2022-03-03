"""
const $ = new Env("华住会签到测试");
华住会签到测试

cron:
0 7 * * * qd_hzh.py
"""


import requests

def sign():
    headers = {
        'Host': 'hweb-mbf.huazhu.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'Access-Control-Request-Method': 'POST',
        'Access-Control-Request-Headers': 'client-platform,user-token',
        'Origin': 'https://campaign.huazhu.com',
        'User-Agent': 'HUAZHU/android/M2012K10C/12/8.6.2/Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36',
        'Sec-Fetch-Mode': 'cors',
        'X-Requested-With': 'com.htinns',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://campaign.huazhu.com/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    response = requests.options('https://hweb-mbf.huazhu.com/api/signIn', headers=headers)
    print(response.text)

def sign1():

    cookies = {
        'Cookie:userToken': 'ed667ecdc3e5486da5733afa33b6743e139581209',
        'Domain': '.huazhu.com',
        'Path': '/',
        '_hudVID': '7549a502-aa81-ee55-1e77-776481c65c07',
        '_hudSource': '',
        'gr_user_id': 'f45c2a40-c6c6-4315-8e1f-29dac60481dc',
        'ec': 'oMErIu33-1646114130746-158c8a2f07534-1350139280',
        'SK': 'ed667ecdc3e5486da5733afa33b6743e139581209',
        '_hudPVID': '4',
        '_hudSID': '1646278106512_3',
        '_hudSID_TS': '1646278106512',
        'gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd': '94e8e3ec-6beb-4d97-a739-5f1e7a78aa0b',
        'gr_session_id_8f6e3e7f89d647cab9784afa81ea87bd_94e8e3ec-6beb-4d97-a739-5f1e7a78aa0b': 'true',
        '_efmdata': 'pEUR9y6IbxkDQbBGWSFhgxWrrODd0qOaFAtPjIlUP0kVD85ACofUtW6EANz9LLgZFPwyQ6cqYU70H9E3TM6cajK%2Flpg%2FymxqFu1oNX%2BlfDQ%3D',
        '_exid': 'ebxy%2FwcQI2LIGlofi0iSa9T6zFG%2BOylKQsZ4t0Si6mizagfJx%2BotMevYIEAczD7aYUPz%2BSfX5Hi2fdUKS5WY9Q%3D%3D',
        'expires': 'Sat Apr 02 11:28:57 GMT+08:00 2022',
    }

    headers = {
        'Host': 'hweb-mbf.huazhu.com',
        'Connection': 'keep-alive',
        'Content-Length': '14',
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
      'day': '03'
    }

    response1 = requests.post('https://hweb-mbf.huazhu.com/api/signIn', headers=headers, cookies=cookies, data=data)
    print(response1.json())

if __name__=='__main__':
    sign()
    sign1()
