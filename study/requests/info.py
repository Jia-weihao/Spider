# @Time: 2026/3/31 18:11
# @Author :JiaWeiHao
# @File : info.py
# @Software: Pycharm
import re

import pandas as pd
import requests
from lxml import etree
from config import mysql_local
import pymysql

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

class FilmInfo:
    def __init__(self):
        self.conn =  pymysql.connect(**mysql_local)
        self.cur = self.conn.cursor()

    # 1、获取响应数据
    def get_res(self,url):
        res = requests.get(url,headers=HEADERS,timeout=10).text
        return res

    # 2、解析数据
    def parse_data_re(self,text):
        # re--正则的方式解析数据
        '''
            fileNames = re.findall('<h2 data-v-7f856186="" class="m-b-sm">(.*?)</h2>',text)
            new_scores =  re.findall('m-b-n-sm">\n(.*?)</p>',text)
            scores = [i.strip() for i in new_scores]
            print(scores,fileNames)
        '''
        # xpath--xpath的方式解析数据
        html = etree.HTML(text)
        fileNames = html.xpath('//h2[@class="m-b-sm"]/text()')
        res_scores = html.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()')
        scores = [i.strip() for i in res_scores]
        areas = html.xpath('//div[@class="m-v-sm info"][1]/span[1]/text()')
        return fileNames,scores,areas
    #3、存储
    def save_data(self,fileNames,scores,areas):
        df = pd.DataFrame()
        df['电影名称'] = fileNames
        df['评分'] = scores
        df['地区'] = areas
        df.to_excel('文本/电影评分.xlsx',index=False)

    def save_data_mysql(self,fileNames,scores,areas):
        data_list = list(zip(fileNames,scores,areas))
        sql = "INSERT INTO films(fileName,score,areas) VALUES (%s,%s,%s);"
        self.cur.executemany(sql,data_list)
        self.conn.commit()

    def main(self,start,end):
        fileNameList = []
        scoresList = []
        areasList = []
        # 获取多页
        for i in range(start,end+1):
            url = f"https://ssr1.scrape.center/page/{i}"
            text = self.get_res(url)
            fileNames, scores, areas = self.parse_data_re(text)
            # 拼接每一页的数据
            fileNameList.extend(fileNames)
            scoresList.extend(scores)
            areasList.extend(areas)
            self.save_data_mysql(fileNames, scores, areas)

        # 存储多页数据

        self.save_data(fileNameList, scoresList, areasList)

if __name__ == "__main__":
    film = FilmInfo()
    film.main(1,10)
