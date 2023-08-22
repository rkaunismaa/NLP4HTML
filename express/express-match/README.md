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