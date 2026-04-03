import requests
import re
url = "http://www.baidu.com"


res = requests.get(url)
 # 设置编码
res.encoding = "utf-8"

html = res.content.decode("utf-8")

# print(re.findall("<title>(.*?)</title>",html))
# print(res.status_code)
# print(res.text)

res1.encoding = 'utf-8'
html1 = res1.content.decode("utf-8")
print(res1.text)


