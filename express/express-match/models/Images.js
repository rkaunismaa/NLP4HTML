const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Images', {
    idImages: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    idUsers: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    userImageNo: {
      type: DataTypes.INTEGER,
      allowNull: false
    },
    Url: {
      type: DataTypes.STRING(256),
      allowNull: false
    },
    Message: {
      type: DataTypes.STRING(512),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'Images',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "idImages" },
        ]
      },
    ]
  });
};
