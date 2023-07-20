# NLP4HTML
This repository will contain my exploration of using nlp to parse html. 

## Wednesday, July 12, 2023

It begins ... using the local docker container 'peaceful_solomon' for this repository. 

## Thursday, July 13, 2023

Got a simple scrapy notebook running with little effort. Now I want to see about getting scrapy to pull stuff from newegg.ca

## Friday, July 14, 2023

This really should be very easy to do with srapy! Trying to scrape yahoo finance ....

Trying to see what I can get going using [ScrappyYahooFinance](https://github.com/iaugustine/WebScraping_Scrapy_YahooFinanceData)

## Saturday, July 15, 2023

So looks like I've been blocked by Yahoo Finance ... time to figure out how to use a proxy server!

Using a proxy server with yfinance is trivial. So far can't get it to work with scrapy. 

Gonna move back to scraping newegg.ca ...

## Monday, July 17, 2023

Working through the [scrapy tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)

## Tuesday, July 18, 2023

Trying again to scrap stuff from [newegg](https://www.newegg.ca/d/Best-Sellers/Gaming-Laptops/c/ID-363) ...

# Thursday, July 20, 2023

Scrapy on newegg is working. Today, I want to persist to some db. 

Yup. Going with MySql ... Yeah ... not going to install MySql to this docker image, but going to spin up a separate docker image that has MySql ...

Installing "MySQL Shell for VS Code" to VSCode ... hmm it did not work ... ok, ran it again, with the docker container running, and it looks like it installed something to the host.
