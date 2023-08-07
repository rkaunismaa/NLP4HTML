const Book = require("../models/Book");
const Author = require("../models/Author");
const Genre = require("../models/Genre");
const BookInstance = require("../models/BookInstance");

const asyncHandler = require("express-async-handler");

// exports.index = asyncHandler(async (req, res, next) => {
//   res.send("NOT IMPLEMENTED: Site Home Page");
// });

exports.index = asyncHandler(async (req, res, next) => {
  // Get details of books, book instances, authors and genre counts (in parallel)
  // const [
  //   numBooks,
  //   numBookInstances,
  //   numAvailableBookInstances,
  //   numAuthors,
  //   numGenres,
  // ] = await Promise.all([
  //   Book.countDocuments({}).exec(),
  //   BookInstance.countDocuments({}).exec(),
  //   BookInstance.countDocuments({ Status: "Available" }).exec(),
  //   Author.countDocuments({}).exec(),
  //   Genre.countDocuments({}).exec(),
  // ]);

  // Get details of books, book instances, authors and genre counts (in parallel)
  // const [
  //   numBooks,
  //   numBookInstances,
  //   numAvailableBookInstances,
  //   numAuthors,
  //   numGenres,
  // ] = await Promise.all([
  //   Book.count({}).then(),
  //   Book.count({}).then(),
  //   Book.count({}).then(),
  //   Book.count({}).then(),
  //   Book.count({}).then()
  // ]);


  









  // const [
  //   numBooks,
  //   numBookInstances,
  //   numAvailableBookInstances,
  //   numAuthors,
  //   numGenres,
  // ] = await Promise.all([
  //   1,
  //   2,
  //   3,
  //   4,
  //   5,
  // ]);






  res.render("index", {
    title: "Local Library Home",
    book_count: numBooks,
    book_instance_count: numBookInstances,
    book_instance_available_count: numAvailableBookInstances,
    author_count: numAuthors,
    genre_count: numGenres,
  });
});

// Display a list of all Books
exports.book_list = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Book List");
});

// Display detail page for a specific Book
exports.book_detail = asyncHandler(async (req, res, next) => {
  res.send(`NOT IMPLEMENTED: Book detail: ${req.params.id}`); // notice the string delimeters we use here! ` ... NOT ' or "
});

// CREATE
// Display Book createform on GET
exports.book_create_get = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Book create GET");
});

// Handle Book create on POST
exports.book_create_post = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Book create POST");
});

// DELETE
// Display Book delete form on GET
exports.book_delete_get = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Book delete GET");
});

// Handle Book delete on POST
exports.book_delete_post = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Book Delete POST");
});

// UPDATE
// Display Book update form on GET
exports.book_update_get = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Book update GET");
});

// Handle Book update on POST
exports.book_update_post = asyncHandler(async (req, res, next) => {
  res.send("NOT IMPLEMENTED: Book update POST");
});
