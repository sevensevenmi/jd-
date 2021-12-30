"""
const $ = new Env("科技玩家签到");
科技玩家签到

cron:
0 9 * * * qd_kjwj.py
"""


import requests

def test():
    cookies = {
        '_ga': 'GA1.1.1397880877.1637140892',
        'Hm_lvt_56cd01307dc3c795bb735a379cdc5e35': '1637221780,1637313224,1637546848,1637636563',
        '_ga_82DHH1SNHE': 'GS1.1.1639547708.23.1.1639547765.0',
        'b2_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lmtlaml3YW5qaWEuY29tIiwiaWF0IjoxNjQwNjY5NjcxLCJuYmYiOjE2NDA2Njk2NzEsImV4cCI6MTY0MTQ0NzI3MSwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMTAxMyJ9fX0.ITHmMZV_mBuKdTzJEKUO8ngqK2hpe9FINgBTtj4NQ8w',
        'wordpress_logged_in_319c49a2ee14e4fe558a6454d059be91': 'user1013_670%7C1640842471%7Ch5QJCoxzWYw8j2TE1EPLq2D4ajxGaX1aFWHX87LvMnp%7Ce254472397ea0b1536da53488d93b885d9b13e31ef21f79e66e82c69627b6a24',
        'wprus_user_pending_async_actions': 'HYYeyZd9Vw3wELlMqrGx0ac08rEMXtAzleE5r7i0V1Cc%2BJTyqc6RTdyFRC4gW26LC7yjbMIADsz8A_d1uXWu2Q%3D%3D',
    }

    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
        'Accept': 'application/json, text/plain, */*',
        'DNT': '1',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lmtlaml3YW5qaWEuY29tIiwiaWF0IjoxNjQwNjY5NjcxLCJuYmYiOjE2NDA2Njk2NzEsImV4cCI6MTY0MTQ0NzI3MSwiZGF0YSI6eyJ1c2VyIjp7ImlkIjoiMTAxMyJ9fX0.ITHmMZV_mBuKdTzJEKUO8ngqK2hpe9FINgBTtj4NQ8w',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://www.kejiwanjia.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.kejiwanjia.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    response = requests.post('https://www.kejiwanjia.com/wp-json/b2/v1/userMission', headers=headers, cookies=cookies).text

    print("恭喜！您今天获得了"+response+"积分")
   
if __name__=='__main__':
    test().
