// First crack at this, I was getting permission errors ... this was the solution.
// https://stackoverflow.com/questions/50093144/mysql-8-0-client-does-not-support-authentication-protocol-requested-by-server


var mysql = require("mysql");

var con = mysql.createConnection({
  host: "127.0.0.1",
  user: "root",
  password: "12345",
  database: "MatchDb"
});


con.connect(function(err) {
    if (err) throw err;

    con.query("SELECT MatchUserId FROM MatchDb.Users", function (err, result, fields) {
      if (err) throw err;
      console.log(result);
    });

  });

// con.connect((err) => {
//   if (err) {
//     console.log("Error connecting to Db");
//     return;
//   }
//   console.log("Connection established");
// });

// uncomment the below stuff will cause a problem with sending back the data ...
// con.end((err) => {
//   // The connection is terminated gracefully
//   // Ensures all remaining queries are executed
//   // Then sends a quit packet to the MySQL server.
//   // throw err;
// });
