# @Time: 2026/4/1 13:15
# @Author :JiaWeiHao
# @File : xpath.py
# @Software: Pycharm
import pandas as pd
from lxml import etree

# xpath 相对于正则更适合解析网页数据

"""
 常用表达式
 /    从根节点选取下一级
 //   不考虑位置匹配节点
 .    选择当前节点
 ..   选择父节点
 @    选取属性
"""

with open("网页.html", "r", encoding="utf-8") as f:
    text = f.read()

html = etree.HTML(text)

# # 找到标签获取文本
# print(tag[0].text.strip())
# # 直接获取文本
# text = tag[0].xpath("./text()")
# print(text)
#
# text2 = html.xpath("//body")[0]
# print(text2.text)
#
# span = html.xpath("//span/text()")
# print(span)

# span1 = html.xpath('//div[@data-v-7f856186=""][@class="m-v-sm info"]//span[@data-v-7f856186=""][1]/text()')
# areas = html.xpath('//div[@class="m-v-sm info"][1]/span[1]/text()')
# print(areas)

fileNames = html.xpath('//h2[@class="m-b-sm"]/text()')
res_scores = html.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()')
scores = [i.strip() for i in res_scores]
areas = html.xpath('//div[@class="m-v-sm info"][1]/span[1]/text()')
print(len(areas))
df = pd.DataFrame({
    "电影名称":fileNames,
    "分数":scores,
    "地区":areas
})
df.to_excel("文本/电影信息.xlsx",index=False)