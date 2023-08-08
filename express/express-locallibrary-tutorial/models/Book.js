const Sequelize = require("sequelize");

module.exports = function (sequelize, DataTypes) {
  return sequelize.define(
    "Book",
    {
      idBook: {
        type: DataTypes.INTEGER,
        allowNull: false,
        primaryKey: true,
      },
      Title: {
        type: DataTypes.STRING(45),
        allowNull: false,
      },
      idAuthor: {
        type: DataTypes.INTEGER,
        allowNull: false,
        references: {
          model: "Author",
          key: "idAuthor",
        },
      },
      Summary: {
        type: DataTypes.STRING(2048),
        allowNull: false,
      },
      ISBN: {
        type: DataTypes.STRING(45),
        allowNull: true,
      },
      idGenre: {
        type: DataTypes.INTEGER,
        allowNull: true,
        references: {
          model: "Genre",
          key: "idGenre",
        },
      },
    },
    {
      sequelize,
      tableName: "Book",
      timestamps: false,
      indexes: [
        {
          name: "PRIMARY",
          unique: true,
          using: "BTREE",
          fields: [{ name: "idBook" }],
        },
        {
          name: "FK_AuthorBook",
          using: "BTREE",
          fields: [{ name: "idAuthor" }],
        },
        {
          name: "FK_GenreBook",
          using: "BTREE",
          fields: [{ name: "idGenre" }],
        },
      ],
    }
  );
};


