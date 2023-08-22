const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('Assessment', {
    idAssessment: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    idUsers: {
      type: DataTypes.STRING(45),
      allowNull: true
    },
    Rating: {
      type: DataTypes.TINYINT,
      allowNull: true
    },
    Comments: {
      type: DataTypes.STRING(1024),
      allowNull: true
    },
    Date: {
      type: DataTypes.STRING(45),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'Assessment',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "idAssessment" },
        ]
      },
    ]
  });
};
