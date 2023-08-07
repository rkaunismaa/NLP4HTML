const Sequelize = require("sequelize");
module.exports = function (sequelize, DataTypes) {
  return sequelize.define(
    "Author",
    {
      idAuthor: {
        type: DataTypes.INTEGER,
        allowNull: false,
        primaryKey: true,
      },
      FirstName: {
        type: DataTypes.STRING(100),
        allowNull: false,
      },
      FamilyName: {
        type: DataTypes.STRING(100),
        allowNull: false,
      },
      DateOfBirth: {
        type: DataTypes.DATEONLY,
        allowNull: true,
      },
      DateOfDeath: {
        type: DataTypes.DATEONLY,
        allowNull: true,
      },
    },
    {
      sequelize,
      tableName: "Author",
      timestamps: false,
      indexes: [
        {
          name: "PRIMARY",
          unique: true,
          using: "BTREE",
          fields: [{ name: "idAuthor" }],
        },
      ],
    }
  );
};
