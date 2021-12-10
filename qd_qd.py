import requests

headers = {
    'Host': 'hope.demogic.com',
    'Connection': 'keep-alive',
    'Content-Length': '735',
    'charset': 'utf-8',
    'sign': 'ff8080816f334552016f59fa1eaa7802',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2011K2C Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3165 MMWEBSDK/20211101 Mobile Safari/537.36 MMWEBID/6620 MicroMessenger/8.0.17.2040(0x28001133) Process/appbrand2 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'content-type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'Referer': 'https://servicewechat.com/wx1c0b429bf06403aa/16/page-frame.html',
}

data = {
  'memberId': 'ff8080816f42e508016f6e80401d1cfa',
  'cliqueId': '-1',
  'cliqueMemberId': '-1',
  'useClique': '0',
  'enterpriseId': 'ff8080816f334552016f59fa1eaa7802',
  'unionid': 'og_4Fv2UfYoQ7s3QYJst9nOwGewQ',
  'openid': 'o4Hns4o5PSQSKI6NZEFdi0RuXaxw',
  'random': '7045785',
  'appid': 'wx1c0b429bf06403aa',
  'transId': 'wx1c0b429bf06403aa2021-12-09 16:13:05',
  'sign': 'b037bec617231dbed1fd87a61d63c801',
  'timestamp': '2021-12-09 16:13:05',
  'gicWxaVersion': '3.8.21',
  'launchOptions': '{"path":"pages/customView/customView","query":{"share":"0","pageId":"ff80808170a6186f0170bd1271f47033"},"scene":1179,"referrerInfo":{"appId":"wxa0517b283f6c8742"},"chatType":1,"mode":"default","apiCategory":"default"}'
}

response = requests.post('https://hope.demogic.com/gic-wx-app/member_sign.json', headers=headers, data=data).text
print(response)