# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.crawler import Crawler


# 自定义 pipeline
# 1、
# 2、写入文件、数据库
# 3、数据清洗（去重、去损、去过期）
# 4、统计
class BookPricePipeline:

    _rate = 8.539

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

    def open_spider(self, spider):
        # 初始化工作：打开数据库、文件等
        pass

    def process_item(self, item, spider):
        # 如果返回 item 则正常处理，如果抛出 DropItem 异常则丢弃该条数据
        # adapter = ItemAdapter(item)
        if item.get('price'):
            price = float(item['price'][1:]) * self._rate
            item['price'] = f'￥{price:.2f}'
            print(f'process_item() real price: {price:.2f}')
            return item
        else:
            raise DropItem(f'Missing price in {item}')

    def close_spider(self, spider):
        # 清理工作：关闭数据库、文件等
        pass
