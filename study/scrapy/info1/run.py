# @Time: 2026/4/2 09:41
# @Author :JiaWeiHao
# @File : run.py
# @Software: Pycharm
# 爬虫运行文件
# 直接运行该文件即可启动爬虫程序
from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'film'])