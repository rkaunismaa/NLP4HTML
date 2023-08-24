const db = require('../models/init-models');
const asyncHandler = require("express-async-handler");
const fs = require('fs');

const { Op } = require("sequelize");

// Display a list of all Users
exports.user_list = asyncHandler(async (req, res, next) => {
  
  // res.send("NOT IMPLEMENTED: Users List");

  // const allUsers = await db.models.Users.findAll( {
  //   where: {
  //     Subscriber: 1
  //   }
  // });

  const allUsers = await db.models.Users.findAll(  {
    where: {
      [Op.or]: [
        { Subscriber: {[Op.eq]: 1 } },
        { LastOnline: {[Op.ne]: ''}} 
      ]
    }
  });

  res.render("user_list", { user_list: allUsers });

});

exports.show_images = asyncHandler(async (req, res, next) => {

  matchUserId = req.params.MatchUserId ;

  // generate the list of file names
  //const images = fs.readdirSync('/images/D6056eiH_oM-UZNn2IPWIw2/');
  imageFolder = '/images/' + matchUserId + '/';

  var images = [];

  fs.readdirSync('./public' + imageFolder).forEach(function(file) {
    images.push(imageFolder + file);
});

// const images2 = ['asdf', 'bsre'] ;

  // console.log(images);

  res.render("images", { matchUserId: matchUserId, images : images });

});




// Copy/pasted from the working project, to see as a guide ... THIS CODE WILL NOT WORK HERE!
exports.index = asyncHandler(async (req, res, next) => {
  // Get details of books, book instances, authors and genre counts (in parallel)
  const [
    numBooks,
    numBookInstances,
    numAvailableBookInstances,
    numAuthors,
    numGenres,
  ] = await Promise.all([
    Book.countDocuments({}).exec(),
    BookInstance.countDocuments({}).exec(),
    BookInstance.countDocuments({ status: "Available" }).exec(),
    Author.countDocuments({}).exec(),
    Genre.countDocuments({}).exec(),
  ]);

  res.render("index", {
    title: "Local Library Home",
    book_count: numBooks,
    book_instance_count: numBookInstances,
    book_instance_available_count: numAvailableBookInstances,
    author_count: numAuthors,
    genre_count: numGenres,
  });
});


// Copy/pasted from the working project, to see as a guide ... THIS CODE WILL NOT WORK HERE!
exports.book_list = asyncHandler(async (req, res, next) => {

  const allBooks = await Book.find({}, "title author")
    .sort({ title: 1 })
    .populate("author")
    .exec();

  res.render("book_list", { title: "Book List", book_list: allBooks });

});
  
