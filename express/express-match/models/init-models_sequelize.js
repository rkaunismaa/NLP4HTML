// Sequelize START
const dbConfig = require("../config/dbconfig.js");
const Sequelize = require("sequelize");

const sequelize = new Sequelize(dbConfig.DB, dbConfig.USER, dbConfig.PASSWORD, {
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

// Test the connection ...
sequelize
  .authenticate()
  .then(() => {
    console.log(
      "Connection from Sequelize to MySQL has been established successfully!"
    );
  })
  .catch((error) => {
    console.error("Unable to connect to the database: ", error);
  });

  // Sequelize END

var DataTypes = require("sequelize").DataTypes;

var _Assessment = require("./Assessment");
var _Images = require("./Images");
var _Users = require("./Users");

function initModels(sequelize) {

  var Assessment = _Assessment(sequelize, DataTypes);
  var Images = _Images(sequelize, DataTypes);
  var Users = _Users(sequelize, DataTypes);

  return {
    Assessment,
    Images,
    Users,
  };
}

// module.exports = initModels;
// module.exports.initModels = initModels;
// module.exports.default = initModels;

const models = initModels(sequelize)

const db = {};
db.Sequelize = Sequelize;
db.sequelize = sequelize;
db.models = models;

module.exports = db;


