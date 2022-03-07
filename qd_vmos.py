"""
const $ = new Env("vmos签到");
vmos签到

cron:
0 7 * * * qd_vmos.py
"""



import requests

headers = {
    'androidApi': '2.0.0',
    'Access-Token': 'null',
    'Host': 'vproapi.vmos.cn',
    'Content-Type': 'application/json; charset=utf-8',
    'Device-Brand': 'Redmi',
    'Device-Model': 'M2012K10C',
    'Device-FingerPrint': 'Redmi/ares/ares:12/SP1A.210812.016/V13.0.3.1.13.DEV:user/release-keys',
    'Device-System-Version-Name': '12',
    'Device-System-Version-Code': '31',
    'Device-Real-Width': '1080',
    'Device-Real-Height': '2400',
    'Device-Display-Width': '1080',
    'Device-Display-Height': '2186',
    'lang': 'zh',
    'Device-System-Bit': '64',
    'Device-Free-Storage': '73797345280',
    'Device-Free-Memory': '73772937216',
    'Device-Total-Memory': '12102811648',
    'Device-CPU-Core': '8',
    'Device-CPU-Model': 'MT6893Z/CZA',
    'Device-CPU-Framework': '0',
    'Device-ROM-Name': 'MIUI',
    'Device-ROM-Version': 'V13.0.3.1.13.DEV',
    'Content-Length': '0',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/5.0.0-alpha.2',
}

params = (
    ('s', '1c51facd917b7f6ef289ae2f1e4904d2'),
    ('k', 'eb759cd6d8e975ec29b999b743123721'),
    ('auth_ver', '2'),
    ('n', '1646658437947'),
    ('u', 'BDE1853AD8C5C14A3C0813A1BDD7CB89B84E1A16'),
    ('c', 'xiaomi'),
    ('v', '20000'),
    ('umid', 'f1251098d255cae482b5b595141dcaceod'),
    ('mp', '18729469208'),
    ('at', '765529A213EB145F4D5AA1B09AC30860'),
    ('pb', 'Redmi'),
    ('pm', 'M2012K10C'),
    ('sv', '12'),
    ('openid', 'oDRYU1MpFOTOA93s6uL4dtfSRPjw'),
    ('qqopenid', ''),
    ('userId', '557'),
    ('isVip', 'false'),
)

#response = requests.post('https://vproapi.vmos.cn/vmospro/login/userPoints/saveSign', headers=headers, params=params)

# Note: original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
response = requests.post('https://vproapi.vmos.cn/vmospro/login/userPoints/saveSign?s=1c51facd917b7f6ef289ae2f1e4904d2&k=eb759cd6d8e975ec29b999b743123721&auth_ver=2&n=1646658437947&u=BDE1853AD8C5C14A3C0813A1BDD7CB89B84E1A16&c=xiaomi&v=20000&umid=f1251098d255cae482b5b595141dcaceod&mp=18729469208&at=765529A213EB145F4D5AA1B09AC30860&pb=Redmi&pm=M2012K10C&sv=12&openid=oDRYU1MpFOTOA93s6uL4dtfSRPjw&qqopenid&userId=557&isVip=false', headers=headers)

print(response.json())