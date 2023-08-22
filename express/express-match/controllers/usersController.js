const db = require('../models/init-models');
const asyncHandler = require("express-async-handler");

// Display a list of all Users
exports.user_list = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Users List");
  });
  
