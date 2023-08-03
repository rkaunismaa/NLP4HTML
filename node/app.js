const express = require("express");
const mysql = require("mysql");
const app = express();
const fs = require('fs');
const path = require("path");

// Serve static files from the 'matchImages' directory
app.use(express.static("public"));

// Replace these configuration values with your actual database settings
const dbConfig = {
  host: "127.0.0.1",
  user: "root",
  password: "12345",
  database: "MatchDb",
};

const connection = mysql.createConnection(dbConfig);

// Connect to the MySQL database
connection.connect((err) => {
  if (err) {
    console.error("Error connecting to the database:", err);
    return;
  }
  console.log("Connected to the database");
});

// Set the view engine to EJS
app.set("view engine", "ejs");

// Route to display data from the database
app.get("/", (req, res) => {
  const sqlQuery =
    "SELECT MatchUserId, FirstName, AgeLocation, LastOnLine, MiniEssayTitle, MiniEssayContent, Summary FROM MatchDb.Users WHERE LastOnline != '' AND Subscriber is True AND Summary != '' ORDER BY AgeLocation";
  connection.query(sqlQuery, (err, results) => {
    if (err) {
      console.error("Error executing the query:", err);
      res.status(500).send("Internal Server Error");
    } else {
      // Render the 'index.ejs' template and pass the data from the database
      res.render("index", { users: results });
    }
  });
});

// Start the server on port 3000 (you can change the port number if needed)
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}/`);
});

// const server = http.createServer((req, res) => {
//   // Check the requested URL and serve the appropriate file
//   if (req.url === '/') {
//       // Serve the HTML file
//       const htmlFilePath = path.join(__dirname, 'match.html');
//       fs.readFile(htmlFilePath, 'utf8', (err, data) => {
//           if (err) {
//               res.writeHead(500, { 'Content-Type': 'text/plain' });
//               res.end('Internal Server Error');
//           } else {
//               res.writeHead(200, { 'Content-Type': 'text/html' });
//               res.end(data);
//           }
//       });
//   } else if (req.url.startsWith('/images/')) {
//       // Serve images
//       const imagePath = path.join(__dirname, req.url);
//       fs.readFile(imagePath, (err, data) => {
//           if (err) {
//               res.writeHead(404, { 'Content-Type': 'text/plain' });
//               res.end('Image not found');
//           } else {
//               res.writeHead(200, { 'Content-Type': 'image/jpeg' }); // Change the content type according to your image format
//               res.end(data);
//           }
//       });
//   } else {
//       // Handle other requests
//       res.writeHead(404, { 'Content-Type': 'text/plain' });
//       res.end('Page not found');
//   }
// });




// Route to serve JSON data for user images
app.get("/images/:userId", (req, res) => {

  const userId = req.params.userId;
  const imagePath = path.join(__dirname, "..", "matchImages", `${userId}`);

  try {
    // Read the user directory synchronously
    const files = fs.readdirSync(imagePath);

    // Filter only image files (you may customize the filter based on your image extensions)
    const imageFiles = files.filter((file) => /\.(png|jpe?g|gif)$/i.test(file));

    res.json(imageFiles);
  } catch (err) {
    console.error("Error reading the images directory:", err);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// // Route to serve user images
// app.get('/images/:userId/:imageName', (req, res) => {

//   const userId = req.params.userId;
//   const imageName = req.params.imageName;

//   const imagePath = path.join(__dirname, '..', 'matchImages', `${userId}`, imageName);

//   fs.readFile(imagePath, (err, data) => {
//     if (err) {
//       console.error('Error reading the image file:', err);
//       res.status(500).send('Internal Server Error');
//     } else {
//       const extension = path.extname(imageName).toLowerCase();
//       let contentType = 'image/jpeg'; // Default to JPEG format
//       if (extension === '.png') {
//         contentType = 'image/png';
//       } else if (extension === '.gif') {
//         contentType = 'image/gif';
//       }

//       res.set('Content-Type', contentType);
//       res.send(data);
//     }
//   });
// });

