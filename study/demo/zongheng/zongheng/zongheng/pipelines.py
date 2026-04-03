# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from zongheng.settings import mysql_local
class ZonghengPipeline:
    def open_spider(self,spider):
        self.con = pymysql.connect(**mysql_local)
        self.cur = self.con.cursor()
        print("爬虫启动")
    def process_item(self, item, spider):
        # print("管道中的数据",item)
        data_list = item['data_list']
        params = (
            data_list.get("author"),
            data_list.get("book_name"),  # 对应bookName
            data_list.get("nums"),
            data_list.get("content"),
            data_list.get("contentUrl"),  # 对应contentUrl
            data_list.get("book_url"),  # 对应bookUrl
            data_list.get("chapter_name"),  # 对应bookUrl
        )
        print(params)
        try:
            sql = "insert into zh (author,bookName,nums,content,contentUrl,bookUrl,chapter) values(%s,%s,%s,%s,%s,%s,%s)"
            self.cur.execute(sql,params)
            self.con.commit()
        except Exception as e:
            print(e)
        print("提交成功")
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.con.close()
