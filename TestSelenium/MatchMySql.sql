/*
Code used to generate the db, tables, and keys for the Match stuff.
MySql Workbench
*/

CREATE DATABASE MatchDb;

USE MatchDb;

CREATE TABLE `MatchDb`.`Users` (
  `idUsers` INT NOT NULL,
  `ScanDateTime` DATETIME NULL,
  `Url` VARCHAR(64) NOT NULL,
  `FirstName` VARCHAR(32) NULL,
  `AgeLocation` VARCHAR(64) NULL,
  `Subscriber` TINYINT NULL,
  `LastOnline` VARCHAR(64) NULL,
  `MiniEssayTitle` VARCHAR(32) NULL,
  `MiniEssayContent` VARCHAR(128) NULL,
  `Summary` VARCHAR(4096) NULL,
  PRIMARY KEY (`idUsers`));

CREATE TABLE `MatchDb`.`Images` (
    `idImages` INT NOT NULL,
    `idUsers` INT NOT NULL,
    `Url` VARCHAR(128) NOT NULL,
    PRIMARY KEY (`idImages`));

ALTER TABLE `MatchDb`.`Images` 
    CHANGE COLUMN `Url` `Url` VARCHAR(256) NOT NULL ;

ALTER TABLE `MatchDb`.`Users` 
    CHANGE COLUMN `Url` `Url` VARCHAR(256) NOT NULL ;

ALTER TABLE `MatchDb`.`Users` 
CHANGE COLUMN `ScanDateTime` `ScanDateTime` DATETIME NOT NULL ;

ALTER TABLE `MatchDb`.`Users` 
CHANGE COLUMN `idUsers` `idUsers` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `MatchDb`.`Images` 
CHANGE COLUMN `idImages` `idImages` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `MatchDb`.`Users` 
CHANGE COLUMN `MiniEssayTitle` `MiniEssayTitle` VARCHAR(64) NULL DEFAULT NULL ,
CHANGE COLUMN `MiniEssayContent` `MiniEssayContent` VARCHAR(256) NULL DEFAULT NULL ;


/*
We should probably have the Match User Id in its own field, 
and move the ScanDateTime field to the end of the table
*/
ALTER TABLE `MatchDb`.`Users` 
ADD COLUMN `MatchUserId` VARCHAR(64) NOT NULL AFTER `idUsers`,
CHANGE COLUMN `ScanDateTime` `ScanDateTime` DATETIME NOT NULL AFTER `Summary`;









