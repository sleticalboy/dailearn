import logging

import scrapy
from scrapy.http import Response
from scrapy.settings import BaseSettings

from ..items import MatplotItem

logger = logging.getLogger(__name__)


class MatplotSpider(scrapy.Spider):
    name = "matplot"
    allowed_domains = ["matplotlib.org"]
    start_urls = ["https://matplotlib.org/stable/gallery/index"]

    custom_settings = {
        'foo': 'hey u foo!'
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def update_settings(cls, settings: BaseSettings):
        # 方式一、spider 自定义属性 custom_settings，update_settings() 方法会自动读取并更新
        super().update_settings(settings)
        logger.warning(f"my settings 'foo': {settings.attributes.get('foo')}")
        # 方式二、通过此方法注入自定义属性
        settings.set('fo', 'hey u son of a beach!', priority='spider')
        logger.warning(f"my settings 'fo': {settings.attributes.get('fo')}")
        pass

    # 自定义爬虫入口
    def start_requests(self):
        # 默认是读取 self.start_urls 作为入口
        return super().start_requests()

    def parse(self, response: Response, **kwargs):
        detail_urls = response.css('div.sphx-glr-thumbcontainer>p>a::attr(href)').extract()
        self.log(f'parse() sample size: {len(detail_urls)} -> {detail_urls[0]}')
        for sample_url in detail_urls:
            yield scrapy.Request(response.urljoin(sample_url), callback=self.parse_detail)
        pass

    def parse_detail(self, response: Response):
        item = MatplotItem()
        item['url'] = response.url

        title = response.css('section.sphx-glr-example-title>h1::text').get()
        self.log(f'parse_detail() sample title: {title}')
        item['title'] = title

        img_urls = item.setdefault('img_urls', [])
        file_urls = item.setdefault('file_urls', [])
        sample_codes = item.setdefault('sample_codes', [])
        for img_url in response.css('img.sphx-glr-single-img::attr(src)').getall():
            img_url = response.urljoin(img_url)
            img_urls.append(img_url)
            file_urls.append(img_url)
            pass

        for code_url in response.css('div.sphx-glr-download-python>p>a::attr(href)').getall():
            code_url = response.urljoin(code_url)
            sample_codes.append(code_url)
            file_urls.append(code_url)
            pass
        yield item
