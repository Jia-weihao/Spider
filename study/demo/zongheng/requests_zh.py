# @Time: 2026/4/3 10:13
# @Author :JiaWeiHao
# @File : requests_zh.py
# @Software: Pycharm
import requests
from lxml import etree


def first():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'ZHID=B054C5C19056BAEF3824BA8DC6291257; ver=2018; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; zh_visitTime=1775124893478; PassportCaptchaId=d8d44e87d5d321b9edb9b5e032329439; acw_tc=7b3975a217751825117205003e2bff51109d6fa056663e8d1e4f16ab77d307; zhffr=0; Hm_lvt_c202865d524849216eea846069349eb9=1775124894,1775182528; Hm_lpvt_c202865d524849216eea846069349eb9=1775182528; HMACCOUNT=897B4E72FFB1E23D',
    }

    response = requests.get(
        'https://book.zongheng.com/store/c0/c0/b0/u0/p1/v0/s1/t0/u0/i1/ALL.html',
        headers=headers,
    )

    html = etree.HTML(response.text)

    book_info_tags = html.xpath('//div[@class="bookinfo"]')
    # print(book_info_tags)
    for tag in book_info_tags:
        book_name = tag.xpath('./div[1]/a/text()')[0]
        book_url = tag.xpath('./div[1]/a/@href')[0]
        print(book_name, book_url)
        book_auth = tag.xpath('./div[2]/a[1]/text()')[0]
        print(book_auth)

def second():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://book.zongheng.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'ZHID=B054C5C19056BAEF3824BA8DC6291257; ver=2018; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; zh_visitTime=1775124893478; PassportCaptchaId=d8d44e87d5d321b9edb9b5e032329439; zhffr=0; Hm_lvt_c202865d524849216eea846069349eb9=1775124894,1775182528; HMACCOUNT=897B4E72FFB1E23D; acw_tc=7b3975b217751835724085454e5e3639fd9007a2f082d76cb7e1f8dceca6f2; Hm_lpvt_c202865d524849216eea846069349eb9=1775184524',
    }

    response = requests.get('https://www.zongheng.com/detail/1442070', headers=headers)
    cookie = {"Cookie":"ZHID=B054C5C19056BAEF3824BA8DC6291257; ver=2018; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22%24device_id%22%3A%2219d4d4afa751f6a-0e33614f042172-26061f51-2073600-19d4d4afa761764%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; zh_visitTime=1775124893478; PassportCaptchaId=d8d44e87d5d321b9edb9b5e032329439; zhffr=0; Hm_lvt_c202865d524849216eea846069349eb9=1775124894,1775182528; HMACCOUNT=897B4E72FFB1E23D; Hm_lpvt_c202865d524849216eea846069349eb9=1775184524"}
    mulu = requests.post("https://bookapi.zongheng.com/api/chapter/getChapterList", headers=headers,cookies=cookie,data={"bookId":"1442070"})
    data = mulu.json()

    html = etree.HTML(response.text)
    nums = html.xpath('//div[@class="book-info--nums"]/div[4]/span/text()')[0]
    print(nums)
    chapterList = data['result']['chapterList']
    for i in chapterList[0:5]:
        print(i["tome"]['tomeName'])
    # print(chapterList)

def third():
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

    response = requests.get(
        "https://read.zongheng.com/chapter/1442070/91519122.html",
        headers=headers,
    )
    html = etree.HTML(response.text)
    content = html.xpath('//div[@class="content"]/p/text()')
    text_content = "\n".join(content)
    print(text_content)
third()