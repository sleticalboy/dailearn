# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 自定义 item
class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field(serilizer=lambda s: ''.join(s))
    name = scrapy.Field()
    price = scrapy.Field()
    pass

