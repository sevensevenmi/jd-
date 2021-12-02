"""
const $ = new Env("公网出口IP");
公网出口IP

每小时获取公网出口IP

cron:
*/60 * * * * ip.py
"""

import urllib.request
import time

t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
bip = urllib.request.urlopen('http://ifconfig.me/ip').read()
#ip = str(bip, encoding="utf-8")
ip = bytes.decode(bip)
with open("/opt/ip.txt", 'a') as file_object:
    file_object.write(t)
    file_object.write('----出口ip: ')
    file_object.write(ip)
    file_object.write('\n')
info = t+'----出口ip: '+ip+'\n'   
print(info)
