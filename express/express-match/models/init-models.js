var DataTypes = require("sequelize").DataTypes;
var _Images = require("./Images");
var _Users = require("./Users");

function initModels(sequelize) {
  var Images = _Images(sequelize, DataTypes);
  var Users = _Users(sequelize, DataTypes);


  return {
    Images,
    Users,
  };
}
module.exports = initModels;
module.exports.initModels = initModels;
module.exports.default = initModels;
