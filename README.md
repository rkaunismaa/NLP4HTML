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

OMG What a fucking idiot!! I was having these problems because I had named my python file 'mysql.py' .... DUH! ... I can't believe how fucking stupid that is!!

## Monday, July 24, 2023

Got the newegg.jsonl stuff to load into MySql, but now, it looks like I am being blocked by newegg, so gotta see how to get around this problem.

Wow. Asked chatgpt for the solution, implemented it, and now the scraping works again!!! Is there any reason to ever use a search engine again??

## Tuesday, July 25, 2023

I want to see how far I can get with scraping yahoo finance data with scrapy ...

Figured how to debug through a spider in visual studio code ...

Nice! The yahoo scraping spider works just great!! ... Again, thanks to chatGPT for help!

Hmmm ... noticing in the mostactive.jsonl file that a bunch of fields are empty ... gonna try working through fixing some of them.

Nice! ... looks like they are now all working!

I think the next scrapy spider will target something I have not looked at yet ...

## Wednesday, July 26, 2023

Let's try to scrape match.com shall we ...

First thing to do is see how to login to the site with scrapy.

Wow. ChatGPT provided a more informative answer to the 'How do I login with scrapy' question than what was shown in the scrapy docs! ...

[Using FormRequest.from_response() to simulate a user login](https://docs.scrapy.org/en/latest/topics/request-response.html#topics-request-response-ref-request-userlogin)

Ok right ... I forgot ... match uses 2 factor authentication ... how the hell do I automate that??

Ok ... its 4:04pm ... I think for now I am beaten on figuring out how to use scrapy to login to match.com ... recaptchaResponse ... how the hell am I supposed to grab that??

4:33pm yahoo and newegg scrapers still work fine ... nice.

## Thursday, July 27, 2023

12:52pm Looking into Selenium ...

5:55pm Dammit ... still having issues with Selenium ... I am gonna bail on the nlp4html conda environment and switch back to the docker environment 'hfpt_July21'

5:59pm ok now spun up in hfpt_July21 ... gonna run newegg and yahoo scrapers ... nice! they both still run! ... what about mysql stuff? ... Yup! MySql stuff still works ... nice! ... ok, moving onto this Selenium shit ...

## Friday, July 28, 2023

Selenium with Chrome under the 'finance' conda environment on KAUWITB works ... but I totally do NOT want to use chrome. I killed it on KAUWITB, and will focus on getting it to work with FireFox ... or maybe even with Brave ... Right ... the thought of uninstalling FireFox then downloading it from FireFox and installing came to mind ... I ran 'sudo snap remove firefox' and it's now gone. Also ran 'sudo apt remove firefox' and stuff got removed. Now will run 'sudo snap install firefox'

3:09pm So Selenium works nicely with FireFox and Brave but only from the conda finance environment. It fails when using the docker container hfpt_July21 ... and I think it's because of the security restrictions of the docker container. So, IF you want to continue to explore Selenium, THEN use conda. So I am switching back the the nlpwhtml conda environment on KAUWITB and gonna test Selenium.

3:59pm Copied the working test_first_script.py file from the ~/Downloads folder and dumped it to the TestSelenium folder of this repo, and ran it through the finance conda environment without problems ... and yeah, if the brave stuff fails, kill any running instance of brave then try again ...

4:16pm So IF you want to dig further into Selenium, then use the conda environment finance ...

Right ... I started this Selenium stuff to see if I could scrape match from brave ... right? ...

5:05pm Nice! I figured out how to access Match.com in Brave with Selenium! Now I can really start to test scraping stuff with Selenium!

7:00pm hmm https://hub.docker.com/u/selenium ... https://github.com/SeleniumHQ/docker-selenium ... gonna see what I should download ...

## Saturday, July 29, 2023

Continuing to drill through match with Selenium ...

Ok. Pulling the data from Match nicely. Next step is to drill through one of the search pages and save to another local list. Damn it's good to be back to coding in real time!

Also, you really need to clean this repo! You are saving stuff you do not need to save!

## Sunday, July 30, 2023

Let's do some repo clean up, shall we ... OK ... bunch of useless stuff deleted.

OK repo now cleaned up.

## Monday, July 31, 2023

Added a bunch more code for run time information. Things are looking good!

## Tuesday, August 1, 2023

Grabbed the missed profiles. Then pulled down the images. I next want to work on some interface for viewing the data and images, and assignining some kind of rating to the profile.

Now let's load the profile data into a local mysql database. I will use the local running instance of MySql and store the database into a local matchDb folder.

Right. To load into mysql, I need to switch back to the nlp4html conda environment ...

OK. Nice! Got all of the profile data loaded into mysql! A few more tweaks to the sql code.

OK. Gonna go with node.js for the web development side of things. I haven't worked with node in a while, but yeah, it should be fun to get back to this side of the development life cycle ... !

docker pull node ... damn! 1Billion+ downloads!!

## Wednesday, August 2, 2023

Ran another scan of match. Moving onto creating a web site for this data using node.

Damn! Is there anything ChatGpt can't help me to solve? I was going through the node stuff at w3schools and wanted to see if I could display images in an html page chatgpt had created. The page displays the images no problem if I simply open it with a browser, but when I served the page up through node.js, none of the images showed. Whelp, I asked chatgpt about it, and it provided the correct answer! Damn, like seriously, the need to deeply understand code has gone WAY down. You need to be able to understand what it generates, but no longer do you need to crank it all out yourself!

This installs the mysql module for use by node => npm install mysql

OK Nice! Got a simple node file to pull stuff from the MatchDb. Next step is to display this to the user in the html page.

And Again! ChatGPT points me in the right direction! I got express to connect to the db, pull from the users table, and display this to the user!

npm install express ejs

No way would I be this far in my efforts without chatgpt! ....If I had stuck to 'reading the manuals' ... damn!

## Thursday, August 3, 2023

Continuing to work through the match user grid. I asked ChatGPT how to change the user.id field in the grid into a hyperlink, which will open a popup window with the images for that user ... it provided a very detailed response. Damn, this work has become so easy to do! ...

Whelp, this has proven to be harder than I thought. The window pops up, with the correct number of images we want to show, but the images are not showing.

3:16pm ... ok ... still struggling with this. damn ...

5:18pm ... meh ... don't want to do this anymore. Will continue later ...

6:37pm ... gonna get back to learning about node.js from [Introduction to Node.js](https://nodejs.dev/en/learn/introduction-to-nodejs/)

[Express Web Framework](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs) seems like a good a place as any to start looking into Express.

Nice! I CAN use TypeScript if I want for my javascript development in node.

Yeah. The above tutorial is gonna be super helpful! Resume [here](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/development_environment) tomorrow ..

## Friday, August 4, 2023

Continuing to go through [Express web framework (Node.js/Javascrip)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs)

The tutorial uses MongoDB, but I am going to use MySQL, just because I already know how to use it, and I know I can get it to work.

So I created the target LocalLibraryDB database in MySQL. Moving onto the routes part of the app.

Ok Nice! All the controller boilerplate stuff is done and tested! Moving onto [Displaying Library data](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Displaying_data)!

## Sunday, August 6, 2023

Continuing with [Displaying Library Data](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Displaying_data)

OK.The tutorial uses mongoosedb, but I want to use MySql. I am at [Home Page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Displaying_data/Home_page) in the tutorial, and of course, it is supposed to work, but does not. So, gotta figure out how to bake in the MySql goodness into this app ... So I need to create a 'countDocuments' method for the Book, BookInstance, Author, Genre objects ... where do I do this? Hmm yeah, it is the models stuff where this is done ... rembember, its all in the Mongoose stuff I totally skipped. So, gotta go through that, and figure out how to replicate that functionality in MySql ... [Express Tutorial Part3: Using a Database (with Mongoose)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/mongoose)

So it would appear the code in, say, ../models/book.js will be where we implement out MySQL access code ... OK ... the mongoose tutorial initiates the connection to the db in app.js, so of course, this will be where we open our connection to mysql ... Hmm ... mongoose uses an ORM ... for MySQL, I may use something like Sequelize ... still digging into this.

The tutotial includes a javascript file that populates the database with some examples. I will populate with dummy data using MySQL Workbench.

OK done with the Database part of the tutorial. I need to implement something like ../models/bookInstanceWithMongoose.js, but with Sequelize, and on an existing database ...

Wait ... I've been calling it wrong. Mongoose is the ORM to MongoDB ... it is NOT the db! ... duh ... and Mongoose ONLY supports MongoDB ...

OK ... gonna go with Sequelize, cuz why not, am I right?! ...

npm install --save sequelize

Hmm ... I ran npm install mysql a while back to provide access to mysql, but apparently that package was published 4 years ago. I am going to run ...

npm install mysql2

7:15pm ok ... ran 'express express-match --view=pug' in the 'express' folder. I am right away going to test this Sequelize stuff in there to see if it works.

7:30pm Installed mysql2 to express-match. It works. Now gonna try Sequelize ...

## Monday, August 7, 2023

To get 'npm run serverstart' to spin up without errors, I had to install mysql2@3.2.0. Now I am going to see if it actually works, meaning, can I get it to pull back data?

Hmm interesting ... there is a tool created by Sequelize called [Sequelize-Auto](https://github.com/sequelize/sequelize-auto) that can scan an existing db for you and create the models for all tables ... yeah, gonna give that a go right now.

npm install sequelize-auto

Jeeze. Took a while to figure out how to run the damn thing! ... You need to set the path to the command to run it ... like so ..

./node_modules/sequelize-auto/bin/sequelize-auto -o 'models' -d MatchDb -h 127.0.0.1 -u root -p 3306 -x 12345 -e mysql

2:54pm yup ... need to get a better understanding, so will dive into [Server-side webiste programming](https://developer.mozilla.org/en-US/docs/Learn/Server-side/First_steps) Still struggling with some unknowns ... sigh.

express untouched-app ... use this as a reference of an untouched express app ... 

6:29pm All the source code for the Express Local Libary can be found [here](https://github.com/mdn/express-locallibrary-tutorial)

## Tuesday, Autust 8, 2023

Yeah, [Node.js Rest APIs example with Express, Sequelize & MySQL](https://www.bezkoder.com/node-js-express-sequelize-mysql/) is a VERY useful 'How do I use Express, MySQL, and Sequelize in a web app?' link ... 

Yeah ... initialize the db in the model init.js file .. not the app.js!

3:32pm OK. Step back, and try to do something real simple with Express, and MySQL connected to, say, MatchDB ...this Sequelize stuff with the LocalLibrary app is taking too long to get going, and I need to start with something simpler, WITHOUT any Sequelize crap ...

3:45pm So mess with the 'express-match' express generated project. It only has had the models stuff dumped in, all the originally generated code remains.

4:03pm Hmmm actually, I am going to pull down [this](https://github.com/bezkoder/nodejs-express-sequelize-mysql.git) repo, and play with it. It is a sample app with all these pieces.I am not going to pull it into this repo just yet, but I may ...

7:37pm Actually, what I think is the best way to learn how to properly wire up the db with express is to go through the LocalLibrary example, [from the start](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs), and use Mongoose/MongoDB ... I will create this in the ExpressGenerator sub folder.

express express-locallibrary-tutorial --view=pug

## Wednesday, August 9, 2023

Starting here [Express Tutorial Part 3: Using a Database (with Mongoose)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/mongoose)

[Install MongoDB Community Edition on Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)

1:33pm docker pull mongo .... cuz why not?! Instead of loading it locally, use the docker image ... right?!

2:24pm so using the default version of mongoose(7.4.2 ... published 6 days ago) fails! ... but using an older release works!

npm i mongoose@5.13.20

So it looks like we are able to connect to the local version of MongoDB using mongoose. Nice! So far, ALL we have done is add the code to the app.js to connect to the database. We have not defined models, views or controllers. The next step is to create our models, so lets to that and test to see if it works. 

2:36pm Create the models, now ready to download the [populatedb.js](https://raw.githubusercontent.com/mdn/express-locallibrary-tutorial/main/populatedb.js) script to pump some dummy data into the db. If this works, then we are in great shape!

2:48pm Nice! The script ran! 

node populatedb "mongodb://127.0.0.1:27017/local_library"

Moving onto [Express Tutorial Part 4: Routes and controllers](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/routes)

Notice the order in which we create these objects. We create the db, then added the tables, then we created the 4 models for those 4 tables, then the controllers for each of those models, then just one catalog.js route file in the routes folder, then update the app.js to include those new routes.

3:45pm [Express Tutorial Part 5: Displaying library data](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Displaying_data) We now move onto creating the views.

4:32pm So now at the point where the home page is correctly pulling back the record counts of each table. This is the part I was UNABLE to get to work with MySQL and Sequelize. I fired up the current code into a new 'JustTheHomePageWorks' branch of the repo.

4:58pm So the part I find confusing is we open the connection to the db in app.js? Hmm interesting ... changing the name of the connection from 'mongoose' to 'GFY' does NOT break the home page from spinning up with the correct numbers!