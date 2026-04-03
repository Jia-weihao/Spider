import scrapy

from info1.items import Info1Item


class FilmSpider(scrapy.Spider):  # 继承爬虫，可以调用爬虫方法
    name = "film"

    # allowed_domains = ["xxxx"] # 允许的域名
    # start_urls = [f"https://ssr1.scrape.center/page/{num}" for num in range(1,11)] # 要爬取的网站 一定要有

    # 重写start_request方法 因为默认只支持get请求，不能进行post所以一般要重写，同时也可以通过重写加上请求头之类的操作
    def start_requests(self):
        # get请求
        # for url in [f"https://ssr1.scrape.center/page/{num}" for num in range(1,6)]:
        #     # scrapy.Request 发起请求获取response通过callback传给用来解析数据的方法也就是parse
        #     headers = {
        #         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
        #     }
        #     yield scrapy.Request(url=url,callback=self.parse)

        # data = {"data1":"data1","data2":"data2","data3":"data3"}
        # url = "https://httpbin.org/post"
        # yield scrapy.FormRequest(url,formdata=data,callback=self.parse)

        url = "https://console-test.desktops.tingyutech.com/node/api/v1/desktop/list?page=1&size=10"
        headers = {
            "authorization":"eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0aWNrZXQiOiJjb25zb2xlX1B6c2lzRE9qQm1iS1d0eFRPZmMtMSIsImlhdCI6MTc3NTAwOTU1MiwiZXhwIjoxNzc1NjE0MzUyfQ.NpEHfUWo01O5CgYKMkwVgN2J9Jn4tgmJQazNC3KwlcOCTlzNcbhpsFHakvDGvUrUcqKMZDPTmccsTGIRIi6eiA",
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
        }
        yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        pass

