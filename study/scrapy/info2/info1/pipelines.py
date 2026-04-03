# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from info1.settings import mysql_local
class Info1Pipeline:
    # 爬虫开始的时候就启动
    def open_spider(self,spider):
        print("爬虫启动")
        self.conn = pymysql.connect(**mysql_local)
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        dataList = item["dataList"]
        sql = "INSERT INTO films(fileName,score,areas) VALUES (%s,%s,%s);"
        self.cur.executemany(sql, dataList)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()


class ExcelPipeline:
    # 爬虫开始的时候就启动
    def open_spider(self,spider):
        self.data_list = []
    def process_item(self, item, spider):
        # 存储一次数据
        # df = pd.DataFrame(data=item["dataList"],columns=["电影名称","分数","地区"])
        # df.to_excel("D:\Program Files (x86)\code\spider\study\文本\电影内容.xlsx",index=False)
        temp_list = item["dataList"]
        self.data_list.extend(temp_list)
        return item

    def close_spider(self,spider):
        df = pd.DataFrame(data=self.data_list, columns=["电影名称", "分数", "地区"])
        df.to_excel("D:\Program Files (x86)\code\spider\study\文本\电影内容.xlsx",index=False)