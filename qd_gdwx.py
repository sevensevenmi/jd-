"""
const $ = new Env("高德打车wx测试");
高德打车wx测试

cron:
0 7 * * * qd_gdwx.py
"""



import requests

headers = {
    'Host': 'm5.amap.com',
    'Connection': 'keep-alive',
    'Content-Length': '1115',
    'bx-umidtoken': 'S2gABVyCIiiVNXEijX0QoHVxfcneExKObnkqryvE2BlWERCAvw8Hm_HBzF6Uqqp_bB71_vC1nzTfH_IU_P1_D1KQlbPPvHjfl3Gs2yr-4YH-ri_jnG1HbL3sBgdZY096Hfg=',
    'charset': 'utf-8',
    'cookie': 'sessionid=3da63fzrjmx543litt5ih7qywr2qw6sn',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K10C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3189 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/7998 MicroMessenger/8.0.20.2100(0x28001439) Process/appbrand1 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'asac': '2A21B23KNLDPZGQEW2YO1I',
    'content-type': 'application/x-www-form-urlencoded',
    'sessionid': '3da63fzrjmx543litt5ih7qywr2qw6sn',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'mini-janus': '10%40sqkPu12Bloq0YoyCqRqQ6ncinCPVOLfNg69l%2FRNNsK7JEUUojlqfkhxMl5VNNN8wj%2F%2Fw7BR5x5%3D%3D',
    'Referer': 'https://servicewechat.com/wxbc0cf9b963bd3550/176/page-frame.html',
}

params = (
    ('xck', 'Vt7iRw2aHPe3/2vRkfAOaZkfCXvaCdgzU3iqNrrkvj1haOrj+5TungSLCdVYcTWRM2pNQ3IGZYeldVvggnyAvxBMdPDJiaIQaUXQix2KDUh5fw6h6lo5y/Jd9P04iHon9W4czn0RqGrVfFx93aqnHHVV92M/MgjLd1dyP84pyO8='),
    ('xck_channel', 'default'),
    ('_bx-m', '1'),
)

data = {
  'in': 'q/RAoU3xHwq9iUsgcm0pmWNzT3ruynPNI8/NwlEEQILfqL9Ps8Z0Zb+PZJsL6AOKvte6L4NtIj/TkfQDNA4nHXRvgNwV5Txd4TUawUcxNSQVvqTK7h8aWKo/ovcyxhjJdraEwdVqvPsdTu8xOschfYDMk7Fv/sqBGuHX/ICNWRTpKrziETuIuMOX9fFTe0Ws00qTes00g89mF7hrz0DfJ41hOtyF58cSrh+b7Rsbka+1ceEEGj0zIC2al5AChJFhbZm3FTqi//ZMkawoR6O+oS9glX21C2JVr5OVGiJEl1tHzQB38MQYeuM/NAk1I2XZhHinB2BxYgDpldAR6ow3I1ZHgD4gwWg8z1YD1CnW1hrIRAmRoF9sEnwqICnV+G5QDDcqbE71Y1ZI+NISN+FQ6HuH4f+8nk+nYKgrmBH5VeesgAqlqXfsDxHqCDDPe5ufMZ2HubkhiYLqajHWVCtJxEqWaRub2DjQX9aHEygU9F15wR5jYtP4SInYjR19ccMVD+GQPnf54pHEa7toROgelIbv2JRgb7OyKUKWS4eFFRWsHpOiA5UM3/sgrvgxrvRvQgiwcRm6F6Smo61vITl5HzbSd6QibTrEWiN0mS3HPcw1CWxqu4ZshXjGp9TizWprCUajp0CRihMDKMjW6AOBpdAfk0YHDqIuTm2yr58r/Odn2ByLlQbQhd2ozcr1nO6Hrhx+zxGcFJbpTISmgZFea4y3J8xEdxobp6vtnq24QKsAcqXR5kJz36Xn2Qu6pcdkJWRO6nIqFGyvq2j7VKjUDEpy/tfN7XRsYL3qSXFCzH+os+lLC5276Je4TU7ZcRySYagOHS8yKmtJY6W4LukXirHeuh9caop098WBD/18ihYDfHdM+k0ctX3ylgTdDqDIvGIen1SFB1QVaVWNr/RbiQkrcdHBNq9aOsiERvxV2tdClZPFnjLaliSiCJrqxnpVsIXZ1BzAqUA6OZiDUUMUN1Tqn1ruawawfQbJTi15ODhtteHVu2LtSUGyBnpoIjSsj/Knn+kVqJdNUeGo3Bnq7g=='
}
def sign():
    response = requests.post('https://m5.amap.com/ws/alice/activity/daily_sign/do_sign', headers=headers, params=params, data=data)

    # Note: original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    #response = requests.post('https://m5.amap.com/ws/alice/activity/daily_sign/do_sign?xck=Vt7iRw2aHPe3%2F2vRkfAOaZkfCXvaCdgzU3iqNrrkvj1haOrj%2B5TungSLCdVYcTWRM2pNQ3IGZYeldVvggnyAvxBMdPDJiaIQaUXQix2KDUh5fw6h6lo5y%2FJd9P04iHon9W4czn0RqGrVfFx93aqnHHVV92M%2FMgjLd1dyP84pyO8%3D&xck_channel=default&_bx-m=1', headers=headers, data=data)
    print(response.json())
    
if __name__=='__main__':
    sign()