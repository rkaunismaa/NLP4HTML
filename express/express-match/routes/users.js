var express = require('express');
var router = express.Router();

const users_controller = require("../controllers/usersController");

// For this method, we do not need to hit the database, so no controller method needed,
// just do everything in here ...
// router.get('/showImages/:MatchUserId', function(req, res, next) {
//   res.send('ShowImages for MatchUserId => ' + req.params.MatchUserId);
// });

router.get("/showImages/:MatchUserId", users_controller.show_images) ;

router.get("/", users_controller.user_list);

module.exports = router;
