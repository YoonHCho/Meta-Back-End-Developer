CREATE DATABASE lab;

CREATE TABLE Employee (
	EmployeeId INT AUTO_INCREMENT,
	LastName VARCHAR(20),
	FirstName VARCHAR(20),
	Title VARCHAR(30),
	ReportsTo INT,
	BirthDate DATE,
	HireDate DATE,
	Address VARCHAR(70),
	PRIMARY KEY (EmployeeId)
);

CREATE TABLE Customers (
	CustomerId INT AUTO_INCREMENT,
	LastName VARCHAR(20),
	FirstName VARCHAR(20),
	Company VARCHAR(30),
	Phone VARCHAR(20),
	Email VARCHAR(100)
	City VARCHAR(20),
	Address VARCHAR(70),
	SupportId INT,
	PRIMARY KEY (CustomerId),
	FOREIGN KEY SupportId REFERENCES Employee (EmployeeId)
);

CREATE TABLE Invoices (
	InvoiceId INT AUTO_INCREMENT,
	CustomerId INT,
	InvoiceDate DATE,
	BillingAddress VARCHAR(100),
	BillingCity VARCHAR(50),
	TrackId INT,
	PRIMARY KEY (InvoiceId),
	FOREIGN KEY BillingAddress REFERENCES Customers (Address),
	FOREIGN KEY BillingCity REFERENCES Customers (City),
	FOREIGN KEY CustomerId REFERENCES Customers (CustomerId),
	FOREIGN KEY TrackId REFERENCES Tracks (TrackId)
);

CREATE TABLE Artists (
	ArtistId INT AUTO_INCREMENT,
	Name VARCHAR(120),
	LocationId INT,
	PRIMARY KEY (ArtistId),
	FOREIGN KEY LocationId REFERENCES Location (LocationId)
);

CREATE TABLE Albums (
	AlbumId INT AUTO_INCREMENT,
	Title VARCHAR(160),
	ArtistId INT,
	PRIMARY KEY (AlbumId),
	FOREIGN KEY (ArtistId) REFERENCES Artists (ArtistId)
);

CREATE TABLE Tracks (
	TrackId INT AUTO_INCREMENT,
	Name VARCHAR(200),
	ArtistId INT,
	UnitPrice DECIMAL (5, 2),
	AlbumId INT,
	PRIMARY KEY (TrackId),
	FOREIGN KEY ArtistId REFERENCES Artists (ArtistId),
	FOREIGN KEY AlbumId REFERENCES Albums (AlbumId)
);

CREATE TABLE Location (
	LocationId INT AUTO_INCREMENT,
	City VARCHAR(100),
	Country VARCHAR(100),
	PRIMARY KEY (LocationId),
);