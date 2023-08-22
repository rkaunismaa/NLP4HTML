var express = require('express');
var router = express.Router();

const users_controller = require("../controllers/usersController");

// /* GET users listing. */
// router.get('/', function(req, res, next) {
//   // res.send('respond with a resource');

//   router.get("/books", book_controller.book_list);

// });

router.get("/", users_controller.user_list);

module.exports = router;
