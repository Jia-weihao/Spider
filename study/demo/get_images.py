# @Time: 2026/3/30 16:00
# @Author :JiaWeiHao
# @File : get_images.py.py
# @Software: Pycharm
import os.path

import requests
import re

# 获取写入一张图片函数
def get_one_iamge(url,name):
    if not os.path.exists("图片"):
        os.makedirs("图片")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
    }
    # 请求图片
    res =  requests.get(url,headers = headers)

    # 构建图片路径
    file_path = os.path.join("图片", f"{name}.jpg")

    # 写入图片
    with open(file_path, "wb") as f:
        f.write(res.content)

# 获取多张图片url方法
def get_many_images(url):
    # 获取整页html结构
    html = requests.get(url)
    # 获取本页所有的图片地址数组
    urls = re.findall('"(https.*?)"',html.text)
    # 函数返回数组
    return urls

# 获取多页的图片
def get_images(url_path,start,end):
    for pageNumber in range(start,end+1):
        page_url = url_path.format(pageNumber)

        urls = get_many_images(page_url)

        for index,url in enumerate(urls):
            get_one_iamge(url,f"{pageNumber}_{index}")


if __name__ == "__main__":
    get_images("https://ssr1.scrape.center/page/{}",1,10)