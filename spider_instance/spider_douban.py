# -*- coding: utf-8 -*-
# Python3.5爬取豆瓣top250
import time
import requests
from bs4 import BeautifulSoup
import xlsxwriter

base_url = 'https://movie.douban.com/top250?start={0}&filter='
# print(url_list)
h = {
    'User-Agent': '(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36)',
}

# 电影排名、电影名称、评分、总的电影信息
# 电影排名、电影名称、评分、总的电影信息
movie_rating = []
movie_name = []
movie_score = []
data_list = []
try:
    print('正在爬取豆瓣top250数据，请耐心等待。。。')
    for k in range(0, 250, 25):
        url = base_url.format(k)
        response = requests.get(url, headers=h)
        body = response.text
        soup = BeautifulSoup(body, 'html.parser')
        # print(soup)
        span_rating_list = soup.findAll('em', attrs={'class': ''})
        span_name_list = soup.findAll('span', attrs={'class': 'title'})
        span_score_list = soup.findAll('span', attrs={'class': 'rating_num'})

        for span_rating in span_rating_list:   # 电影排名
            span_rating = span_rating.string
            movie_rating.append(span_rating)
        # print(movie_rating)
        for span_name in span_name_list:   # 电影名称
            span_name = span_name.string
            if span_name.find('/') == -1:
                span_name = span_name
                movie_name.append(span_name)
        # print(movie_name)
        for span_score in span_score_list:  # 电影评分
            span_score = span_score.string
            movie_score.append(span_score)
        # print(movie_score)
    data_list.append(movie_rating)
    data_list.append(movie_name)
    data_list.append(movie_score)
    # print(data_list)
    # 写入Excel
    workbook = xlsxwriter.Workbook('豆瓣top250.xlsx')
    worksheet = workbook.add_worksheet('豆瓣top250数据分析')
    bold = workbook.add_format({'bold': True})
    col = ('排名', '电影名称', '评分', '读取时间')
    tsp = time.strftime('%Y%m%d %H:%M:%S', time.localtime())
    for v in range(0, 4):
        worksheet.write(0, v, col[v], bold)   # i写入列名
    worksheet.write(1, 3, tsp)

    for i in range(0, 250):
        for j in range(0, 3):
            worksheet.write(i+1, j, data_list[j][i])
            worksheet.write(i+1, j, data_list[j][i])
            worksheet.write(i+1, j, data_list[j][i])
            worksheet.set_column(i, 1, 20)  # 设置第二列列宽为20

    workbook.close()
    print('数据已保存到豆瓣top250.xlsx')

except Exception as e:
    print(e)



