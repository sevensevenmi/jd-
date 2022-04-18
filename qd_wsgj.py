"""
const $ = new Env("网速管家");
网速管家

cron:
0 7 * * * qd_wsgj.py
"""



import requests
def sign():
    headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjZmY2M4OGQwNjA3YTlkN2IwNDIxM2NhOTM4ZjcxYjQ1MmU5ZDYwYmQxMGMyMjg1NTk3YzcyYjNmOGJmYmQyMzJlZjU4ODM0YzQyNDZlZjU1In0.eyJhdWQiOiIyIiwianRpIjoiNmZjYzg4ZDA2MDdhOWQ3YjA0MjEzY2E5MzhmNzFiNDUyZTlkNjBiZDEwYzIyODU1OTdjNzJiM2Y4YmZiZDIzMmVmNTg4MzRjNDI0NmVmNTUiLCJpYXQiOjE2NDYxOTI0NTcsIm5iZiI6MTY0NjE5MjQ1NywiZXhwIjoxNjc3NzI4NDU3LCJzdWIiOiIyMTQ4NiIsInNjb3BlcyI6W119.mTicYaOrpoRl_0wCz8I2UCjdA8r1ABIUtPRlRsJeY1-D5PKsOBSIUd-IIcIUTOBivvjps9EKS-sujTAgZHvJI4AF05QRKxkyNIRpMiwYtuzZUmxB8WsT1saIKntRJf49TrtStM6CUTaH9rHVMZZn7S_bAhD1F-7i3fAlfGB_kzntQR0kN8pioiJe2bJF_7h50YAtSpv_eRiwfaKx_KgESeKrtCn6HHwFNcgbOgqdsC6bvXL-DPqPj4_sYiI-uEgFngPb5UCkDuXd50_xpLVA0auWFy4wE7kLYncaMQHcogDJbI3c7ijpGyxX_4C_85JqCI3ipmGUCfGrZ4VE0sk5qXSwi4wIfLzpF0pr7ZI1zIxycrSiQNVDpJzBLRZTdhBaJNoobuJm9DVbi2cXLVgutmtxbljnQWTkvnltLjZOtM8xMu0uDfCF1jyvHb44KU7UmfIHFnQhiC7bAlIb_rWAd7CPCBIx7rRO8k_1ksJ_BT_Xmi9mqFjcfcHFdyVe-Dn8EhNO-eQJ-gDOuVBaKBM6W4k_hDcYoPV2xfJmfMZL1Z2cQ-BZU8LGvVjUN1pNcm8XENY67q25jlTXG-1bGToPWCef565K_QreNYfM75jG895IURzcYM7gEQtYhGQtpue5OlTqx-z_3wz0U1S0c41DUsmU56X1V2HXIUhEmGXsTe4',
        'Accept': 'application/json',
        'App-Source': 'android',
        'App-VersionCode': '132',
        'User-Agent': 'speedtest/6.9.2',
        'Content-Length': '0',
        'Host': 'forge.speedtest.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
    }

    response = requests.post('https://forge.speedtest.cn/api/v2/signv2', headers=headers)
    print(response.json())

if __name__=='__main__':
    sign()