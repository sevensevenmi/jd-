"""
const $ = new Env("华住会签到测试");
华住会签到测试

cron:
0 7 * * * qd_hzh.py
"""



import requests

import time, datetime
t=int(round(time.time() * 1000))
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '""',
    'DNT': '1',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 11; zh-cn; M2007J1SC Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/15.7.22 app/vipaccount Edg/98.0.4758.102',
    'sec-ch-ua-platform': '',
    'Accept': '*/*',
    'Origin': 'https://campaign.huazhu.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://campaign.huazhu.com/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

params = (
    ('stm', t),
)

data = {
  '6\x86\xF0D\n\xE6\x05\xC6\b`#\0\xB0\x01\x80f()\x92\x0B@\x0E\x01\x98\b\t\x87%\x88\x13\x80c|\b\r\x80F\x1C\f\xDD\0L\x13@V$*\xEB\xB0\0h\xC0\x06q\x86\x13\x176\x15\x88\x13\xC7\x07\x15\x04\\\x11\x95e\xC7\x02>ik`\xA4\x88\xB6$\x03\x84\x01w\x15@\r\x95\0\xD6B\xC2\x98\x0Bc\x01\x9D$\x8C\xF1\xE3\xA0\x1D\x9B\xEC\xAE\xC2\0\x0EN.n\x1E^\fx\xC4\xDE(\xC2l\x16p\x8E\x81p\0\x96\0\xE6\0v\0t\0\x16\x10p\0^yYT\0\xF6\xCEA\xE2\0\xF4\x81\xA5)\x19\xA6"\0\xCA9\xA5\x81U\xF5l\x98\0\x1E\xB9N\x96\xF6\x980\xA0`9\xE29\xA6\xA6\x81"\xD0UUT\x89\xC9\xE9\xD9y\x85\xC5e\x8E5u\r\xCD\xAD\xED"\xA6p\xA6)TU\x8E\x98l)pg\x98\x19\x108\fY\xE4H\xC8\x04phY\x81\x19i\xF6\0n\xE2\xE7;\x83\xC9\xECAx\x19\xDE\x9Fo\xBD\x9B\xADT\xBA\xFC\0\xC4\0\'R\xA9T\xC5S\x85d\xE0\x81v\x869': '',
  '\x94\xC2|\xE0\xF8\x9C \\\xE5\x91\x12\x05,)4F$EFFY,\0wDV': '\x12\x95\xF8\x95J\r[\x8D#\x95\x90BYJ\xB6,\x86N\x0B\xF7I\x1CR\xDC\xF6g0\x11\x02\xAB\\1\xD4\xCC',
  '\xD9X\xE3Ht5`\0/\xA0\x9C\x03\r\x82\xCA\x91(\xBEg \x13\x8F\xE5\xE2\t\xD6\x92y@\x91J\xA5\x9B\xC9\xF4\xD2\xA3%\x96\xC8\xC5\x94y\rY@\xA8R \x14J\xD2R\x99F>X\xAF\xB1\x8D`\xF0\xAA\x88\x99`\x04\x90\xC9\xFD\xC4\xB1\xF8\xE6I;\xA8\x02\xE8\xEA\xB3@\0': ''
}

response = requests.post('https://api.growingio.com/v2/8f6e3e7f89d647cab9784afa81ea87bd/web/action', headers=headers, params=params, data=data)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
#response = requests.post('https://api.growingio.com/v2/8f6e3e7f89d647cab9784afa81ea87bd/web/action?stm=1646188677235', headers=headers, data=data)
print(response)

