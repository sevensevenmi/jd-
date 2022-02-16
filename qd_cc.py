"""
const $ = new Env("曹操出行");
曹操出行

cron:
0 7 * * * qd_cc.py
"""

# -*- coding: utf8 -*-

import requests

def test():
    headers = {
        'ctag': '{smdid:DuoymE0lF_0nY-Ze_SiQQg7K908Hx7-OYMbcM2QMWwENxFQfl8vus6FwWNmkEu-JLGn88Aa9aM-mVgw-5V5dkD0g}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '201',
        'Host': 'frontend.caocaokeji.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0',
    }

    data = {
      'uid': '184929328',
      'patchId': '406',
      'appVersion': '5.3.1',
      'clientType': '2',
      'sign': 'F5A1C92101831FD6939289697C26D62A',
      'appCode': '5BPSOX95E680',
      'version': '5.3.1',
      'deviceId': '9ac0b089edab1282',
      'timestamp': '1639029910712',
      'token': 'CwOTpEprEOD55X7M'
    }

    response = requests.post('https://frontend.caocaokeji.cn/hot-patch-service/setupSuccess2', headers=headers, data=data).text
    print(response)



def test1():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'content-length': '142',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2011K2C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.1',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://mobile.caocaokeji.cn',
        'x-requested-with': 'cn.caocaokeji.user',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A?uid=184929328&phone=18729469208&token=CwOTpEprEOD55X7M&cityCode=028&locPreferCityCode=028&appVersion=5.3.1&isNewWebview=1&pageStyle=3&liveCityCode=028',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'SERVERID=f9aaea2e8f0d40a1b6f9bcdc4f97f1bd|1639029939|1639029939',
    }

    data = {
      'appCode': '3SHWZXJEY3GG',
      'clientType': '3',
      'appVersion': '1.0.0',
      'encryptionId': 'C3570DEA3AFA788A',
      'timestamp': '1639029941188',
      'sign': '14B4C982F0F36D890D8087C8BDAB22E9'
    }

    response = requests.post('https://mobile.caocaokeji.cn/cap/ump-activity/acquirePageConfigByEncryptionId/1.0', headers=headers, data=data).text
    print(response)

def test2():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'cn.caocaokeji.user',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('uid', '184929328'),
        ('phone', '18729469208'),
        ('token', 'CwOTpEprEODMYhNm'),
        ('cityCode', '028'),
        ('locPreferCityCode', '028'),
        ('appVersion', '5.3.3'),
        ('isNewWebview', '1'),
        ('pageStyle', '3'),
        ('liveCityCode', '028'),
    )

    response = requests.get('https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A', headers=headers, params=params).text
    print(response.json())

def test2():
    headers = {
        'Host': 'mobile.caocaokeji.cn',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K10C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 caocaokeji_CaoCaoApp_5.3.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Requested-With': 'cn.caocaokeji.user',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('uid', '184929328'),
        ('phone', '18729469208'),
        ('token', 'CwOTpEprEODMYhNm'),
        ('cityCode', '028'),
        ('locPreferCityCode', '028'),
        ('appVersion', '5.3.3'),
        ('isNewWebview', '1'),
        ('pageStyle', '3'),
        ('liveCityCode', '028'),
    )

    response = requests.get('https://mobile.caocaokeji.cn/mobile-tools/activity/C3570DEA3AFA788A', headers=headers, params=params).text
    print(response)

def test3():
    headers = {
        'ctag': '{smdid:DuzCib47tNRNjh7-EvjMxOdXZLD-L15J8TStZznAJhAWolY1OHRF0-YOkQ1zFSSngEYogu25py5KpFBt5NxEfIrA}',
        'oaid': '9a8199876c050344',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '773',
        'Host': 'cclog.caocaokeji.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.11.0',
    }

    data = {
      'app_service_event': '5baK2PrAac7aqv4uxGWKgRib4HggRJOHgtmJqkbD2jRCNB71g/o5yTUmXP7+HN05CF9QZK2eO0r6bz8diNnmdC+XjmdOklJEZ/CBy+AZ9SN4w+R7aDv/W0dXA0uLwKsaLflGqCa5OMajlFclXkz0g9R5rxj+8VmgK4uVzntDMyLtlWQbISO76zNLS9Yy5y++D8iUxGMiNMXeCCBtsfKGMJEa98Nl63l2oSfbeh00i6cNYa1W+U9h7lx3YM0XSIij7vh+tjrE7ax6i9zogtauIk7snAyBlnD03Zpw0XXwGch5qMwSprMw9qSucf7CzXBMFH7YKPhu+7mbxHfevrVPN4qbTsiJfJbWz80ZoZi32xvy+jXs2EFr6hgxKKDRIoT2FNwGzaDTSDT9qxjLet00W7h3u2wOwvk2rzp17z70r89mfaKuLDyG7fTZfOrhiv+PYFdPdY8TNA2iYRibf01Np4zmqtpRqXMq+H9eb9Jwy+IGEPDv33DPl62d93qEKUH2sWTNh7B7ZJ9/eGLUwV8Frw==',
      'key': 'ZICuEfuo7mUBhWvWcLxdFrHC2S5G5WrtaUeATBBZmXagqJUvNd4fI4Z5zu7Ei1axHPukR7yKMI19RKycjuF3wqrM1pn2bLQEvNm67oRgrIR82AwYwFFAev0wsJlFRmzJZOHpt1qaoAPBwzRqvcb4Sw2xUaO7qdaU5LeSZa8UDX8='
    }

    response = requests.post('https://cclog.caocaokeji.cn/app/event/v2', headers=headers, data=data).text
    print(response)

if __name__=='__main__':
    test()
    test1()
    test2()
    test3()