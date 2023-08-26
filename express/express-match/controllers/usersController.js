const db = require('../models/init-models');
const asyncHandler = require("express-async-handler");
const fs = require('fs');

const { Op } = require("sequelize");

// Display a list of all Users
exports.user_list = asyncHandler(async (req, res, next) => {
  
  // res.send("NOT IMPLEMENTED: Users List");

  const allUsers = await db.models.Users.findAll({});

  // const allUsers = await db.models.Users.findAll( {
  //   where: {
  //     Subscriber: 1
  //   }
  // });

  // const allUsers = await db.models.Users.findAll(  {
  //   where: {
  //     [Op.or]: [
  //       { Subscriber: {[Op.eq]: 1 } },
  //       { LastOnline: {[Op.ne]: ''}} 
  //     ]
  //   }
  // });


  // const allUsers = await db.models.Users.findAll(  {
  //   where: {
  //     [Op.and]: [
  //       { Subscriber: {[Op.eq]: 0 } },
  //       { LastOnline: {[Op.eq]: ''}} 
  //     ]
  //   }
  // });

res.render("user_list", { user_list: allUsers });

});

exports.show_images = asyncHandler(async (req, res, next) => {

  idUserId = req.params.id ;

  const [
    user,
    images
  ] = await Promise.all([
    db.models.Users.findByPk(idUserId),
    db.models.Images.findAll( {
      where: {
        idUsers: idUserId
      }
    })
  ]);

  matchUserId = user.MatchUserId ;

  // generate the list of file names
  imageFolder = '/images/' + matchUserId + '/';
  var fileSystemimages = [];

  fs.readdirSync('./public' + imageFolder).forEach(function(file) {
    fsName = imageFolder + file ;
    imageNote = '';
    fileSystemimages.push([fsName, imageNote]);
});

fsiLength = fileSystemimages.length;
for (let i = 0; i < fsiLength; i++) {

  fullImageName = fileSystemimages[i];
  fullImageNameParts = fullImageName[0].split('/');
  fsImageName = fullImageNameParts[fullImageNameParts.length -1];
  // Scan images for this name
  imageNote = '' ;
  // Mark our selected genres as checked.
  for (const image of images) {
    url = image.Url;
    message = image.Message;
    if (url.endsWith(fsImageName)) {
      imageNote = message;
    }
  }
  fullImageName[1] = imageNote;
}

  res.render("images", { idUserId : idUserId, matchUserId: matchUserId, fileSystemimages : fileSystemimages, firstName : user.FirstName, ageLocation : user.AgeLocation, rating : user.Rating });

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
  
