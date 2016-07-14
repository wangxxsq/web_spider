# -*- coding: utf-8 -*-
import urllib.request
from urllib.parse import urlencode
import http.cookiejar

# response = urllib.request.urlopen("http://www.baidu.com")
# html_data = response.read()
# print(html_data)

# req = urllib.request.Request("http://www.baidu.com")
# response = urllib.request.urlopen(req)
# html_data = response.read()
# print(html_data)

body = {
    "username": 'wangxinxinsq@sina.cn',
    "password": 'wxx199121@'
}

# POST
# requ_body = urlencode(body).encode()
# url = 'http://weibo.com/?sudaref=www.114la.com&retcode=6102'
# request = urllib.request.Request(url, requ_body)
# response = urllib.request.urlopen(request)
# print(response.read())

# GET
requ_body = urlencode(body).encode()
url = 'http://weibo.com/?sudaref=www.114la.com&retcode=6102'
url = url + '?'+str(requ_body)
request = urllib.request.Request(url, requ_body)
response = urllib.request.urlopen(request)
print(response.read())

