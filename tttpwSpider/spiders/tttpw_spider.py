import scrapy
# from scrapy.selector import Selector
from ..items import TttpwspiderItem
import time

class CnblogsSpider(scrapy.Spider):
    name = "tttpw"
    allowed_domains = ["ivsky.com"]     #不允许越站
    start_urls = [
        "http://www.ivsky.com/tupian/shishangnvhai_t19861/"
    ]

    def parse(self, response):
        papers = response.xpath(".//div[@class='il_img']")
        num = 0
        for paper in papers:
            time.sleep(0.2)
            print(paper)
            num += 1
            url = paper.xpath(".//a/img/@src").extract()[0]
            title = paper.xpath(".//a/img/@alt").extract()[0]
            index = num
            print(url, title, index)
            item = TttpwspiderItem(url=url, title=title, index=index)
            yield  item
        # 使用Selector的re（）抽取下一页
        # next_page = Selector(response).re(u'<a class="page-next" href="(\S*)">下一页</a>')
        next_page = response.xpath(".//a[@class='page-next']/@href").extract()[0]
        print(next_page)
        if next_page:
            yield scrapy.Request(url="http://www.ivsky.com" + next_page, callback=self.parse)
        else:
            print("end")
