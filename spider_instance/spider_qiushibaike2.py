import re
import urllib.request
from urllib.error import URLError


class QiuShiBaiKe(object):

    def __init__(self):     # 初始化变量(页数， 每页的所有段子信息， 程序是否运行状态标识)
        self.page = 1
        self.message = []
        self.enable = False
        self.pattern = re.compile(
            '<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<div class="stats"'
            '.*?i class="number">(.*?)</i>(.*?)</span>.*?<span class="dash">.*?i class="number">(.*?)</i>(.*?)</a>',
            re.S)

    def get_pagelist(self, page):  # 抓取对应页数的所有段子，添加到列表种
        try:
            h = {
                'User-Agent': '(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
            }
            baseurl = 'http://www.qiushibaike.com/hot/page/'
            url = baseurl + str(page)
            requ = urllib.request.Request(url, headers=h)
            response = urllib.request.urlopen(requ)
            content = response.read().decode('utf-8')
            item_list = re.findall(self.pattern, content)

            page_list = []
            for item in item_list:
                img = re.search('img', item[1])
                if not img:
                    text = re.sub('<(.*?)>', '', item[1].strip())
                    page_list.append([item[0], text, item[2], item[4]])
            return page_list

        except URLError as e:
            print('error:', e.reason)
            return None

    def load_page(self):  # 加载下一页
        if self.enable is True:
            if len(self.message) < 2:   # page小于2（此时正读取某页最后一条段子）
                page_list = self.get_pagelist(self.page)
                if page_list:
                    self.message.append(page_list)
                    self.page += 1

    def get_onepage(self, page, page_list):
        for paragraph in page_list:
            input_info = input()
            self.load_page()
            if input_info == 'Q':
                self.enable = False
                return
            print('{0}, {1}, {2}, {3}, {4}'.format(page, paragraph[0], paragraph[1], paragraph[2], paragraph[3]))

    def run(self):   # 程序运行...
        print('正在读取糗事百科热门段子...')
        print('按回车读取新段子，按Q退出')
        self.enable = True
        self.load_page()
        nowpage = 0   # 控制当前页
        while self.enable:   # 取出最新元素后，并删除
            if len(self.message) > 0:
                page_list = self.message[0]
                nowpage += 1
                del self.message[0]
                self.get_onepage(nowpage, page_list)
if __name__ == '__main__':
    spider = QiuShiBaiKe()
    spider.run()





