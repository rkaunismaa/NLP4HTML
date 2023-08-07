/* sql code to create the target MySql database */

CREATE DATABASE `LocalLibraryDB`

CREATE TABLE `LocalLibraryDB`.`Author` (
  `idAuthor` INT NOT NULL,
  `FirstName` VARCHAR(100) NOT NULL,
  `FamilyName` VARCHAR(100) NOT NULL,
  `DateOfBirth` DATE NULL,
  `DateOfDeath` DATE NULL,
  PRIMARY KEY (`idAuthor`));

  CREATE TABLE `LocalLibraryDB`.`Book` (
  `idBook` INT NOT NULL,
  `Title` VARCHAR(45) NOT NULL,
  `idAuthor` INT NOT NULL,
  `Summary` VARCHAR(2048) NOT NULL,
  `ISBN` VARCHAR(45) NULL,
  `idGenre` INT NULL,
  PRIMARY KEY (`idBook`));

  CREATE TABLE `LocalLibraryDB`.`BookInstance` (
  `idBookInstance` INT NOT NULL,
  `idBook` INT NOT NULL,
  `Imprint` VARCHAR(45) NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `DueBack` DATE NULL,
  PRIMARY KEY (`idBookInstance`));

  CREATE TABLE `LocalLibraryDB`.`Genre` (
  `idGenre` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idGenre`));

ALTER TABLE LocalLibraryDB.Book
ADD CONSTRAINT FK_AuthorBook
FOREIGN KEY (idAuthor) REFERENCES Author(idAuthor);

ALTER TABLE LocalLibraryDB.Book
ADD CONSTRAINT FK_GenreBook
FOREIGN KEY (idGenre) REFERENCES Genre(idGenre);

ALTER TABLE LocalLibraryDB.BookInstance
ADD CONSTRAINT FK_BookBookInstance
FOREIGN KEY (idBook) REFERENCES Book(idBook);

ALTER TABLE LocalLibraryDB.Author AUTO_INCREMENT=1;
ALTER TABLE LocalLibraryDB.Book AUTO_INCREMENT=1;
ALTER TABLE LocalLibraryDB.BookInstance AUTO_INCREMENT=1;
ALTER TABLE LocalLibraryDB.Genre AUTO_INCREMENT=1;
