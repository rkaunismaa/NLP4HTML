var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();


// https://www.digitalocean.com/community/tutorials/how-to-use-sequelize-with-node-js-and-mysql

const sequelize = require("sequelize");

// this next stuff blows up!
const seqConnection = new sequelize(
 'LocalLibraryDB',
 'root',
 '12345',
  {
    host: '127.0.0.1',
    dialect: 'mysql'
  }
);

// Sequelize END






// MySQL START
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "127.0.0.1",
  user: "root",
  password: "12345",
  database : "LocalLibraryDB"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("MySQL Connected!");
});
// MySQL END


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
