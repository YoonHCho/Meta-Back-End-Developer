CREATE DATABASE bookstore;


CREATE TABLE customers;


INSERT INTO customers (customerID, customerName, customerAddress)
VALUES (1, "Jack", "115 Old street Belfast");


INSERT INTO customers (customerID, customerName, customerAddress)
VALUES (2, "James", "24 Carlson Rd London");

-- OR to insert multiple rows/data
INSERT INTO customers (customerID, customerName, customerAddress)
VALUES                (3, "Ripper", "123 New street Belfast");
                      (4, "Iron Man", "321 Back end street");


CREATE DATABASE football_club;

CREATE TABLE players (
  id INT,
  name VARCHAR(100),
  age INT
);

CREATE TABLE games (
  gameID INT,
  gameDate DATE,
  score INT
);
