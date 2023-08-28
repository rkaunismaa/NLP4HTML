var express = require('express');
var router = express.Router();

const users_controller = require("../controllers/usersController");

// For this method, we do not need to hit the database, so no controller method needed,
// just do everything in here ...
// router.get('/showImages/:MatchUserId', function(req, res, next) {
//   res.send('ShowImages for MatchUserId => ' + req.params.MatchUserId);
// });

router.get("/showImages/:id", users_controller.show_images) ;

// The route signature and method is specified here, 
// along with the controller and controller method you want to target ...
router.post("/showImages/:id", users_controller.show_images_post) ;

router.get("/", users_controller.user_list);

module.exports = router;
