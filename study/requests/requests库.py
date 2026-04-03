# @Time: 2026/4/1 17:09
# @Author :JiaWeiHao
# @File : requests库.py
# @Software: Pycharm
import requests

# 添加请求头
url = "http://httpbin.org/get"

# 添加请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://ssr1.scrape.center/page/2',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
# 添加query参数
params = {
    "key": "value",
    "key2": "value2",
}
# 添加cookie  或者在 headers里面
cookie = ""

# 添加超时时间
# res = requests.get(url,headers = headers,params = params,cookies = cookie,timeout = s)

# 是否允许重定向 allow_redirects = True / False

# 代理IP
# proxies = {"http":"xxx.xxx.xxx:xxxx","https":"xxx.xxx.xxx:xxxx"}
# ,proxies = proxies
# res = requests.get(url,headers = headers,params = params,cookies = cookie)
# print(res.text)

# 提交表单数据
# url = "http://httpbin.org/post"
# data = {"key":"value","key2":"value2"}
# res = requests.post(url,data = data,headers = headers)
# print(res.text)

# 提交JSON数据
url = "http://httpbin.org/post"
json = {
    "key": "value",
    "key2": "value2",
}
res = requests.post(url, json=json, headers=headers, cookies=cookie)
print(res.text)

# verify = False 忽略证书验证