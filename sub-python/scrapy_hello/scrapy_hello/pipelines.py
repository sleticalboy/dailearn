# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import logging

import scrapy
from itemadapter import ItemAdapter
from scrapy.crawler import Crawler
from scrapy.exceptions import DropItem
from scrapy.pipelines import files

from .items import BookItem, MatplotItem

logger = logging.getLogger(__name__)


# 自定义 pipeline manager
class PipelineManager(scrapy.pipelines.ItemPipelineManager):

    # 记录当前爬虫的名字
    _spider_name = ''

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        cls._spider_name = crawler.spider.name
        logger.info(f'======== {cls} => spider: {cls._spider_name}')
        return cls.from_settings(crawler.settings, crawler)

    @classmethod
    def _get_mwlist_from_settings(cls, settings):
        from scrapy.utils.conf import build_component_list
        # 根据爬虫名字获取 ITEM_PIPELINES 配置
        compdict = settings.getwithbase("ITEM_PIPELINES_ME").get(cls._spider_name, {})
        return build_component_list(compdict=compdict)


# 自定义 pipeline
# 1、写入文件、数据库
# 2、数据清洗（去重、去损、去过期）
# 3、统计
class BookPricePipeline:
    _rate = 8.539
    _mapper = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
    }

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        # 从配置中读取参数并传递给初始化函数，注意：不能返回 None，否则会报如下错误
        # Traceback (most recent call last):
        #   File "{site-packages}/twisted/internet/defer.py", line 2003, in _inlineCallbacks
        #     result = context.run(gen.send, result)
        #   File "{site-packages}/scrapy/crawler.py", line 158, in crawl
        #     self.engine = self._create_engine()
        #   File "{site-packages}/scrapy/crawler.py", line 172, in _create_engine
        #     return ExecutionEngine(self, lambda _: self.stop())
        #   File "{site-packages}/scrapy/core/engine.py", line 101, in __init__
        #     self.scraper = Scraper(crawler)
        #   File "{site-packages}/scrapy/core/scraper.py", line 109, in __init__
        #     self.itemproc: ItemPipelineManager = itemproc_cls.from_crawler(crawler)
        #   File "{site-packages}/scrapy/middleware.py", line 90, in from_crawler
        #     return cls.from_settings(crawler.settings, crawler)
        #   File "{site-packages}/scrapy/middleware.py", line 67, in from_settings
        #     mw = create_instance(mwcls, settings, crawler)
        #   File "{site-packages}/scrapy/utils/misc.py", line 197, in create_instance
        #     raise TypeError(f"{objcls.__qualname__}.{method_name} returned None")
        # builtins.TypeError: BookPricePipeline.from_crawler returned None

        # print(f'from_crawler() =====')
        # for k, v in crawler.settings.copy_to_dict().items():
        #     print(f'  {k}: {v}')
        # print(f'from_crawler() =====')
        return cls()
        pass

    def open_spider(self, spider: scrapy.Spider):
        # 初始化工作：打开数据库、文件等
        pass

    def process_item(self, item, spider: scrapy.Spider):
        # 如果返回 item 则正常处理，如果抛出 DropItem 异常则丢弃该条数据
        if not isinstance(item, BookItem):
            raise DropItem(f"except {BookItem}, got {item.__class__}")
        adapter = ItemAdapter(item)
        rating = adapter.get('review_rating')
        if rating:
            item['review_rating'] = self._mapper[rating]
        if adapter.get('price'):
            price = float(item['price'][1:]) * self._rate
            item['price'] = f'￥{price:.2f}'
            # print(f'process_item() real price: {price:.2f}')
            return item
        else:
            raise DropItem(f"Missing 'price' in {type(item)}")

    def close_spider(self, spider: scrapy.Spider):
        # 清理工作：关闭数据库、文件等
        pass


# matplot 下载图片和代码
class FilesPipeline(files.FilesPipeline):

    @classmethod
    def _make_path(cls, url):
        logger.debug(f'_make_path() {url}')
        type_ = 'codes' if url.endswith('.py') else 'images'
        return f'matplot/{type_}/' + url.split('/')[-1]

    def get_media_requests(self, item, info):
        from scrapy.http.request import NO_CALLBACK
        import os

        _requests = []
        # 跳过已下载的文件
        for url in ItemAdapter(item).get(self.files_urls_field, []):
            _path = self.store.basedir + '/' + self._make_path(url)
            if os.path.exists(_path):
                # logger.debug(f'=== skip {url} -> {_path}')
                continue
            # logger.debug(f'>>> hit request {url} -> {_path}')
            _requests.append(scrapy.Request(url, callback=NO_CALLBACK))
        # logger.debug(f'>=>= request size: {len(_requests)}')
        return _requests

    def process_item(self, item, spider: scrapy.Spider):
        if not isinstance(item, MatplotItem):
            raise DropItem(f"except {MatplotItem}, got {item.__class__}")
        return super().process_item(item, spider)

    def file_path(self, request, response=None, info=None, *, item=None):
        return self._make_path(request.url)
