const express = require('express');
const mysql = require('mysql');
const app = express();

// Replace these configuration values with your actual database settings
const dbConfig = {
    host: "127.0.0.1",
    user: "root",
    password: "12345",
    database: "MatchDb"
};

const connection = mysql.createConnection(dbConfig);

// Connect to the MySQL database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to the database:', err);
    return;
  }
  console.log('Connected to the database');
});

// Set the view engine to EJS
app.set('view engine', 'ejs');

// Route to display data from the database
app.get('/', (req, res) => {
  const sqlQuery = 'SELECT MatchUserId, FirstName, AgeLocation, Summary FROM MatchDb.Users';
  connection.query(sqlQuery, (err, results) => {
    if (err) {
      console.error('Error executing the query:', err);
      res.status(500).send('Internal Server Error');
    } else {
      // Render the 'index.ejs' template and pass the data from the database
      res.render('index', { users: results });
    }
  });
});

// Start the server on port 3000 (you can change the port number if needed)
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}/`);
});
