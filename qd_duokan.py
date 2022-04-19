import requests
import time

t = int(time.time())
headers = {
    'Cookie': 'mi_version=V13.0.4.1.23.DEV;_m=1;_n=1;platform=android;app_id=DuoKan;build=701030000;channel=Y6WBAG;first_version=660220131;version_name=7.1.3;device_model=M2012K10C;device_name=ares;os_version=12;os_sdk=31;manufacturer=Xiaomi;random_id=af0506a3746bfbfe108c05c9b902c928;reg_id=qDBBiLht25gxz%2FD2tTVsMBSunRugIQ3XgL3XikaLbmM%3D;personal_recommend=1;personalise_rec=1;store_pref=;user_type=2;book_level=0_1;fiction_level=0_1;_t=1649730498;_c=40751;oaid=38db8373afe8a67d;device_id=D006300074bcbca64d6110b0d4408f201ed18d8;token=_3YRwf_g5HG8LMsqyTqxW_WFpoY8nm5sxr_TGkGep1YqCLetOAkxVpRhr6_3Wn78uUKqHk_je9ZVBx3wxhHdbA..;',
    # 'Accept-Encoding': 'gzip,deflate',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 12; M2012K10C Build/SP1A.210812.016)',
    'Host': 'www.duokan.com',
    'Connection': 'Keep-Alive',
    # 'Content-Length': '22',
}
t = int(time.time())
c = 0
t_device_id = f"D006300074bcbca64d6110b0d4408f201ed18d8&{t}"
for index, one in enumerate(t_device_id):
    c = (c * 131 + ord(one)) % 65536


data = {
    '_t': t,
    '_c': c,
}

response = requests.post(
    'https://www.duokan.com/checkin/v0/checkin', headers=headers, data=data)
print(response.json())
