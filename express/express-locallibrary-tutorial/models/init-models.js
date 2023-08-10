// const DataTypes = require("sequelize").DataTypes;
// const _Author = require("./Author");
// const _Book = require("./Book");
// const _BookInstance = require("./BookInstance");
// const _Genre = require("./Genre");

// I added this Sequelize stuff ...
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

const DataTypes = require("sequelize").DataTypes;
const _Author = require("./Author");
const _Book = require("./Book");
const _BookInstance = require("./BookInstance");
const _Genre = require("./Genre");


// Sequelize END

function initModels(sequelize) {
  const Author = _Author(sequelize, DataTypes);
  const Book = _Book(sequelize, DataTypes);
  const BookInstance = _BookInstance(sequelize, DataTypes);
  const Genre = _Genre(sequelize, DataTypes);

  Book.belongsTo(Author, { as: "idAuthor_Author", foreignKey: "idAuthor" });
  Author.hasMany(Book, { as: "Books", foreignKey: "idAuthor" });
  BookInstance.belongsTo(Book, { as: "idBook_Book", foreignKey: "idBook" });
  Book.hasMany(BookInstance, { as: "BookInstances", foreignKey: "idBook" });
  Book.belongsTo(Genre, { as: "idGenre_Genre", foreignKey: "idGenre" });
  Genre.hasMany(Book, { as: "Books", foreignKey: "idGenre" });

  return {
    Author,
    Book,
    BookInstance,
    Genre,
  };
}

const models = initModels(sequelize)

const db = {};
db.Sequelize = Sequelize;
db.sequelize = sequelize;
db.models = models;

module.exports = db;


// initModels(sequelize);

// module.exports = initModels;
// module.exports.initModels = initModels;
// module.exports.default = initModels;
