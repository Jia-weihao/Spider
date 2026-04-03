# @Time: 2026/3/31 17:52
# @Author :JiaWeiHao
# @File : excel表格.py
# @Software: Pycharm

import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ssr1.scrape.center/"

res = requests.get(url)

names = re.findall('class="m-b-sm">(.*?)</h2>',res.text)
scores = re.findall('m-b-n-sm">\n(.*?)</p>',res.text)


new_scores = [i.strip() for i in scores]
df = pd.DataFrame()
df["电影名称"] = names
df["评分"] = new_scores


df.to_excel("电影信息.xlsx",index=False)