# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NeweggItem(scrapy.Item):
    # define the fields for your item here like:
    dateTime = scrapy.Field()
    sourceUrl = scrapy.Field()
    tagmedal = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    imgsrc = scrapy.Field()
    price = scrapy.Field()
    wasprice = scrapy.Field()
    savings = scrapy.Field()
    bullets = scrapy.Field()
    pass
