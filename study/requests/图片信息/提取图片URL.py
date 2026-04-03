# @Time: 2026/3/30 15:11
# @Author :JiaWeiHao
# @File : 提取图片URL.py
# @Software: Pycharm

import requests
import re


url = "https://ssr1.scrape.center/"

html = requests.get(url)

# print(html.text)

text = re.findall('src="(https.*?)"',html.text)

for i in text:
    print(i)

def getURLS(url):
    html = requests.get(url)
    urls = re.findall('src="(https.*?)"',html.text)
    return urls

