-- Update columns for a table
UPDATE student_tbl
SET home_address = '123 Back-end', contact_number = '1234567890'
WHERE ID = 3;

UPDATE student_tbl
SET college_address = 'Harper Building'
WHERE department = 'engineering';

-- Delete a record/row
DELETE FROM student_tbl
WHERE last_name = 'Millar';

DELETE FROM student_tbl
WHERE department = 'engineer';

-- will delete all the records from student_tbl
DELETE FROM student_tbl;
TRUNCATE TABLE student_tbl; -- use this to when deleting all records


-- Create new Database, table and records to delete a record
CREATE DATABASE bookshop;

CREATE TABLE customers (customerID INT, customerName VARCHAR(50), customerAddress VARCHAR(255));

INSERT INTO customers (customerID, customerName, customerAddress)
VALUES
(1, 'Jack', '115 Old street Belfast'),
(2, 'James', '24 Carlson Rd London'),
(4, 'Maria', '5 Fredrik Rd, Bedford'),
(5, 'Jade', '10 Copland Ave Portsmouth '),
(6, 'Yasmine', '15 Fredrik Rd, Bedford'),
(3, 'Jimmy', '110 Copland Ave Portsmouth');

-- Delete "Jimmy" using the customerID
DELETE FROM customers WHERE customerID = 3;
-- Delete "Yasmine" using the customerID
DELETE FROM customers WHERE customerID = 5;