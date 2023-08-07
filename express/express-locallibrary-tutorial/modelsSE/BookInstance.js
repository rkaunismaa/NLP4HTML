const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('BookInstance', {
    idBookInstance: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    idBook: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: 'Book',
        key: 'idBook'
      }
    },
    Imprint: {
      type: DataTypes.STRING(45),
      allowNull: false
    },
    Status: {
      type: DataTypes.STRING(45),
      allowNull: false
    },
    DueBack: {
      type: DataTypes.DATEONLY,
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'BookInstance',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "idBookInstance" },
        ]
      },
      {
        name: "FK_BookBookInstance",
        using: "BTREE",
        fields: [
          { name: "idBook" },
        ]
      },
    ]
  });
};
