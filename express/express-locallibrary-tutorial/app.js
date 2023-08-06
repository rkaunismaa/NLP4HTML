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

const dbConfig = require("./config/dbconfig.js");

const sequelize = require("sequelize");

const dbConnection = new sequelize(dbConfig.DB, dbConfig.USER, dbConfig.PASSWORD, {
  host: dbConfig.HOST,
  dialect: dbConfig.dialect,
  operationsAliases: false,
  pool: {
    max: dbConfig.pool.max,
    min: dbConfig.pool.min,
    acquire: dbConfig.pool.acquire,
    idle: dbConfig.pool.idle,
  },
});

const db = {};

// https://www.digitalocean.com/community/tutorials/how-to-use-sequelize-with-node-js-and-mysql

// const Sequelize = require("sequelize");

// const sequelize = new Sequelize(
//  'LocalLibraryDB',
//  'root',
//  '12345',
//   {
//     host: '127.0.0.1',
//     dialect: 'mysql'
//   }
// );

// Sequelize END

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
