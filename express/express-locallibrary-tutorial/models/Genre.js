const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Genre', {
    idGenre: {
      type: DataTypes.INTEGER,
      allowNull: false,
      defaultValue: 1,
      primaryKey: true
    },
    Name: {
      type: DataTypes.STRING(45),
      allowNull: false
    }
  }, {
    sequelize,
    tableName: 'Genre',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "idGenre" },
        ]
      },
    ]
  });
};
