# 简单爬虫1
import urllib.request

url = 'https://www.douban.com/'
resp = urllib.request.urlopen(url)
data = resp.read().decode()
print(data)
print(resp.geturl())
print(resp.info())
print(resp.getcode())