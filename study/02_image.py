# @Time: 2026/3/27 13:50
# @Author :JiaWeiHao
# @File : 02_image.py
# @Software: Pycharm

# 实例网站 https://ssr1.scrape.center/
import requests

def get_one_image():
    # url = "https://ssr1.scrape.center"
    url = "https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@464w_644h_1e_1c"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
              }

    res = requests.get(url , headers = headers)

    print(res)  # 获取response对象

    with open("test.jpg", "wb") as f:
        f.write(res.content) # 获取二进制数据用content、获取文本数据用text


def get_iamges(url):
