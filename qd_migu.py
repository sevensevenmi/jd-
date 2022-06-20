# -*- coding: UTF-8 -*-
# Desc: 咪咕音乐签到 v2.3.3
#每日签到 +（周三抽奖（可以抽到白金会员）&周三自动使用补签卡）+ 白金会员每月五号自动领取2张补签卡
# by 影。 	
#0 0 12 * * * *
# Time: 2021/3/10 上午9:58:14


import requests
import time
import json


# 填酷推skey
skey = 'e0193bea3ac1dc1edd397f4a31de7d05'
#填写自己是否为白金VIP 0不是/1是，目前咪咕音乐白金VIP可以每月领取2张补签卡
bjVIP = 0
# 填必要参数，前三个签到和抽奖页面都能抓
uid = '19126423'
channel = '0146921'
aversionid = 'DF948C8E93A9A68E6B9387A5D07AA0729599888994ECEE8A6396B8CE897FCD6E9CC8B8878EA4A8BE978E90D0877E9474C494878894A4A28C67C68DE98CAACB729494848B93A8A2B96396BA9FD0C5E3729994898A96A5A4916A9A889E'
#这个抓包抽奖连接"https://app.act.nf.migu.cn/MAC/activity3/nncj/takePrize?activityId=MAC_ZK_KF_NNCJ&token=xxxxxxxxx"打x的就是（周三点进去抽奖了才能抓到）
token = '8484010001330200584D6B55344E455A454D6B5177517A52434F4463774D54677A40687474703A2F2F70617373706F72742E6D6967752E636E2F6E303030312F403064666139633234633461353433663339343535333633653333386430373534030004058B8DB904000632323030323405001038616431313130343238306131356332FF0020CBE2C3262E275BAB68005E950A6DFD8422BE1978DC8DF9EDED9BE7B797301334'






#发送酷推
def push(title, content):
    url = "https://push.xuthus.cc/send/" + skey
    data = title + "\n" + content
    # 发送请求
    res = requests.post(url=url, data=data.encode('utf-8')).text
    # 输出发送结果
    print(res)


#获取北京时间
def getBeijinTime():
    hea = {'User-Agent': 'Mozilla/5.0'}
    url = r'http://time1909.beijing-time.org/time.asp'
    r = requests.get(url=url, headers=hea)
    if r.status_code == 200:
        result = r.text
        if "nday=5" in result and "nwday=3" not in result:
            if bjVIP == 1 :
                mouth_bqcard()
        elif "nday=5" not in result and "nwday=3" in result:
            chou_jiang()
        elif "nday=5"  in result and "nwday=3" in result:
            if bjVIP == 1 :
                mouth_bqcard()
            chou_jiang()
    else:
        push("【咪咕音乐】","获取当前时间失败")


#获取补签卡数量
def sign_card():
    target = 'https://u.musicapp.migu.cn/MIGUM3.0/user/sign-card/v1.0'
    headers = { "Host":"u.musicapp.migu.cn",
                "ua":"Android_migu",
                "uid":uid,
                "channel":channel,
                "aversionid":aversionid,
                "User-Agent":"Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 Mobile Safari/537.36 AndroidAmberV2.7.5 mobilemusic/7.1.1",
                "version":"7.1.1",
                "Origin":"https://h5.nf.migu.cn",
                "X-Requested-With":"cmccwm.mobilemusic",
                "Referer":"https://h5.nf.migu.cn/app/v3/p/native/whisper-sign/index.html",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}


    resp = requests.get(target, headers=headers).text
    print(resp)
    res = json.loads(resp)
    # 过滤条件
    if res['info'] == "操作成功":
        c = str(res["data"])
        a = int(c)
        print("当前补签卡数量:"+c+"张")
        if a != 0 :
            resign_reward(a)
    else:
        push("【咪咕音乐】\n获取补签卡数量出错","错误状态:" + res['info'])


#使用补签卡
def resign_reward(i):
    target = 'https://u.musicapp.migu.cn/MIGUM2.0/v1.0/user/resign-reward'
    headers = { "Host":"u.musicapp.migu.cn",
                "ua":"Android_migu",
                "uid": uid,
                "channel": channel,
                "aversionid": aversionid,
                "User-Agent":"Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 Mobile Safari/537.36 AndroidAmberV2.7.5 mobilemusic/7.1.1",
                "version":"7.1.1",
                "Origin":"https://h5.nf.migu.cn",
                "X-Requested-With":"cmccwm.mobilemusic",
                "Referer":"https://h5.nf.migu.cn/app/v3/p/native/whisper-sign/index.html",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}


    d = i
    while i > 0 :
        resp = requests.get(target, headers=headers).text
        print(resp)
        res = json.loads(resp)
        time.sleep(0.5)
        i -= 1
        # 过滤条件
    if res['info'] == "操作成功":
        b = float(str(res['data']['point'])) * d
        push("【咪咕音乐补签】\n" + "补签"+ str(d) + "次成功","补签获得成长值:" + str(b) )
    else:
        # push(推送标题,推送内容)
        push("【咪咕音乐补签】\n" + "补签失败\n" + "失败状态:" + res['info'], "请检查")


#会员每月补签卡领取
def mouth_bqcard():
    target = 'https://u.musicapp.migu.cn/MIGUM2.0/v1.0/user/vip-sign-card'
    headers = {"Host": "u.musicapp.migu.cn",
               "ua": "Android_migu",
               "uid": uid,
               "channel": channel,
               "User-Agent":"Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 Mobile Safari/537.36 AndroidAmberV2.7.5 mobilemusic/7.1.1",
               "Origin": "https://h5.nf.migu.cn",
               "Referer": "https://h5.nf.migu.cn/app/v3/p/native/whisper-sign/index.html"}


    resp = requests.get(target, headers=headers).text
    # 打印执行结果 此处打印后应当是string
    print(resp)
    # 将string转为 json 而后对json作判断 此处按需自行操作
    res = json.loads(resp)
    # 过滤条件
    if res['code'] == 200003:
        # push(推送标题,推送内容)
        push("【咪咕音乐】", "状态:" + res['info'])
    elif res['code'] == 000000:
        push("【咪咕音乐】", "状态:" + res['info'] + "\n已为您领取2张补签卡,将在周三抽奖时一并使用")
    else:
        # push(推送标题,推送内容)
        push("【咪咕音乐】", "状态:" + res['info'])


#周三抽奖
def chou_jiang():
    target = 'https://app.act.nf.migu.cn/MAC/activity3/nncj/takePrize?activityId=MAC_ZK_KF_NNCJ&token='+token
    headers = { "Host":"app.act.nf.migu.cn",
                "ua":"Android_migu",
                "uid":uid,
                "channel":channel,
                "aversionid":aversionid,
                "User-Agent": "Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 Mobile Safari/537.36 AndroidAmberV2.7.5 mobilemusic/7.1.1",
                "version":"7.1.1",
                "Origin":"https://h5.nf.migu.cn",
                "X-Requested-With":"cmccwm.mobilemusic",
                "Referer":"https://h5.nf.migu.cn/app/v3/p/native/whisper-sign/index.html",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}


    resp = requests.get(target,headers=headers).text
    # 打印执行结果 此处打印后应当是string
    print(resp)
    # 将string转为 json 而后对json作判断 此处按需自行操作
    res = json.loads(resp)
    # 过滤条件
    if res['code'] == "600001":
        push("【咪咕音乐周三抽奖】","状态:"+res['info'])
    elif res['code'] == "000000":
        push("【咪咕音乐周三抽奖】","状态:"+res['info']+"\n"+"抽奖结果:"+res['data'])
    elif res['code'] == "600003":
        push("【咪咕音乐周三抽奖】","状态:"+"本周"+res['info'])
    elif res['code'] == "600005":
        push("【咪咕音乐周三抽奖】","状态:"+"状态:"+res['info'])
    else:
        push("【咪咕音乐周三抽奖】\n"+"状态:"+res['info'] ,"抽奖失败,请检查")
    sign_card()


#主程序
def run():
    target = 'https://c.musicapp.migu.cn/MIGUM2.0/v2.0/user/sign-reward'
    headers = {"Host": "c.musicapp.migu.cn",
               "ua": "Android_migu",
               "uid": uid,
               "channel": channel,
               "User-Agent":"Mozilla/5.0 (Linux; Android 9; MI 6 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 Mobile Safari/537.36 AndroidAmberV2.7.5 mobilemusic/7.1.1",
               "Origin": "https://h5.nf.migu.cn",
               "Referer": "https://h5.nf.migu.cn/app/v3/p/native/whisper/index.html"}


    resp = requests.get(target, headers=headers).text
    print(resp)
    res = json.loads(resp)
    # 过滤条件
    if res['info'] == "操作成功":
        # push(推送标题,推送内容)
        push("【咪咕音乐】\n"+"签到成功\n"+"今日成长值:"+str(res['data']['point']),"连续签到天数:"+str(res['data']['continuousDays'])+"天" )
    else:
        # push(推送标题,推送内容)
        push("【咪咕音乐】\n"+"签到失败\n"+"失败状态:"+res['info'] ,"请检查")
    getBeijinTime()






def main_handler(event, context):
    run()


# 本地测试
if __name__ == '__main__':
    run()