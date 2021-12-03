"""
const $ = new Env("定时重启猫");
在 1 3 5 7 13 17 23 的56分重启猫
定时重启猫

路由器账号密码
CMCCAdmin
aDm8H%MdA
cron:
56 1,3,5,7,13,17,23 * * * cq.py
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import urllib.request

username = "CMCCAdmin"
password = "aDm8H%MdA"
chrome_options = Options()
chrome_options.add_argument('--headless') # 16年之后，chrome给出的解决办法，抢了PhantomJS饭碗
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')  # root用户不加这条会无法运行
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.get("http://192.168.8.1/getpage.gch?pid=1002&nextpage=manager_dev_restart_t.gch")
driver.get("http://192.168.8.1/")
time.sleep(1)

driver.execute_script('document.getElementById("username").value="";')
time.sleep(1)
driver.find_element(By.NAME,"username").send_keys(username)
driver.execute_script('document.getElementById("logincode").value="";')
driver.find_element(By.NAME,"logincode").send_keys(password)
driver.find_element(By.XPATH,"/html/body/div/div[3]/div/div/div/div/form/div[4]/a[1]").click()
for i in range(10):
    print(driver.title)
driver.get("http://192.168.8.1/getpage.gch?pid=1002&nextpage=manager_dev_restart_t.gch")
driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div[3]/div[2]/table/tbody/tr[1]/td/input").click()
driver.find_element(By.XPATH,"/html/body/div[5]/table/tbody/tr[3]/td/input[1]").click()
for i in range(10):
    print("success restart!!!")

time.sleep(180)
t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
bip = urllib.request.urlopen('http://ifconfig.me/ip').read()
#ip = str(bip, encoding="utf-8")
ip = bytes.decode(bip)
with open("/ql/log/sevensevenmi_jd-_cq/cqrecord.txt", 'a') as file_object:
    file_object.write(t)
    file_object.write('---重启成功---出口ip:')
    file_object.write(ip)
    file_object.write('\n')

driver.close()
info = t+'---重启成功---出口ip: '+ip+'\n'   
print(info)

