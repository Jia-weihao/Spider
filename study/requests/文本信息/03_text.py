# @Time: 2026/3/30 16:59
# @Author :JiaWeiHao
# @File : 03_text.py
# @Software: Pycharm

import requests
import re


url = "https://ssr1.scrape.center/"

res = requests.get(url)

titles = re.findall('<h2 data-v-7f856186="" class="m-b-sm">(.*?)</h2>',res.text)
scores = re.findall('m-b-n-sm">\n(.*?)</p>',res.text)
# 列表推导式进行操作
new_scores = [i.strip() for i in scores]
for i in titles:
    print(i)

for i in new_scores:
    print(i.strip())



