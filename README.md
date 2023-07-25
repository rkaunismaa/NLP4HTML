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

# Friday, July 21, 2023

Tweaking some issues with newegg scrapy code ... 

Ok ... it's working now, but the list is out of order. I can live with that. I just need it to scrape the correct data.

Wrote a simple python file to fix the order problem. It's bloody ridiculous how much more useful is the response from ChatGPT than what I get back with a search engine!

OK ... now running under a newer docker container, based off the latest image ...

docker pull huggingface/transformers-pytorch-gpu

This new container has been given the name hfpt_June21 ... fuck me ... that really should be July21 ... meh ... 

OK ... killed that, restarted with the correct name, with user root privileges, and was now able to install the MySQL connector to Visual Studio Code. Yay!

## Saturday, July 22, 2023

Still ongoing issues with the 'MySQL connector to Visual Studio Code'

## Sunday, July 23, 2023

Switched to a newly created conda environment called 'nlp4html' Gonna see if I appear to have fewer issues with this ... 

So yeah, I do get a little further, but I STILL cannot connect to mysql20230720 from python. Sigh ... Gonna install mysql server to kauwitb ... 

OMG What a fucking idiot!! I was having these problems because I had named my python file 'mysql.py' .... DUH! ... I can't beleive how fucking stupid that is!!

## Monday, July 24, 2023

Got the newegg.jsonl stuff to load into MySql, but now, it looks like I am being blocked by newegg, so gotta see how to get around this problem.

Wow. Asked chatgpt for the solution, implemented it, and now the scraping works again!!! Is there any reason to ever use a search engine again??

## Tuesday, July 25, 2023

I want to see how far I can get with scraping yahoo finance data with scrapy ... 

Nice! The yahoo scraping spider works just great!! ... Again, thanks to chatGPT for help!

Hmmm ... noticing in the mostactive.jsonl file that a bunch of fields are empty ... gonna try working through fixing some of them.