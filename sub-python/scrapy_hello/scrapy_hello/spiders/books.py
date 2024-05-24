import sys

import scrapy
from scrapy.http import Response


# -t: basic crawl csvfeed xmlfeed
# scrapy genspider -t basic books books.toscrape.com
# scrapy crawl books -o out/books.csv
class BooksSpider(scrapy.Spider):
    # 爬虫的名字
    name = "books"
    # 允许爬取哪些域名
    allowed_domains = ["books.toscrape.com"]
    # 起始 url
    start_urls = ["https://books.toscrape.com"]

    # 页面解析：生成器函数
    def parse(self, response: Response, **kwargs):
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            # print(f'=== name: {name}, price: {price}', file=sys.stderr)
            yield {'name': name, 'price': price}
        # 下一页 # ul.paget li.next a::attr(href)
        next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
        print(f'=== next url: {next_url}', file=sys.stderr)
        if next_url:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
        pass
