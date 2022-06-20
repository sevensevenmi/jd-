"""
const $ = new Env("MIUI历史版本签到");
MIUI历史版本签到

cron:
0 7 * * * qd_miui_history.py
"""



import requests

cookies = {
    'wordpress_sec_f82bae77b4519a305f00e3f66136abf7': 'zq1121734772%7C1656914904%7CsXofpYWRHRrp9qmfw0Ov7v5j4Wyuc0HZEJwbGLpYdm2%7Cc8cf07b6eed1ed98d4ab59c4c7b238fc2fed2732e64a56621ea075d3dfc894f0',
    '_ga': 'GA1.2.1597023974.1652952910',
    '_gid': 'GA1.2.283634491.1655705300',
    '_gat': '1',
    'PHPSESSID': '3s4dh0rt2n6vof7ot50abjk63u',
    'wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7': 'zq1121734772%7C1656914904%7CsXofpYWRHRrp9qmfw0Ov7v5j4Wyuc0HZEJwbGLpYdm2%7C696014d906e70ed0e3116338a68d279c1a0aaee7768b4a40b643e77cd2256803',
}

headers = {
    'authority': 'miuiver.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'wordpress_sec_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1656914904%7CsXofpYWRHRrp9qmfw0Ov7v5j4Wyuc0HZEJwbGLpYdm2%7Cc8cf07b6eed1ed98d4ab59c4c7b238fc2fed2732e64a56621ea075d3dfc894f0; _ga=GA1.2.1597023974.1652952910; _gid=GA1.2.283634491.1655705300; _gat=1; PHPSESSID=3s4dh0rt2n6vof7ot50abjk63u; wordpress_logged_in_f82bae77b4519a305f00e3f66136abf7=zq1121734772%7C1656914904%7CsXofpYWRHRrp9qmfw0Ov7v5j4Wyuc0HZEJwbGLpYdm2%7C696014d906e70ed0e3116338a68d279c1a0aaee7768b4a40b643e77cd2256803',
    'dnt': '1',
    'origin': 'https://miuiver.com',
    'referer': 'https://miuiver.com/user-profile/?action=credit',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
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