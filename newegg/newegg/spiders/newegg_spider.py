
from pathlib import Path

import scrapy

from newegg.items import NeweggItem

class NeweggSpider(scrapy.Spider):

    name = "newegg"
    
    def start_requests(self):

        urls = [
            "https://www.newegg.ca/d/Best-Sellers/CPUs-Processors/c/ID-34",
            # "https://www.newegg.ca/d/Best-Sellers/Motherboards/c/ID-20",
            # "https://www.newegg.ca/d/Best-Sellers/SSDs/c/ID-119",
            # "https://www.newegg.ca/d/Best-Sellers/Gaming-Laptops/c/ID-363",
            # "https://www.newegg.ca/d/Best-Sellers/Desktop-Computers/c/ID-228",
            # "https://www.newegg.ca/d/Best-Sellers/GPUs-Video-Graphics-Devices/c/ID-38",
        ]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        # grab all the items
        items = response.css(".goods-container") # .getall() does not work!

        # loop through the items
        for item in items:

            tagmedal = item.css(".tag-medal::text").get()
            title = item.css(".goods-title::text").get()
            url = item.css(".goods-title::attr(href)").get()
            imgsrc = item.css("a > img::attr(src)").get()

            # price
            dollars = item.css("span.goods-price-value > strong::text").get()
            cents = item.css("span.goods-price-value > sup::text").get()
            price = "$" + dollars + cents

            # these items may not not exist ...
            wasPrice = item.css(".goods-price-was::text").get()
            savings = item.css("div.goods-info > div.tag-list > div > div::text").get()
       
            #if tagmedal and title and wasPrice and salePrice and savings:
            if tagmedal and title and url and imgsrc and price:
                neitem = NeweggItem()
                neitem["tagmedal"] = tagmedal.strip()
                neitem["title"] = title.strip()
                neitem["url"] = url.strip()
                neitem["imgsrc"] = imgsrc.strip()
                neitem["price"] = price
                if wasPrice is not None:
                    neitem["wasprice"] = wasPrice.strip()
                else:
                    neitem["wasprice"] = ""
                if savings is not None:
                    neitem["savings"] = savings.strip()
                else:
                    neitem["savings"] = ""

                # Follow the link to the item details page
                yield scrapy.Request(url, callback = self.parse_item,  meta={'neitem': neitem})

              
    def parse_item(self, response):

        listitems = response.css("div.product-bullets > ul > li::text").getall()

        # Get the neitem object from the metadata of the response object
        neitem = response.meta['neitem']

        neitem["bullets"] = listitems

        yield neitem

