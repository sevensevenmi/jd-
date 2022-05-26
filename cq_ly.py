"""
const $ = new Env("定时重启路由");
在 11 23 的58分重启路由
定时重启路由

路由器账号密码
CMCCAdmin
aDm8H%MdA
cron:
58 5,11,17,23 * * * cq_ly.py
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import urllib.request


passwd = "1121734772"
chrome_options = Options()
chrome_options.add_argument('--headless') # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://192.168.68.1/")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/div/div/div[1]/input").send_keys(passwd)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div[4]/div[2]/button/span/i").click()

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/button[2]/span').click()
time.sleep(3)
for i in range(5):
    print(driver.find_element(By.XPATH, '/html/body/div[6]/div/p').text)


time.sleep(90)
t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
bip_4 = urllib.request.urlopen('http://4.ipw.cn/').read()
#ip = str(bip, encoding="utf-8")
ip = bytes.decode(bip_4)
print(ip)
with open("/ql/data/log/sevensevenmi_jd-_cq_ly/cq_lyrecord.txt", 'a') as file_object:
    file_object.write(t)
    file_object.write('---重启成功---出口ip:')
    file_object.write(ip)
    file_object.write('\n')

driver.close()
info = t+'---重启成功---出口ip: '+ip+'\n'
print(info)




