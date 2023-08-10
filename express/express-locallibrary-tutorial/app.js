const createError = require("http-errors");
const express = require("express");
const path = require("path");
const cookieParser = require("cookie-parser");
const logger = require("morgan");

const indexRouter = require("./routes/index");
const usersRouter = require("./routes/users");

// I added this ...
const catalogRouter = require("./routes/catalog"); // Import routes for "catalog" area of this site

const app = express();

// Sequelize START

// const dbConfig = require("./config/dbconfig.js");
// const sequelize = require("sequelize");

// const dbConnection = new sequelize(
//   dbConfig.DB,
//   dbConfig.USER,
//   dbConfig.PASSWORD,
//   {
//     host: dbConfig.HOST,
//     dialect: dbConfig.dialect,
//     operationsAliases: false,
//     pool: {
//       max: dbConfig.pool.max,
//       min: dbConfig.pool.min,
//       acquire: dbConfig.pool.acquire,
//       idle: dbConfig.pool.idle,
//     },
//   }
// );

// // Test the connection ...
// dbConnection
//   .authenticate()
//   .then(() => {
//     console.log(
//       "Connection from Sequelize to MySQL has been established successfully!"
//     );
//   })
//   .catch((error) => {
//     console.error("Unable to connect to the database: ", error);
//   });

// I am totally guessing this is what I need to do here ...
// Hmmm the working code in the folder /ExpressGenerator/express-locallibrary-tutorial does NOT do anything like this! ...
// It does NOT make any require into the models! ...suggesting strongly that this is not needed here!
// const initModels = require("./models/init-models");
// const models = initModels(dbConnection);

// This method DOES fire, but returns a Promise ...
// models.Author.count();
// models.Book.count();
// models.BookInstance.count();
// models.Genre.count();

// const bookCount = models.Book.count() ;
// console.log(bookCount)

// models.Book.count({}).then()

// Sequelize END

//
// const models = initModels(sequelize)

// const db = require('./models/init-models')
// db.dbConnection.sync()
//   .then(() => {
//     console.log("Synced db.");
//   })
//   .catch((err) => {
//     console.log("Failed to sync db: " + err.message);
//   });

// MySQL START
// var mysql = require('mysql');

// var con = mysql.createConnection({
//   host: "127.0.0.1",
//   user: "root",
//   password: "12345",
//   database : "LocalLibraryDB"
// });

// con.connect(function(err) {
//   if (err) throw err;
//   console.log("MySQL Connected!");
// });
// MySQL END

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use("/", indexRouter);
app.use("/users", usersRouter);

// I also added this ...
app.use("/catalog", catalogRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
  next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

module.exports = app;
