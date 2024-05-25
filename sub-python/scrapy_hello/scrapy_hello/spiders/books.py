import sys

import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor

from ..items import BookItem


# -t: basic crawl csvfeed xmlfeed
# scrapy genspider -t basic books books.toscrape.com
# scrapy crawl books -o out/books.csv
class BooksSpider(scrapy.Spider):
    # 爬虫的名字
    name = "books"
    # 允许爬取哪些域名
    allowed_domains = ["books.toscrape.com"]
    # 爬虫起始点 (start_request()方法)
    start_urls = ["https://books.toscrape.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # 记录已处理了多少页数据
        self.pages = 0

    # 页面解析：生成器函数
    def parse(self, response: Response, **kwargs):
        self.pages += 1
        # 解析数据
        for item in response.css('article.product_pod'):
            name = item.xpath('./h3/a/@title').extract_first()
            price = item.css('p.price_color::text').extract_first()
            # print(f'=== name: {name}, price: {price}', file=sys.stderr)
            # 方式一、使用 dict 存储数据
            # yield {'name': name, 'price': price}
            # 方式二、使用自定义 Item 存储数据
            book = BookItem()
            book['name'] = name
            book['price'] = price
            yield book
            pass
        # 获取下一页连接 ul.paget li.next a::attr(href)
        # 方式一、通过 css 选择器
        # next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        # print(f'=== next url: {next_url}', file=sys.stderr)
        # if next_url and self.pages < 2:
        #     # 构造下一个 requst 并返回
        #     yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
        # 方式二、通过 LinkExtractor
        linker = LinkExtractor(restrict_css='ul.pager li.next', tags=('a', 'area'), attrs=('href',))
        links = linker.extract_links(response)
        print(f'=== next url: {links}', file=sys.stderr)
        if links and len(links) > 0 and self.pages < 2:
            yield scrapy.Request(links[0].url, callback=self.parse)
        pass
