import requests
import re
url = "http://www.baidu.com"

url1 = "https://console-test.desktops.tingyutech.com/statistics"

res = requests.get(url)
res.encoding = "utf-8"

html = res.content.decode("utf-8")

# print(re.findall("<title>(.*?)</title>",html))
# print(res.status_code)
# print(res.text)

res1 = requests.get(url1)
res1.encoding = 'utf-8'
html1 = res1.content.decode("utf-8")
print(res1.text)