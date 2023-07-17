
from pathlib import Path

import scrapy

class NeweggSpider(scrapy.Spider):

    name = "newegg"
    
    start_urls = ['https://www.newegg.ca/d/Best-Sellers/Gaming-Laptops/c/ID-363']

    def parse(self, response):

        # yield response.css(".goods-title::text").getall()


        # yield response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').extract()


    #    allGoods = response.css(".goods-container").getall()

    #    for good in allGoods:
           
    #        title = good.css('img::title').get()

    #        yield { 'title', title}

           

           


        # for item in items[:10]:

        #     title = item.css('.goods-title::text').get()

        #     yield {
        #         'title': title,
        #     }
