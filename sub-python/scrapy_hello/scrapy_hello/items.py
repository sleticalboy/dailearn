# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 自定义 item
class BookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    upc = scrapy.Field()
    review_rating = scrapy.Field()
    review_num = scrapy.Field(serializer=int)
    stock = scrapy.Field(serializer=int)
    img_url = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    pass


class MatplotItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    file_urls = scrapy.Field()
    img_urls = scrapy.Field()
    sample_codes = scrapy.Field()
    pass

