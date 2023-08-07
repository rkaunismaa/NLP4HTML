var DataTypes = require("sequelize").DataTypes;
var _Author = require("./Author");
var _Book = require("./Book");
var _BookInstance = require("./BookInstance");
var _Genre = require("./Genre");

function initModels(sequelize) {
  var Author = _Author(sequelize, DataTypes);
  var Book = _Book(sequelize, DataTypes);
  var BookInstance = _BookInstance(sequelize, DataTypes);
  var Genre = _Genre(sequelize, DataTypes);

  Book.belongsTo(Author, { as: "idAuthor_Author", foreignKey: "idAuthor"});
  Author.hasMany(Book, { as: "Books", foreignKey: "idAuthor"});
  BookInstance.belongsTo(Book, { as: "idBook_Book", foreignKey: "idBook"});
  Book.hasMany(BookInstance, { as: "BookInstances", foreignKey: "idBook"});
  Book.belongsTo(Genre, { as: "idGenre_Genre", foreignKey: "idGenre"});
  Genre.hasMany(Book, { as: "Books", foreignKey: "idGenre"});

  return {
    Author,
    Book,
    BookInstance,
    Genre,
  };
}
module.exports = initModels;
module.exports.initModels = initModels;
module.exports.default = initModels;
