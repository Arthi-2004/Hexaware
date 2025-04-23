create database TECHSHOP_NEW1;
use TECHSHOP_NEW1;

-- Create Customers table with auto-incrementing customerid
create table customers (
    customerid int identity(1,1) primary key,
    firstname varchar(100),
    lastname varchar(100),
    email varchar(100),
    phone varchar(20),
    address varchar(200)
);

-- Create Products table with auto-incrementing productid
create table products (
    productid int identity(1,1) primary key,
    productname varchar(100),
    description varchar(255),
    price decimal(10, 2)
);

-- Create Orders table with auto-incrementing orderid
create table orders (
    orderid int identity(1,1) primary key,
    customerid int,
    orderdate date,
    totalamount decimal(10, 2),
    foreign key (customerid) references customers(customerid)
);

-- Create OrderDetails table with auto-incrementing orderdetailid
create table orderdetails (
    orderdetailid int identity(1,1) primary key,
    orderid int,
    productid int,
    quantity int,
    foreign key (orderid) references orders(orderid),
    foreign key (productid) references products(productid)
);

-- Create Inventory table with auto-incrementing inventoryid
create table inventory (
    inventoryid int identity(1,1) primary key,
    productid int,
    quantityinstock int,
    laststockupdate date,
    foreign key (productid) references products(productid)
);

insert into customers (firstname, lastname, email, phone, address) values
('John', 'Doe', 'john.doe@example.com', '1234567890', 'XYZ Avenue');

insert into products (productname, description, price) values
('Laptop', 'Dell Inspiron 15', 75000.00),
('Mouse', 'Wireless Mouse', 500.00),
('Keyboard', 'Mechanical Keyboard', 2000.00);

SELECT * FROM customers;
delete from customers where customerid = 4;

-- Insert an order for customer with customerid = 1
insert into orders (customerid, orderdate, totalamount) values
(1, '2025-04-20', 77000.00);

-- Ensure the order was inserted
SELECT * FROM orders;  -- Check the order that was inserted

-- After confirming the order is inserted, insert order details for the order
insert into orderdetails (orderid, productid, quantity) values
(3, 1, 1),   -- Product 1 (Laptop)
(4, 2, 1);   -- Product 2 (Mouse)

-- Check inserted orders and order details
SELECT * FROM orders;
SELECT * FROM orderdetails;
select * from products;
select * from customers;
SELECT productid, productname FROM products;

select * from inventory;
-- Insert inventory data for the products
insert into inventory (productid, quantityinstock, laststockupdate) values
(1, 10, '2025-04-20'),  -- Laptop: 10 items vsin stock
(2, 50, '2025-04-20'),  -- Mouse: 50 items in stock
(3, 30, '2025-04-20');  -- Keyboard: 30 items in stock

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'orders';

SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'products';

