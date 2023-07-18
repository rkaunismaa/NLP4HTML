
from pathlib import Path

import scrapy

from newegg.items import NeweggItem

class NeweggSpider(scrapy.Spider):

    name = "newegg"
    
    start_urls = ['https://www.newegg.ca/d/Best-Sellers/Gaming-Laptops/c/ID-363']

    def parse(self, response):

        # grab all the items
        items = response.css(".goods-container")

        # loop through the items
        for item in items:

            # //*[@id="item_cell_34-156-308_1_0"]/a/img
            title = item.css(".goods-title::text").get()

            # salePrice
            spDollars = item.css("span.goods-price-value > strong::text").get()
            spCents = item.css("span.goods-price-value > sup::text").get()
            salePrice = "$" + spDollars + spCents

            wasPrice = item.css(".goods-price-was::text").get()

            if title and wasPrice and salePrice:
                neitem = NeweggItem()
                neitem["title"] = title.strip()
                neitem["originalPrice"] = wasPrice.strip()
                neitem["salePrice"] = salePrice
                yield neitem

