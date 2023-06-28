-- Exercise - working with numbers
-- TINYINT, SMALLINT, INT OR INTEGER, BIGINT, FLOAT, DEC OR DECIMAL, DOUBLE etc
CREATE TABLE devices (
  deviceID INT,
  deviceName VARCHAR(50),
  price DECIMAL(10, 2)  -- can store a total of 10 digits, with 2 of those digits reserved for decimal places. 12345678.90
);

CREATE TABLE stock (
  deviceID INT,
  quantity INT,
  totalCost DECIMAL(10, 2)
);

-- Exercise - working with strings
-- CHAR(size), VARCHAR(size), TINYTEXT, TEXT(size), MEDIUMTEXT, LONGTEXT
CREATE TABLE customers (
  username CHAR(10),
  fullName VARCHAR(100),
  email VARCHAR(255)
);

CREATE TABLE feedback (
  feedbackID CHAR(8),
  feedbackType VARCHAR(100),
  comment TEXT(500)
);

-- Exercise - working with default values
CREATE TABLE Address (
  id int NOT NULL,
  street VARCHAR(255),
  postcode VARCHAR(10) DEFAULT "HA97DE",
  town VARCHAR(30) DEFAULT "Harrow"
);

-- Choosing the right data type for a column
CREATE TABLE invoice (
  customerID VARCHAR(50),
  orderDate DATE,
  quantity INT,
  price DECIMAL
);

CREATE TABLE contact (
  acctNum INT,
  phone INT,
  email VARCHAR(50)
);

