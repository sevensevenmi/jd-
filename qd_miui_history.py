"""
const $ = new Env("MIUI历史版本签到");
MIUI历史版本签到

cron:
0 7 * * * qd_miui_history.py
"""



import requests

cookies = {
    'wordpress_sec_f82bae77b4519a305f00e3f66136abf7': 'zq1121734772%7C1652151818%7CcoInMw1WWd0iAkvfC79mX5ZQu7cKGdz4IBKFmfy2HUc%7Cb9ab98aaf6b9e0611ff9f7dd73dfac14969ead750363c2dbf041cf47aadd75f0',
    '_ga': 'GA1.2.124877360.1648781979',
    'PHPSESSID': 'tmf674g7cl60gpsnb8havkehas',
    'wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7': 'zq1121734772%7C1652151818%7CcoInMw1WWd0iAkvfC79mX5ZQu7cKGdz4IBKFmfy2HUc%7Cf693620a625221817e11a277d38c4f01f8de01c2b09dc51a133aba34222e8c69',
}

headers = {
    'authority': 'miuiver.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'wordpress_sec_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1652151818%7CcoInMw1WWd0iAkvfC79mX5ZQu7cKGdz4IBKFmfy2HUc%7Cb9ab98aaf6b9e0611ff9f7dd73dfac14969ead750363c2dbf041cf47aadd75f0; _ga=GA1.2.124877360.1648781979; PHPSESSID=tmf674g7cl60gpsnb8havkehas; wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1652151818%7CcoInMw1WWd0iAkvfC79mX5ZQu7cKGdz4IBKFmfy2HUc%7Cf693620a625221817e11a277d38c4f01f8de01c2b09dc51a133aba34222e8c69',
    'dnt': '1',
    'origin': 'https://miuiver.com',
    'referer': 'https://miuiver.com/user-profile/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'action': 'epd_checkin',
}


def main():
    response = requests.post('https://miuiver.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
    print(response.json())

if __name__=='__main__':
    main()