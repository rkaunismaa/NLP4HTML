import scrapy
# Import the ItemObjects
from ..items import YahooscrapingItem

class MostactiveSpider(scrapy.Spider):

    name = 'mostactive'

    def start_requests(self):
        
        urls = ['https://finance.yahoo.com/most-active/']  # Most active start URL

        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_pages)

    def get_pages(self, response):
        count = str(response.xpath('// *[ @ id = "fin-scr-res-table"] / div[1] / div[1] / span[2] / span').css(
            '::text').extract())
        total_results = int(count.split()[-2])
        total_offsets = total_results // 25 + 1
        offset_list = [i * 25 for i in range(total_offsets)]
        for offset in offset_list:
            yield scrapy.Request(url=f'https://finance.yahoo.com/most-active?count=25&offset={offset}',
                                 callback=self.get_stocks)

    def get_stocks(self, response):
        # Get all the stock symbols
        stocks = response.xpath('//*[@id="scr-res-table"]/div[1]/table/tbody//tr/td[1]/a').css('::text').extract()
        for stock in stocks:
            # Follow the link to the stock details page.
            yield scrapy.Request(url=f'https://finance.yahoo.com/quote/{stock}?p={stock}', callback=self.parse)
            # https://finance.yahoo.com/quote/NVDA?p=NVDA ... an example

    def parse(self, response):
        #Declare the item objects
        items = YahooscrapingItem()
        #Save the extracted data in the item objects
        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').extract()

        items['intraday_price'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').css('::text').extract()
        # above no longer works, so trying this ... nope!
        items['intraday_price'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]/span').css('::text').extract()

        items['price_change'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]').css('::text').extract()
        # above no longer works, so trying this ... it works!
        items['price_change'] = response.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[2]/span').css('::text').extract()

        items['current_timestamp'] = response.xpath('//*[@id="quote-market-notice"]/ span').css('::text').extract()
        items['prev_close'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]').css(
            '::text').extract()
        items['open'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]').css(
            '::text').extract()
        
        # this is not working ...
        items['bid'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]/span').css('::text').extract()
        # so let's try this ... yes!
        items['bid'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]').css('::text').extract()
        
        # this is not working
        items['ask'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]/span').css('::text').extract()
        # so let's try this ... yes!
        items['ask'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]').css('::text').extract()

        items['range_day'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]').css('::text').extract()
        items['range_52weeks'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]').css('::text').extract()
        
        # this is not working ...
        items['volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/span').css('::text').extract()
        # so let's try this ... nope
        items['volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/fin-streamer/span').css('::text').extract()



        # this is not working ...
        items['volume_avg'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]/span').css('::text').extract()
        # so let's try this ... yes!
        items['volume_avg'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]').css('::text').extract()
        
        
        # this is not working ...
        items['market_cap'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]/span').css('::text').extract()
        # so let's try this ... yes!
        items['market_cap'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]').css('::text').extract()

        # this is not working ...
        items['beta_5yr_monthly'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]/span').css('::text').extract()
        # so let's try this ... yes!
        items['beta_5yr_monthly'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]').css('::text').extract()

        # this is not working ...
        items['pe_ratio'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]/span').css('::text').extract()
        # so let's try this ... yes!
        items['pe_ratio'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]').css('::text').extract()


        # this is not working ...
        items['eps'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[2]/span').css('::text').extract()
        # so lets try this ... yes!
        items['eps'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[2]').css('::text').extract()





        items['earnings_date'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]/span[1]').css('::text').extract()
        items['fwd_div_yield'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]').css('::text').extract()

        # this no longer works ...
        items['exp_div_date'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[7]/td[2]/span').css('::text').extract()
        # so let's try this ... ...hm ok it works for some ... yeah, no changes
        items['exp_div_date'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[7]/td[2]/span').css('::text').extract()

        # this no longer works ...
        items['est_yr_target'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]/span').css('::text').extract()
        # so let's pick this ... yes!
        items['est_yr_target'] = response.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]').css('::text').extract()

        # an example of the output from above ...
        # {"stock_name": ["NVIDIA Corporation (NVDA)"], "intraday_price": [], "price_change": [], "current_timestamp": ["As of  03:18PM EDT. Market open."], "prev_close": ["446.12"], "open": ["449.41"], "bid": [], "ask": [], "range_day": ["449.23 - 461.83"], "range_52weeks": ["108.13 - 480.88"], "volume": [], "volume_avg": [], "market_cap": [], "beta_5yr_monthly": [], "pe_ratio": [], "eps": [], "earnings_date": ["Aug 23, 2023"], "fwd_div_yield": ["0.16 (0.04%)"], "exp_div_date": ["Jun 07, 2023"], "est_yr_target": []}

        yield items