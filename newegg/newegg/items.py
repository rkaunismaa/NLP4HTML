# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NeweggItem(scrapy.Item):
    # define the fields for your item here like:
    tagmedal = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    wasprice = scrapy.Field()
    price = scrapy.Field()
    savings = scrapy.Field()
    pass
