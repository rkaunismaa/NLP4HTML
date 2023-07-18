
from pathlib import Path

import scrapy

from newegg.items import NeweggItem

class NeweggSpider(scrapy.Spider):

    name = "newegg"
    
    start_urls = ['https://www.newegg.ca/d/Best-Sellers/Gaming-Laptops/c/ID-363']

    def parse(self, response):


        # 1) Get all items
       #  allGoods = response.css(".goods-container").getall()

        # 2) Loop through each item
        titles = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "goods-title", " " ))]').css('::text').extract()

        # yield { 'title', title}
        for title in titles:
            item = NeweggItem()
            item["title"] = title.strip()
            yield item





        # yield response.css(".goods-title::text").getall()


        # yield response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').extract()


    #    allGoods = response.css(".goods-container").getall()
    # //*[@id="item_cell_34-156-308_1_0"]

    # //*[contains(concat( " ", @class, " " ), concat( " ", "goods-container", " " ))]
    # //*[contains(concat( " ", @class, " " ), concat( " ", "goods-info", " " ))]
    # //*[contains(concat( " ", @class, " " ), concat( " ", "goods-title", " " ))]
    # //*[contains(concat( " ", @class, " " ), concat( " ", "goods-container", " " ))]

    #    for good in allGoods:
           
    #        title = good.css('img::title').get()

    #        yield { 'title', title}

           

           


        # for item in items[:10]:

        #     title = item.css('.goods-title::text').get()

        #     yield {
        #         'title': title,
        #     }
