# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 自定义 item
class BookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # name = scrapy.Field(serializer=lambda s: ''.join(s))
    price = scrapy.Field()
    upc = scrapy.Field()
    review_rating = scrapy.Field()
    review_num = scrapy.Field(serializer=lambda o: int(o))
    stock = scrapy.Field(serializer=lambda o: int(o))
    img_url = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    pass

