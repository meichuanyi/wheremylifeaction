import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Referer': 'http://wheremylife.cn/home.htm'
}
session = requests.Session()

url = 'http://wheremylife.cn/user/login'

payload = {
    'email': input(),
           'password': input()
    }

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Referer': 'http://wheremylife.cn/home.htm'
}
s = session.post(url, data=payload, headers=headers)
s2 = session.post('http://wheremylife.cn/user/resetBook', headers=headers)
print('打卡成功！')
