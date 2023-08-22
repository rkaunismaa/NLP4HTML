var DataTypes = require("sequelize").DataTypes;
var _Assessment = require("./Assessment");
var _Images = require("./Images");
var _Users = require("./Users");

function initModels(sequelize) {
  var Assessment = _Assessment(sequelize, DataTypes);
  var Images = _Images(sequelize, DataTypes);
  var Users = _Users(sequelize, DataTypes);


  return {
    Assessment,
    Images,
    Users,
  };
}
module.exports = initModels;
module.exports.initModels = initModels;
module.exports.default = initModels;
