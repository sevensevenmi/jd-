"""
const $ = new Env("MIUI历史版本签到");
MIUI历史版本签到

cron:
0 7 * * * qd_miui_history.py
"""



import requests

def main():
    headers = {
        'authority': 'miuiver.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://miuiver.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://miuiver.com/user-profile/',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'wordpress_sec_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1645691264%7CYctgzTPfM7OxGMfuoKurUT5nN9p2g6MZLMrrVF6yQs9%7C113b08d380c71279d9964f5450b27b9cb82247c0290779fb198dbc10cac6c9a2; PHPSESSID=phc3dlbemcj5lee4sjt8gdfks1; wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1645691264%7CYctgzTPfM7OxGMfuoKurUT5nN9p2g6MZLMrrVF6yQs9%7C33b9f333359b5525b877b956275b8b381f93ed331e15af660e45c4f84b8a6701',
    }

    data = {
      'action': 'epd_checkin'
    }

    response = requests.post('https://miuiver.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    data=response.json()
    if "登录" in data["msg"]:
        print("cookie 失效")
    else:
        print(data["msg"])

if __name__=='__main__':
    main()