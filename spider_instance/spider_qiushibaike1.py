# -*- coding:utf-8 -*-
# 抓取糗事百科24小时第一页段子（用户名，内容，好笑数，评论数）
import re
import urllib.request
from urllib.error import URLError

url = 'http://www.qiushibaike.com/hot/page/1'
# headers验证
h = {
    'User-Agent': '(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
}
try:
    requ = urllib.request.Request(url, headers=h)
    response = urllib.request.urlopen(requ)
    content = response.read().decode('utf-8')
# 正则匹配（此正则匹配目前糗百最新网页内容）
    pattern = re.compile(
        '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<div class="stats"'
        '.*?i class="number">(.*?)</i>(.*?)</span>.*?<span class="dash">.*?i class="number">(.*?)</i>(.*?)</a>',
        re.S)
    items = re.findall(pattern, content)

    # 过滤掉内容中图片
    for item in items:
        img = re.search('img', item[1])
        if not img:
            print(item[0], item[1].strip(), item[2], item[3])

except URLError as e:
    print('error', e.reason)


