import sys

import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor

from ..items import BookItem


# -t: basic crawl csvfeed xmlfeed
# scrapy genspider -t basic books books.toscrape.com
# scrapy crawl books -o out/books.csv
# scrapy crawl books -o 'out/%(name)s-%(time)s.xml'
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
            book_url = item.css('div.image_container>a::attr(href)').get()
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_detail)
            pass
        # 获取下一页连接 ul.paget li.next a::attr(href)
        # 方式一、通过 css 选择器
        # next_url = response.css('ul.pager li.next a::attr(href)').get()
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

    @classmethod
    def parse_detail(cls, response: Response):
        img_url = response.css('#product_gallery>div>div>div>img::attr(src)').get()
        img_url = response.urljoin(img_url)

        main = response.css('div.product_main')
        name = main.xpath('./h1/text()').get()
        price = main.css('p.price_color::text').get()
        review_rating = main.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')

        table = response.css('table.table.table-striped')
        upc = table.xpath('.//tr[1]/td/text()').get()
        stock = table.xpath('.//tr[last()-1]/td/text()').re_first(r'\((\d+) available\)')
        review_num = table.xpath('.//tr[last()]/td/text()').get()

        # 方式一、使用 dict 存储数据
        # yield {'name': name, 'price': price}
        # 方式二、使用自定义 Item 存储数据
        book = BookItem()
        book['name'] = name
        book['price'] = price
        book['review_rating'] = review_rating
        book['review_num'] = review_num
        book['upc'] = upc
        book['stock'] = stock
        book['img_url'] = img_url

        img_urls = book.setdefault('file_urls', [])
        img_urls.append(img_url)
        yield book
