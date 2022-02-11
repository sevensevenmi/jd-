"""
const $ = new Env("网易蜗牛阅读签到");
网易蜗牛阅读签到

cron:
0 7 * * * qd_163du.py
"""


import requests

cookies = {
    'Cookie:_cid': 'a44963f5-054e-498e-a408-af51a451f397',
    '_xsrf': '457605ce-e211-46e2-a04b-4b1f3712e309',
    'JSESSIONID-WNYD-WEB': '1644549938454-F845E590104D04098041E0.hzabj-snailprotocolpre',
    'X-Auth-Token': '9670c4107d68461d96dd6fd3f61c1dec',
}
def main():
    headers = {
        'Host': 'du.163.com',
        'Connection': 'keep-alive',
        'Content-Length': '46',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; M2007J22C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 NeteaseSnailReader/1.9.25 NetType/WIFI (odyzmju0ntq1mte3nte2cta4ojawoji3oji3ojjhojcwctllnzjhnznjnzbhyzhjodejotq4njq4ywzjngu2zdrhoq%3d%3d;yingyongbao) NEJSBridge/2.0.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://du.163.com',
        'X-Requested-With': 'com.netease.snailread',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://du.163.com/fe/client/welfare-exchange/dist/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
      'csrfToken': '457605ce-e211-46e2-a04b-4b1f3712e309'
    }

    response = requests.post('https://du.163.com/activity/201907/activityCenter/sign.json', headers=headers, cookies=cookies, data=data)
    print(response.text)

if __name__=='__main__':
    main()