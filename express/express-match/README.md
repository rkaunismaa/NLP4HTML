## Monday, August 21, 2023

3:15pm Getting back to building this site. I want to start with the landing page, being a simple grid displaying some of the fields found in the Users table.

## Tuesday, August 22, 2023

1:08pm reran ... ./node_modules/sequelize-auto/bin/sequelize-auto -o 'models' -d MatchDb -h 127.0.0.1 -u root -p 3306 -x 12345 -e mysql

This was run from within the ~/Data/Documents/Github/rkaunismaa/NLP4HTML/express/express-match folder ...

The ChatGPT express code is found in the /node subfolder ...

This is what I did to get the page showing the user details grid to show up ...

1) Added config/dbconfig.js to hold the connection settings to the MatchDb database.
2) Add the code to connect to the db in /models/init-models.js

... Start with the route, then the controller, then the model ... the route points to the controller, and it is in the controller where we do the work of specifying what we want to do with the database. 

 3) I added a new 'controllers' folder, and then added an empty usersController.js file. There is typically a one to one relation between the tables in the database and a controller file. At the top of this file, I require '../models/init-models' to pull in all the models, and "express-async-handler".

 ... spun up, got a runtime error with "express-async-handler" ... so ran ...

 npm i express-async-handler

 4) To the /routes/users.js file, in the existing router.get method (/* GET users listing. */), I commented out the existing res.send code, and added a require to the usersController.js file. 

 5) In the usersController.js file, in the 'exports.user_list = ...' method, I commented out the boilerplate ' res.send("NOT IMPLEMENTED: Users List");' method, and added the default code to send back all the users ...

 So now, the work is trying to figure out how to create the user list template using pug ... ugh ... The code in the /ExpressGenerator/express-locallibrary-tutorial has a lot of pug examples in the /view folder ... use this as your guide. ... Right, to run this site, you first need to spin up the mongodb with ... 

 sudo systemctl start mongod

 6) Add the code to hit the db and send back all the users in the exports.user_list method of /controllers/usersController.js

 7) Add a new '

 ## Wednesday, August 23, 2023

 11:50am Rescraped match data and images. Loaded into MySQL. Working on finessing the users listing page. 

 1:01pm ok nice. User grid data is showing nicely. The next step is to add a link to open a popup window that will display the images for the user.

## Thursday, August 24, 2023

3:30pm Damn, that took a long time! Finally got the images page to spin up! ...

[This](https://www.sitepoint.com/a-beginners-guide-to-pug/) was a helpful resource!

Next Steps are to add a rating scale to the image page, and allow the user to rate this person, then save this ratings back to the database.

I also want to add at the top of the userlist page the ability to control what gets sent back to the user. Right now I tweak the query in the usersController.js file, which works, but is inefficient. 

Hmmm there is probably a way to send ALL the data to the user, and then tweak what is shown on the client and NOT make another call back to the server for a new user list ...

## Saturday, August 26, 2023

3:56pm rescanned stuff this morning, added a Message field into the Images table for any message from the user for the given image. 

4:11pm meh ... moved images into the desired /public/images folder, backing up the original images folder by renaming it to images_August_26_2023.

6:28pm ok nice. I now have the images being displayed with any existing note. 

## Monday, August 28, 2023

3:57pm Adding the rating to the user images page.
6:14pm ok got the rating stuff working. Yeah, it could be improved, but the functionality is there.

## Wednesday, March 6, 2024

3:13pm Adding the users first image to the users listing page.