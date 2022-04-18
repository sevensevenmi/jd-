"""
const $ = new Env("东芝签到");
东芝签到

cron:
0 7 * * * qd_dongzhi.py
"""



import requests

cookies = {
    'PHPSESSID': 'okf8f1csajh1kui7lkm93hh04p',
}

headers = {
    'Host': 'wechat-toc.toshiba-semicon-storage.com',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3193 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/7998 MicroMessenger/8.0.20.2100(0x28001439) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://wechat-toc.toshiba-semicon-storage.com/member/credit/my',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 'PHPSESSID=okf8f1csajh1kui7lkm93hh04p',
}
def sign():
    response = requests.get('https://wechat-toc.toshiba-semicon-storage.com/api/sign/index', headers=headers, cookies=cookies)
    print(response.json())

if __name__=='__main__':
    sign()