const DataTypes = require("sequelize").DataTypes;
const _Author = require("./Author");
const _Book = require("./Book");
const _BookInstance = require("./BookInstance");
const _Genre = require("./Genre");

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
module.exports = initModels;
module.exports.initModels = initModels;
module.exports.default = initModels;
