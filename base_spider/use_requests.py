'''Python requesst库'''
import requests

'''基本get请求'''
r = requests.get('https://www.python.org')
print(r.status_code)
print(r.text)

'''带参数get请求'''
url = 'https://www.python.org'
payload = {'key1': 'vlaue1', 'key2': 'value2'}
r = requests.get(url, params=payload)
print(r.status_code)
print(r.text)

'''发送post请求'''
payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.status_code)
print(r.text)