# @Time: 2026/3/27 13:50
# @Author :JiaWeiHao
# @File : 02_image.py
# @Software: Pycharm
import os

# 实例网站 https://ssr1.scrape.center/

import requests

from 提取图片URL import getURLS


def get_one_image(url,name):
    if not os.path.exists("图片"):
        os.makedirs("图片")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
              }

    res = requests.get(url , headers = headers)

    file_path = os.path.join("图片", f"{name}.jpg")

    with open(file_path, "wb") as f:
        f.write(res.content) # 获取二进制数据用content、获取文本数据用text

# url = f"https://ssr1.scrape.center/"
#
# urls = getURLS(url)
#
# for index,img in enumerate(urls):
# get_one_image(img,index)

def get_many_images(url_path,start,end):
     for pageNum in range(start,end+1):
         page_url = url_path.format(pageNum)

         urls = getURLS(page_url)

         for index, url in enumerate(urls):
             get_one_image(url,f"{pageNum}_{index}.jpg")

url = "https://ssr1.scrape.center/page/{}"
get_many_images(url,1,10)


