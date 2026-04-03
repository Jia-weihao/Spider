import scrapy

from info1.items import Info1Item

class FilmSpider(scrapy.Spider): # 继承爬虫，可以调用爬虫方法
    name = "film"
    allowed_domains = ["xxxx"] # 允许的域名
    start_urls = [f"https://ssr1.scrape.center/page/{num}" for num in range(1,11)] # 要爬取的网站 一定要有

    def parse(self, response):
        # xpath 需要转换成xpath对象的形式
        # text = response.text
        # html = etree.HTML(text)
        # fileNames = html.xpath('//h2[@class="m-b-sm"]/text()')
        # res_scores = html.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()')
        # scores = [i.strip() for i in res_scores]
        # areas = html.xpath('//div[@class="m-v-sm info"][1]/span[1]/text()')
        # print("xpath",areas,fileNames,scores)
        #  scrapy的response自动兼容xpath不过是Selector对象集成了xpath的解析方式，需要通过getall()获取所需的数据，注意不需要进行xpath对象的转换了
        fileNames = response.xpath('//h2[@class="m-b-sm"]/text()').getall()
        res_scores = response.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()').getall()
        scores = [i.strip() for i in res_scores]
        areas = response.xpath('//div[@class="m-v-sm info"][1]/span[1]/text()').getall()
        # print("Selector",fileNames,scores,areas)
        item = Info1Item()
        # print(item)
        # print(dict(item))
        data_list = list(zip(fileNames,scores,areas))
        # print(data_list)
        # return item
        item["dataList"] = data_list
        # 在scarpy里面通过yield返回不用return
        yield item

