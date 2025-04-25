create database CMS;

use CMS;

CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-increment for UserID
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    Password VARCHAR(255),
    ContactNumber VARCHAR(20),
    Address TEXT
);

CREATE TABLE Courier (
    CourierID INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-increment for CourierID
    SenderName VARCHAR(255),
    SenderAddress TEXT,
    ReceiverName VARCHAR(255),
    ReceiverAddress TEXT,
    Weight DECIMAL(5, 2),
    Status VARCHAR(50),
    TrackingNumber VARCHAR(20) UNIQUE,
    DeliveryDate DATE
);

CREATE TABLE CourierServices (
    ServiceID INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-increment for ServiceID
    ServiceName VARCHAR(100),
    Cost DECIMAL(8, 2)
);

CREATE TABLE Employee (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-increment for EmployeeID
    Name VARCHAR(255),
    Email VARCHAR(255) UNIQUE,
    ContactNumber VARCHAR(20),
    Role VARCHAR(50),
    Salary DECIMAL(10, 2)
);

CREATE TABLE Location (
    LocationID INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-increment for LocationID
    LocationName VARCHAR(100),
    Address TEXT
);

CREATE TABLE Payment (
    PaymentID INT IDENTITY(1,1) PRIMARY KEY,  -- Auto-increment for PaymentID
    CourierID INT,
    LocationID INT,
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    FOREIGN KEY (CourierID) REFERENCES Courier(CourierID),  -- Corrected reference to Courier table
    FOREIGN KEY (LocationID) REFERENCES Location(LocationID)
);

INSERT INTO Users (Name, Email, Password, ContactNumber, Address)
VALUES
('John Doe', 'john.doe@example.com', 'password123', '1234567890', '123 Main St, City, Country'),
('Jane Smith', 'jane.smith@example.com', 'password456', '0987654321', '456 Elm St, City, Country');

INSERT INTO Courier (SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate)
VALUES
('John Doe', '123 Main St, City, Country', 'Alice Brown', '789 Pine St, City, Country', 5.50, 'In Transit', 'TN12345', '2025-04-25'),
('Jane Smith', '456 Elm St, City, Country', 'Bob White', '101 Maple St, City, Country', 3.00, 'Delivered', 'TN12346', '2025-04-20');

INSERT INTO CourierServices (ServiceName, Cost)
VALUES
('Standard Shipping', 20.00),
('Express Shipping', 50.00),
('Overnight Shipping', 100.00);

INSERT INTO Employee (Name, Email, ContactNumber, Role, Salary)
VALUES
('Alice Johnson', 'alice.johnson@example.com', '1122334455', 'Courier Driver', 35000.00),
('Bob Williams', 'bob.williams@example.com', '2233445566', 'Customer Support', 40000.00);

INSERT INTO Location (LocationName, Address)
VALUES
('Warehouse A', '123 Warehouse Rd, City, Country'),
('Warehouse B', '456 Industrial St, City, Country');

INSERT INTO Payment (CourierID, LocationID, Amount, PaymentDate)
VALUES
(1, 1, 20.00, '2025-04-21'),
(2, 2, 50.00, '2025-04-20');

SELECT * FROM Users;
SELECT * FROM Courier;
SELECT * FROM CourierServices;
SELECT * FROM Employee;
SELECT * FROM Location;
SELECT * FROM Payment;

SELECT * FROM Courier WHERE TrackingNumber = 'TN12345';

SELECT Status, COUNT(*) FROM Courier GROUP BY Status;

SELECT Status, SUM(Weight * 10) AS Revenue 
FROM Courier 
GROUP BY Status;



-- 1. Inserting a new courier.
--- q: Verify that the new courier is inserted correctly into the Courier table

SELECT * FROM Courier WHERE TrackingNumber = 'TN12345';

--- 2. Updating the courier status.
-- q: Verify that the status of the courier with tracking number 'TN12345' has been updated.

SELECT TrackingNumber, Status FROM Courier WHERE TrackingNumber = 'TN12345';

---- 3. Retrieving courier details.
---- q: Verify that the details of the courier are correct.

SELECT * FROM Courier WHERE TrackingNumber = 'TN12345';

--- 4. Generating a shipment status report.
---q: Verify that the shipment status report is generated correctly, showing the count of couriers for each status.

SELECT Status, COUNT(*) AS Total FROM Courier GROUP BY Status;

--- 5. Generating a revenue report.
---q: Verify that the revenue report is generated correctly, showing the total revenue for each status.
ALTER TABLE Courier
ADD Revenue DECIMAL(10, 2);


SELECT Status, SUM(Revenue) AS TotalRevenue 
FROM Courier 
WHERE Status = 'Delivered'
GROUP BY Status;

SELECT CourierID, TrackingNumber, Revenue FROM Courier WHERE Status = 'Delivered';

SELECT c.Status, SUM(p.Amount) AS TotalRevenue
FROM Payment p
JOIN Courier c ON c.CourierID = p.CourierID
GROUP BY c.Status;
