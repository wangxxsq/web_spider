# -*- coding: utf-8 -*-
import urllib.request
import urllib.error

__author__ = 'xinxin'


# 抓取糗事百科某一页所有热门段子

page = 1  # 某页
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
headers = {'User-Agent': user_agent}

url = 'http://www.qiushibaike.com/hot/page/'+str(page)


try:
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    response_body = response.read().decode()
    print("RESP_BODY:", response_body)

except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)





