"""
const $ = new Env("MIUI历史版本签到");
MIUI历史版本签到

cron:
0 7 * * * qd_miui_history.py
"""



import requests

cookies = {
    'wordpress_sec_f82bae77b4519a305f00e3f66136abf7': 'zq1121734772%7C1649991583%7CfV9buiUC9OrWiuxM2dUzyH4DYG5soU3p8xL8yqGZRgn%7C2566c6da3e2145278cf58137313b609e78281e756268c26f9e61b652fce3daf3',
    '_ga': 'GA1.2.124877360.1648781979',
    '_gid': 'GA1.2.1917683348.1648781979',
    '_gat': '1',
    'PHPSESSID': 'rs8rnrdrj725tto611iagujs11',
    'wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7': 'zq1121734772%7C1649991583%7CfV9buiUC9OrWiuxM2dUzyH4DYG5soU3p8xL8yqGZRgn%7Ccec4c0e1bfe1ff1b9de9574b58e350bbb3fbbce3e2c0132ab0cd60166b0fcf74',
}

headers = {
    'authority': 'miuiver.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55',
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
    # Requests sorts cookies= alphabetically
    # 'cookie': 'wordpress_sec_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1649991583%7CfV9buiUC9OrWiuxM2dUzyH4DYG5soU3p8xL8yqGZRgn%7C2566c6da3e2145278cf58137313b609e78281e756268c26f9e61b652fce3daf3; _ga=GA1.2.124877360.1648781979; _gid=GA1.2.1917683348.1648781979; _gat=1; PHPSESSID=rs8rnrdrj725tto611iagujs11; wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1649991583%7CfV9buiUC9OrWiuxM2dUzyH4DYG5soU3p8xL8yqGZRgn%7Ccec4c0e1bfe1ff1b9de9574b58e350bbb3fbbce3e2c0132ab0cd60166b0fcf74',
}

data = {
    'action': 'epd_checkin',
}
def main():
    response = requests.post('https://miuiver.com/wp-admin/admin-ajax.php', headers=headers, cookies=cookies, data=data)
    print(response.json())

if __name__=='__main__':
    main()