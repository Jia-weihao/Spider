import scrapy
import json

from study.demo.zongheng.zongheng.zongheng.items import ZonghengItem


class ZhSpider(scrapy.Spider):
    name = "zh"
    # allowed_domains = ["book.zongheng.com"]
    # start_urls = ["https://book.zongheng.com"]

    def start_requests(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://www.zongheng.com/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            # 'Cookie': 'ZHID=B054C5C19056BAEF3824BA8DC6291257; ver=2018; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; zh_visitTime=1775124893478; PassportCaptchaId=d8d44e87d5d321b9edb9b5e032329439; zhffr=0; Hm_lvt_c202865d524849216eea846069349eb9=1775124894,1775182528; HMACCOUNT=897B4E72FFB1E23D; acw_tc=276aedfb17751944143243985eb9aedd1648fc18f481c5fd2e8b6a8d6abdf9; Hm_lpvt_c202865d524849216eea846069349eb9=1775194430',
        }
        url = "https://book.zongheng.com/store/c0/c0/b0/u0/p1/v0/s1/t0/u0/i1/ALL.html"
        yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        book_info_tags = response.xpath('//div[@class="bookinfo"]')
        for tag in book_info_tags[0:1]:
            book_name = tag.xpath("./div[1]/a/text()").getall()[0]
            book_url = tag.xpath("./div[1]/a/@href").getall()[0]
            book_author = tag.xpath("./div[2]/a[1]/text()").getall()[0]
            print(book_name, book_url, book_author)
            # 请求二级路由
            headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Referer": "https://book.zongheng.com/",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
                "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                # 'Cookie': 'ZHID=B054C5C19056BAEF3824BA8DC6291257; ver=2018; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; zh_visitTime=1775124893478; PassportCaptchaId=d8d44e87d5d321b9edb9b5e032329439; zhffr=0; Hm_lvt_c202865d524849216eea846069349eb9=1775124894,1775182528; HMACCOUNT=897B4E72FFB1E23D; acw_tc=7b3975b217751835724085454e5e3639fd9007a2f082d76cb7e1f8dceca6f2; Hm_lpvt_c202865d524849216eea846069349eb9=1775184524',
            }
            print("发起首页请求")
            book_info = {
                "book_name": book_name,
                "author": book_author,
                "book_url": book_url,
            }
            yield scrapy.Request(
                book_url,
                headers=headers,
                callback=self.parse_second,
                meta={"book_info": book_info},
            )

    def parse_second(self, response):
        print("请求二级路由")
        book_info = response.meta["book_info"]

        nums = response.xpath(
            '//div[@class="book-info--nums"]/div[4]/span/text()'
        ).getall()[0]
        book_id = response.url.split("/")[-1].replace(".html", "")
        api_url = "https://bookapi.zongheng.com/api/chapter/getChapterList"
        post_data = {"bookId": book_id}
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://www.zongheng.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "referer": "https://www.zongheng.com/",
            "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            # 'cookie': 'ZHID=B054C5C19056BAEF3824BA8DC6291257; ver=2018; zh_visitTime=1775124893478; PassportCaptchaId=d8d44e87d5d321b9edb9b5e032329439; zhffr=0; Hm_lvt_c202865d524849216eea846069349eb9=1775124894,1775182528; HMACCOUNT=897B4E72FFB1E23D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lpvt_c202865d524849216eea846069349eb9=1775200343',
        }
        cookies = {
            "ZHID": "B054C5C19056BAEF3824BA8DC6291257",
            "ver": "2018",
            "zh_visitTime": "1775124893478",
            "PassportCaptchaId": "d8d44e87d5d321b9edb9b5e032329439",
            "zhffr": "0",
            "Hm_lvt_c202865d524849216eea846069349eb9": "1775124894,1775182528",
            "HMACCOUNT": "897B4E72FFB1E23D",
            "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D",
            "Hm_lpvt_c202865d524849216eea846069349eb9": "1775200343",
        }
        print("发起post请求")
        content_url = (
            "https:" + response.xpath('//div[@class="book-info--btn"]/a[1]/@href').get()
        )
        book_info["book_id"] = book_id
        book_info["content_url"] = content_url
        book_info["nums"] = nums
        yield scrapy.FormRequest(
            url=api_url,
            headers=headers,
            formdata=post_data,
            callback=self.parse_chapter,
            meta={"book_info": book_info},
            cookies=cookies,
        )

    def parse_chapter(self, response):
        # print(response.meta["book_info"])
        book_info = response.meta["book_info"]
        text_content = json.loads(response.text)
        content = text_content["result"]["chapterList"][0]["chapterViewList"]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://book.zongheng.com/",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            # 'Cookie': 'ZHID=B054C5C19056BAEF3824BA8DC6291257; ver=2018; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; zh_visitTime=1775124893478; PassportCaptchaId=d8d44e87d5d321b9edb9b5e032329439; zhffr=0; Hm_lvt_c202865d524849216eea846069349eb9=1775124894,1775182528; HMACCOUNT=897B4E72FFB1E23D; acw_tc=7b3975b217751835724085454e5e3639fd9007a2f082d76cb7e1f8dceca6f2; Hm_lpvt_c202865d524849216eea846069349eb9=1775184524',
        }
        # print(content)
        read_domain  = book_info["content_url"].split("chapter/")[0] + "chapter/"

        for i in content:
            # print("开始请求内容")
            chapter_id = i["chapterId"]
            chapter_name = i["chapterName"]
            read_url = f"{read_domain}{book_info['book_id']}/{chapter_id}.html"
            book_info_copy = book_info.copy()
            book_info_copy["chapter_name"] = chapter_name
            book_info_copy["contentUrl"] = read_url
            yield scrapy.Request(
                url=read_url,
                headers=headers,
                callback=self.parse_content,
                meta={"book_info": book_info_copy},
            )

    def parse_content(self, response):
        # print("请求内容中")
        book_info = response.meta["book_info"]
        content = response.xpath('//div[@class="content"]/p/text()').getall()
        text_content = "\n".join(content)
        book_info["content"] = text_content
        item = ZonghengItem()
        item["data_list"] = book_info
        print("请求到内容了")

        yield item
