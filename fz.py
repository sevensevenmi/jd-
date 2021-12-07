


"""
const $ = new Env("飞猪签到");

飞猪签到

cron:
0 7 * * * fz.py
"""

# -*- coding: utf8 -*-
import time

import requests
import json

ts = str(int(round(time.time()*1000)))

url1 = "http://amdc.m.taobao.com/amdc/mobileDispatch?appkey=12663307&deviceId=YY6IFVTYD8cDADKlmrQjUvC%2F&platform=android&v=5.0"
def start2():
    headers = {
        'authority': 'h5api.m.taobao.com',
        'sec-ch-ua': '""',
        'accept': 'application/json',
        'dnt': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-mobile': '?1',
        'user-agent': 'jdapp;android;10.2.2;11;4373169333533346-5633466623367363;model/M2011K2C;addressid/6511073045;aid/47a9353de3df2c76;oaid/043970b71db85df4;osVer/30;appBuild/91077;partner/xiaomi001;eufv/1;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 11; M2011K2C Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045735 Mobile Safari/537.36 Edg/96.0.4664.55',
        'sec-ch-ua-platform': '',
        'origin': 'https://market.m.taobao.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://market.m.taobao.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'cna=QPgdGqCzGWoCAW65J3zDO5Xw; lgc=tb9469208_2012; tracknick=tb9469208_2012; enc=PmTJBWkslRVuuWHoKHqaX64xGFJCD3Dv6oQzDbRQ2nyOrcFJK4h%2BisHMb4fW21vX9xHtrdYHwTuzF%2BzHEfTcBw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; t=0020ab7fa301f94d5e4374d323283827; _m_h5_tk=a5392d9e7183f5f9ebda91cf00d4a5cc_1638856480349; _m_h5_tk_enc=fbcf3220eda6e242ed94c492db353a50; _samesite_flag_=true; cookie2=1ae82361afb834deafcfea92eb50111b; _tb_token_=e448fe3bd86ae; sgcookie=E100Q1lebd5HxFHP94vi41hq33sT3euY2Xq%2Fl5UBqyQQ8mLHp7gY2xp1x5fBLpql64770vixZlwMOT3NhJal%2FsN2xI%2Bgv3f9d3tw9bkfpeyqrrc%3D; ockeqeudmj=hJ9gG1I%3D; _w_tb_nick=tb9469208_2012; munb=864645313; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BKK8XV%2BtavCSCczqkAv1qQA%3D%3D; _w_app_lg=0; unb=864645313; uc3=lg2=URm48syIIVrSKA%3D%3D&nk2=F5RMHUKiIFDbcl7oZv8%3D&id2=W89IsXwomGzA&vt3=F8dCvUmnPDw59cV1rxo%3D; csg=799d3a8e; ntm=0; cancelledSubSites=empty; cookie17=W89IsXwomGzA; dnk=tb9469208_2012; skt=e9cb48643f714b06; uc4=id4=0%40Wey5FdZ9e%2FiqQwpnYPgTuA9YTxI%3D&nk4=0%40FY4HWGi3I4Hy5mAbZaXUNN7QGummQm8Q3A%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=238; _nk_=tb9469208_2012; cookie1=Vy6%2FHir86QDbPRpRDPKmng7UqcFJopzrwvPhaw3aZHI%3D; l=eBryc0W7gkp4XCvpBOfwourza77OSIRAguPzaNbMiOCPOQ5p5jYPW6IUcpY9C3GRh6zyR35EzuM7BeYBq_C-nxvTa0NwiIDmn; tfstk=cPrNB09RzGIZWzofyciV5Y8dEenOZYZ04_ktSPR6E0ZDo20GiCOxKfMTzzLADVf..; mt=ci=0_1; uc1=cookie21=UIHiLt3xTwwM1Oej1w%3D%3D&existShop=false&cookie14=Uoe3f4iSSY7Mkw%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D; isg=BDU19adquFrsitzm6ClCygY5UbHvsunE_ocC3bda8Kz7jleAfwONlNRI3FS4zgF8',
    }

    params = (
        ('type', 'originaljson'),
        ('api', 'mtop.trip.serverless.api.gateway'),
        ('v', '2.0'),
        ('data',
         '{"source":"UNKNOWN-Web","fcId":"266555914156571313","fcGroup":"fc-fl-ssf","fcName":"fc-index","fcData":"{\\"sffParams\\":{\\"sff_oss_url\\":\\"https://fliggy-sff.oss-cn-hangzhou.aliyuncs.com/local/h5-mileage-play/1.9.6/service.json\\",\\"sff_schema\\":\\"\\",\\"defaultParams\\":{\\"actionType\\":\\"NON_FLIGGY\\",\\"signInActivityId\\":391},\\"returnAll\\":false,\\"needLogin\\":true}}","fcConfig":"{\\"disasterRecover\\":false}","h5Version":"1.9.6"}'),
        ('ttid', '201300@travel_h5_3.1.0'),
        ('appKey', '12574478'),
        ('t', '1638846364847'),
        ('sign', '03e26b0bdea6a6176d2b8bc3f609c770'),
    )

    response = requests.get('https://h5api.m.taobao.com/h5/mtop.trip.serverless.api.gateway/2.0', headers=headers,params=params).text
    print(response)

def start1():
    headers = {
        'authority': 'h5api.m.taobao.com',
        'sec-ch-ua': '""',
        'accept': 'application/json',
        'dnt': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-mobile': '?1',
        'user-agent': 'jdapp;android;10.2.2;11;4373169333533346-5633466623367363;model/M2011K2C;addressid/6511073045;aid/47a9353de3df2c76;oaid/043970b71db85df4;osVer/30;appBuild/91077;partner/xiaomi001;eufv/1;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 11; M2011K2C Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045735 Mobile Safari/537.36 Edg/96.0.4664.55',
        'sec-ch-ua-platform': '',
        'origin': 'https://market.m.taobao.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://market.m.taobao.com/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'cna=QPgdGqCzGWoCAW65J3zDO5Xw; lgc=tb9469208_2012; tracknick=tb9469208_2012; enc=PmTJBWkslRVuuWHoKHqaX64xGFJCD3Dv6oQzDbRQ2nyOrcFJK4h%2BisHMb4fW21vX9xHtrdYHwTuzF%2BzHEfTcBw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; t=0020ab7fa301f94d5e4374d323283827; _m_h5_tk=a5392d9e7183f5f9ebda91cf00d4a5cc_1638856480349; _m_h5_tk_enc=fbcf3220eda6e242ed94c492db353a50; _samesite_flag_=true; cookie2=1ae82361afb834deafcfea92eb50111b; _tb_token_=e448fe3bd86ae; sgcookie=E100Q1lebd5HxFHP94vi41hq33sT3euY2Xq%2Fl5UBqyQQ8mLHp7gY2xp1x5fBLpql64770vixZlwMOT3NhJal%2FsN2xI%2Bgv3f9d3tw9bkfpeyqrrc%3D; ockeqeudmj=hJ9gG1I%3D; _w_tb_nick=tb9469208_2012; munb=864645313; WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BKK8XV%2BtavCSCczqkAv1qQA%3D%3D; _w_app_lg=0; unb=864645313; uc3=lg2=URm48syIIVrSKA%3D%3D&nk2=F5RMHUKiIFDbcl7oZv8%3D&id2=W89IsXwomGzA&vt3=F8dCvUmnPDw59cV1rxo%3D; csg=799d3a8e; ntm=0; cancelledSubSites=empty; cookie17=W89IsXwomGzA; dnk=tb9469208_2012; skt=e9cb48643f714b06; uc4=id4=0%40Wey5FdZ9e%2FiqQwpnYPgTuA9YTxI%3D&nk4=0%40FY4HWGi3I4Hy5mAbZaXUNN7QGummQm8Q3A%3D%3D; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=238; _nk_=tb9469208_2012; cookie1=Vy6%2FHir86QDbPRpRDPKmng7UqcFJopzrwvPhaw3aZHI%3D; l=eBryc0W7gkp4XCvpBOfwourza77OSIRAguPzaNbMiOCPOQ5p5jYPW6IUcpY9C3GRh6zyR35EzuM7BeYBq_C-nxvTa0NwiIDmn; tfstk=cPrNB09RzGIZWzofyciV5Y8dEenOZYZ04_ktSPR6E0ZDo20GiCOxKfMTzzLADVf..; mt=ci=0_1; uc1=cookie21=UIHiLt3xTwwM1Oej1w%3D%3D&existShop=false&cookie14=Uoe3f4iSSY7Mkw%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D; isg=BDU19adquFrsitzm6ClCygY5UbHvsunE_ocC3bda8Kz7jleAfwONlNRI3FS4zgF8',
    }

    params = (
        ('type', 'originaljson'),
        ('api', 'mtop.user.getUserSimple'),
        ('v', '1.0'),
        ('data', '{"h5Version":"1.9.6"}'),
        ('needLogin', 'true'),
        ('sessionOption', 'AutoLoginOnly'),
        ('jsonpIncPrefix', 'liblogin'),
        ('ttid', '201300@travel_h5_3.1.0'),
        ('appKey', '12574478'),
        ('t', '1638846364846'),
        ('sign', 'bc0ca666f3703c4347dd893d865d1686'),
    )

    response = requests.get('https://h5api.m.taobao.com/h5/mtop.user.getUserSimple/1.0', headers=headers, params=params).text
    print(response)

if __name__=='__main__':
    start1();
    start2();
