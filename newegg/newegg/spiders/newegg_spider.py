
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

            # #item_cell_34-156-452_3_0 > div.goods-info > div.tag-list > div > div
            title = item.css(".goods-title::text").get()

            # salePrice
            spDollars = item.css("span.goods-price-value > strong::text").get()
            spCents = item.css("span.goods-price-value > sup::text").get()
            salePrice = "$" + spDollars + spCents

            wasPrice = item.css(".goods-price-was::text").get()

            savings = item.css("div.goods-info > div.tag-list > div > div::text").get()

            if title and wasPrice and salePrice and savings:
                neitem = NeweggItem()
                neitem["title"] = title.strip()
                neitem["originalPrice"] = wasPrice.strip()
                neitem["salePrice"] = salePrice
                neitem["savings"] =savings.strip()
                yield neitem

