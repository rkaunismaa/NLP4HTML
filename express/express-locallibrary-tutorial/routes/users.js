const express = require('express');
const router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

/* GET users listing. */
router.get('/cool', function(req, res, next) {
  res.send('Youre so cool!');
});

module.exports = router;
