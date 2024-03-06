const Sequelize = require('sequelize');
module.exports = function(sequelize, DataTypes) {
  return sequelize.define('UsersView', {
    idUsers: {
      autoIncrement: true,
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true
    },
    MatchUserId: {
      type: DataTypes.STRING(64),
      allowNull: false
    },
    Url: {
      type: DataTypes.STRING(256),
      allowNull: false
    },
    FirstName: {
      type: DataTypes.STRING(32),
      allowNull: true
    },
    AgeLocation: {
      type: DataTypes.STRING(64),
      allowNull: true
    },
    Subscriber: {
      type: DataTypes.TINYINT,
      allowNull: true
    },
    LastOnline: {
      type: DataTypes.STRING(64),
      allowNull: true
    },
    MiniEssayTitle: {
      type: DataTypes.STRING(256),
      allowNull: true
    },
    MiniEssayContent: {
      type: DataTypes.STRING(512),
      allowNull: true
    },
    Summary: {
      type: DataTypes.STRING(4096),
      allowNull: true
    },
    ScanDateTime: {
      type: DataTypes.DATE,
      allowNull: false
    },
    Rating: {
      type: DataTypes.STRING(45),
      allowNull: true,
      defaultValue: "0"
    },
    ImageURL: {
      type: DataTypes.STRING(512),
      allowNull: true
    }
  }, {
    sequelize,
    tableName: 'Match_Users_View',
    timestamps: false,
    indexes: [
      {
        name: "PRIMARY",
        unique: true,
        using: "BTREE",
        fields: [
          { name: "idUsers" },
        ]
      },
    ]
  });
};
