#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# from pip._vendor import requests
import requests
from bs4 import BeautifulSoup

x = 1


def get_img(self):
    # 获取网页内容
    page_url = "https://www.dbmeinv.com/dbgroup/show.htm?cid=4&pager_offset=%s" % self
    print('url地址：', page_url)
    page_response = requests.get(page_url)
    # print('请求结果：', page_response)
    page_html = page_response.text
    # print('页面内容: ', page_response.text)

    # 解析页面,解析对象
    soup = BeautifulSoup(page_html, 'html.parser')

    # 获取所有图片标签内容
    imgs = soup.find_all('img')
    print('图片url总数：', imgs.__len__())
    # 申明图片变量
    # x = 1

    for i in imgs:
        # 获取所有链接
        link = i.get('src')
        # 下载图片
        imgs_res = requests.get(link)

        global x
        # nonlocal x
        # 写图片
        if imgs_res.status_code == 200:
            # with open('images\%s.jpg' % x, 'wb') as f:
            with open('C:/Users/Administrator/Desktop/images' + str(self) + '%s.jpg' % x, 'ab') as f:
                print(f.name)
                f.write(imgs_res.content)
                x += 1


for i in range(1, 10):
    get_img(i)
