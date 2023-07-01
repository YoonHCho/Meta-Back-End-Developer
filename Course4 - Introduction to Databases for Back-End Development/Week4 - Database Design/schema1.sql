-- CREATE A SCHEMA

CREATE DATABASE shopping_cart_db;

CREATE TABLE customer (
	customer_id INT AUTO_INCREMENT, -- AUTO_INCREMENT to let the table insert unique values automatically
	name VARCHAR(100),
	address VARCHAR(255),
	email VARCHAR(10),
	phone VARCHAR(10),
	PRIMARY KEY (customer_id)
);

CREATE TABLE product (
	product_id INT AUTO_INCREMENT,
	name VARCHAR(100),
	price NUMERIC (8, 2),
	description VARCHAR(255),
	PRIMARY KEY (product_id)
);

CREATE TABLE cart_order (
	order_id INT AUTO_INCREMENT,
	customer_id INT,
	product_id INT,
	quantity INT,
	order_date DATE,
	status VARCHAR(100),
	PRIMARY KEY (order_id),
	-- FOREIGN KEY points to the external source table/referenced table. this is to establish a relationship with other table.
	FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
	FOREIGN KEY (product_id) REFERENCES product(product_id),
);

CREATE TABLE Staff (
    Email VARCHAR(200) NOT NULL,
    Name VARCHAR(255) NOT NULL,
    CONSTRAINT PK_Email PRIMARY KEY (Email) -- will ensures that each value in the "Email" column is unique and serves as the primary key for the table
);

CONSTRAINT SalesID PRIMARY KEY (customerID, productID); -- will create a PRIMARY KEY column SalesID, the value is made up of (customerID + productID)