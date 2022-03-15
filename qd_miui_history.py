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
        'cookie': 'wordpress_sec_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1648521042%7CFUNxTeWVbLkCP2FuOwuXHJS3ETIZVAq9loLjkUf3UsK%7C682070029882f581e43057823d2ccc17df258e0822f0f51a6b446b8274619ec1; _ga=GA1.2.1741035115.1646120001; _gid=GA1.2.612555610.1647311439; _gat=1; PHPSESSID=1j5kjcelkhv5n8fa0u5mab3qd0; wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1648521042%7CFUNxTeWVbLkCP2FuOwuXHJS3ETIZVAq9loLjkUf3UsK%7C72ffb67e721b3e38d2e942744c6c42b7ff86b12501b67209db4cae836c842d09',
    }

    data = {
      'action': 'epd_checkin'
    }

    response = requests.post('https://miuiver.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    print(response.json())

if __name__=='__main__':
    main()