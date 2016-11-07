# 模拟浏览器访问
import urllib.request

url = 'http://www.douban.com/'
# h = {
#     'User-Agent': '(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
# }

# 复杂的请求头
h2 = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml. *-*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': '(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Host': 'www.douban.com',
    'DNT': '1'
}
requ = urllib.request.Request(url=url, headers=h2)
resp = urllib.request.urlopen(requ)
data = resp.read().decode()
print(resp.info())





