// Initialize the connection to the db here ... START
const Sequelize = require("sequelize");
const DataTypes = require("sequelize").DataTypes;
const dbConfig = require("../config/dbconfig.js");

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

// Initialize the connection to the db here ... END

const _Assessment = require("./Assessment");
const _Images = require("./Images");
const _Users = require("./Users");

const _UsersView = require("./UsersView");


function initModels(sequelize) {

  const Assessment = _Assessment(sequelize, DataTypes);
  const Images = _Images(sequelize, DataTypes);
  const Users = _Users(sequelize, DataTypes);

  const UsersView = _UsersView(sequelize, DataTypes);

  return {
    Assessment,
    Images,
    Users,
    UsersView,
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