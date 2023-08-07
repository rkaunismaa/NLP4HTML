const Genre = require("../models/Genre");
const asyncHandler = require("express-async-handler");

// Display a list of all Genres
exports.genre_list = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Genre List");
});

// Display detail page for a specific Genre
exports.genre_detail = asyncHandler(async (req, res, next) => {
  res.send(`NOT IMPLEMENTED: Genre detail: ${req.params.id}`); // notice the string delimeters we use here! ` ... NOT ' or "
});

// CREATE
// Display Genre createform on GET
exports.genre_create_get = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Genre create GET");
});

// Handle Genre create on POST
exports.genre_create_post = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Genre create POST");
});

// DELETE
// Display Genre delete form on GET
exports.genre_delete_get = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Genre delete GET");
});

// Handle Genre delete on POST
exports.genre_delete_post = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Genre Delete POST");
});

// UPDATE
// Display Genre update form on GET
exports.genre_update_get = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Genre update GET");
});

// Handle Genre update on POST
exports.genre_update_post = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Genre update POST");
});
