create database TECHSHOP_NEW;
use TECHSHOP_NEW

create table customers (
    customerid int primary key,
    firstname varchar(100),
    lastname varchar(100),
    email varchar(100),
    phone varchar(20),
    address varchar(200)
);

create table products (
    productid int primary key,
    productname varchar(100),
    description varchar(255),
    price decimal(10, 2)
);

create table orders (
    orderid int primary key,
    customerid int,
    orderdate date,
    totalamount decimal(10, 2),
    foreign key (customerid) references customers(customerid)
);

create table orderdetails (
    orderdetailid int primary key,
    orderid int,
    productid int,
    quantity int,
    foreign key (orderid) references orders(orderid),
    foreign key (productid) references products(productid)
);

create table inventory (
    inventoryid int primary key,
    productid int,
    quantityinstock int,
    laststockupdate date,
    foreign key (productid) references products(productid)
);


insert into customers values (1, 'john', 'doe', 'john.doe@example.com', '1234567890', '123 elm street');
insert into customers values (2, 'jane', 'smith', 'jane.smith@example.com', '2345678901', '456 oak avenue');
insert into customers values (3, 'michael', 'johnson', 'michael.j@example.com', '3456789012', '789 pine road');
insert into customers values (4, 'emily', 'davis', 'emily.d@example.com', '4567890123', '321 maple lane');
insert into customers values (5, 'david', 'miller', 'david.m@example.com', '5678901234', '654 cedar street');
insert into customers values (6, 'sarah', 'wilson', 'sarah.w@example.com', '6789012345', '987 birch drive');
insert into customers values (7, 'daniel', 'moore', 'daniel.m@example.com', '7890123456', '147 spruce street');
insert into customers values (8, 'linda', 'taylor', 'linda.t@example.com', '8901234567', '258 fir boulevard');
insert into customers values (9, 'robert', 'anderson', 'robert.a@example.com', '9012345678', '369 palm circle');
insert into customers values (10, 'laura', 'thomas', 'laura.t@example.com', '0123456789', '741 willow avenue');



insert into products values (1, 'laptop', '15 inch, 8gb ram, 512gb ssd', 750.00);
insert into products values (2, 'smartphone', '6.5 inch display, 128gb', 500.00);
insert into products values (3, 'headphones', 'noise cancelling', 120.00);
insert into products values (4, 'keyboard', 'mechanical keyboard', 60.00);
insert into products values (5, 'mouse', 'wireless mouse', 30.00);
insert into products values (6, 'monitor', '24 inch full hd', 180.00);
insert into products values (7, 'tablet', '10 inch, 64gb', 300.00);
insert into products values (8, 'printer', 'all-in-one wireless', 200.00);
insert into products values (9, 'webcam', '1080p hd webcam', 70.00);
insert into products values (10, 'external hard drive', '1tb usb 3.0', 90.00);

insert into orders values (1, 1, '2024-03-01', 880.00);
insert into orders values (2, 2, '2024-03-02', 560.00);
insert into orders values (3, 3, '2024-03-03', 300.00);
insert into orders values (4, 4, '2024-03-04', 130.00);
insert into orders values (5, 5, '2024-03-05', 930.00);
insert into orders values (6, 6, '2024-03-06', 180.00);
insert into orders values (7, 7, '2024-03-07', 270.00);
insert into orders values (8, 8, '2024-03-08', 750.00);
insert into orders values (9, 9, '2024-03-09', 120.00);
insert into orders values (10, 10, '2024-03-10', 90.00);

insert into orderdetails values (1, 1, 1, 1);
insert into orderdetails values (2, 1, 3, 1);
insert into orderdetails values (3, 2, 2, 1);
insert into orderdetails values (4, 2, 4, 1);
insert into orderdetails values (5, 3, 7, 1);
insert into orderdetails values (6, 4, 3, 1);
insert into orderdetails values (7, 4, 5, 1);
insert into orderdetails values (8, 5, 1, 1);
insert into orderdetails values (9, 5, 10, 2);
insert into orderdetails values (10, 6, 6, 1);


insert into inventory values (1, 1, 10, '2024-03-01');
insert into inventory values (2, 2, 15, '2024-03-01');
insert into inventory values (3, 3, 25, '2024-03-01');
insert into inventory values (4, 4, 20, '2024-03-01');
insert into inventory values (5, 5, 30, '2024-03-01');
insert into inventory values (6, 6, 12, '2024-03-01');
insert into inventory values (7, 7, 8, '2024-03-01');
insert into inventory values (8, 8, 10, '2024-03-01');
insert into inventory values (9, 9, 18, '2024-03-01');
insert into inventory values (10, 10, 14, '2024-03-01');


                                                     ---Task 2 ---

-- q1: retrieve the names and emails of all customers
select firstname, lastname, email from customers;

-- q2: list all orders with their order dates and corresponding customer names
select o.orderid, o.orderdate, c.firstname, c.lastname
from orders o
join customers c on o.customerid = c.customerid;

-- q3: insert a new customer record into the "customers" table
insert into customers (customerid, firstname, lastname, email, phone, address)
values (11, 'lisa', 'ray', 'lisa.ray@example.com', '9876543210', '45 green street, chicago');

-- q4: update the prices of all electronic gadgets in the "products" table by increasing them by 10%
update products
set price = price * 1.10
where description like '%electronic%';

-- q5: delete a specific order and its associated order details from the "orders" and "orderdetails" tables
delete from orderdetails
where orderid = 1;

-- q6: insert a new order into the "orders" table
insert into orders (orderid, customerid, orderdate, totalamount)
values (106, 1, '2025-04-08', 0.00);  

-- q7: update contact information (email and address) of a specific customer
update customers
set email = 'newemail@example.com',
    address = '123 new street, cityville'
where customerid = 1; 

-- q8: recalculate and update total cost of each order in the "orders" table
update orders
set totalamount = (
    select sum(p.price * od.quantity)
    from orderdetails od
    join products p on od.productid = p.productid
    where od.orderid = orders.orderid
);

--- q9: delete all orders and their associated order details for a specific customer----
delete od
from orderdetails od
join orders o on od.orderid = o.orderid
where o.customerid = 1; -- replace 1 with the desired customer id
-- then delete orders for that customer
delete from orders
where customerid = 1; 

-- q10: insert a new electronic gadget product into the "products" table
insert into products (productid, productname, description, price)
values (11, 'wireless earbuds', 'bluetooth-enabled earbuds with noise cancellation', 2499.00);

alter table orders
add status varchar(20);

-- q11: update the status of a specific order in the "orders" table
update orders
set status = 'shipped'
where orderid = 3;

--q12 Write an SQL query to calculate and update the number of orders placed by each customer 

alter table Customers
add OrderCount int;

update Customers
set OrderCount = (
    select COUNT(*)
    from Orders
    where Orders.CustomerID = Customers.CustomerID
);



                                                        ---Task3----

-- q1: retrieve a list of all orders along with customer information
select o.orderid, o.orderdate, c.firstname, c.lastname, c.email
from orders o
join customers c on o.customerid = c.customerid;

-- q2: find the total revenue generated by each electronic gadget product
select p.productname, sum(od.quantity * p.price) as total_revenue
from orderdetails od
join products p on od.productid = p.productid
group by p.productname;

-- q3: list all customers who have made at least one purchase
select distinct c.customerid, c.firstname, c.lastname, c.email, c.phone, c.address
from customers c
join orders o on c.customerid = o.customerid;

-- q4: find the most popular electronic gadget (highest total quantity ordered)
select top 1 p.productname, sum(od.quantity) as total_quantity_ordered
from orderdetails od
join products p on od.productid = p.productid
group by p.productname
order by total_quantity_ordered desc;

-- q5: retrieve a list of electronic gadgets along with their corresponding categories
select productid, productname
from products;

-- q6. average order value per customer
select c.customerid,c.firstname + ' ' + c.lastname as customer_name,
avg(o.totalamount) as average_order_value
from customers c
join orders o on c.customerid = o.customerid
group by c.customerid, c.firstname, c.lastname;

-- q7. order with the highest total revenue
select top 1 o.orderid,c.firstname + ' ' + c.lastname as customer_name,c.email,o.totalamount as total_revenue
from orders o
join customers c on o.customerid = c.customerid
order by o.totalamount desc;

-- q8. list products and number of times each was ordered
select p.productname,count(od.orderdetailid) as times_ordered
from products p
join orderdetails od on p.productid = od.productid
group by p.productname
order by times_ordered desc;

-- q9. find customers who purchased a specific product
select c.firstname,c.lastname,c.email,p.productname
from customers c
join orders o on c.customerid = o.customerid
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where p.productname = 'mouse';  

--q10.Write an SQL query to calculate the total revenue generated by all orders placed within a specific date
select sum(od.quantity * p.price) as total_revenue
from  orders o
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where o.orderdate between '2024-01-01' and '2024-12-31';

												 
												 

												  
												 --- Task4----

-- q1: find customers who have not placed any orders
select customerid, firstname, lastname
from customers

where customerid not in (select customerid from orders);
-- q2: find total number of products available for sale
select count(*) as total_products
from products;

-- q3: calculate total revenue from all orders
select sum(od.quantity * p.price) as total_revenue
from orderdetails od
join products p on od.productid = p.productid;

-- q4: calculate average quantity ordered for products like '%laptop%' (you can change this as needed)
select avg(quantity) as avg_quantity
from orderdetails
where productid in (
    select productid from products where productname like '%laptop%'
);

-- q5: calculate total revenue by specific customer
select sum(od.quantity * p.price) as total_revenue
from orders o
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid
where o.customerid = 3;

-- q6: find customers who placed the most orders
select customerid, firstname, lastname, order_count
from (select c.customerid, c.firstname, c.lastname, count(o.orderid) as order_count from customers c
 join orders o on c.customerid = o.customerid
 group by c.customerid, c.firstname, c.lastname
) as customer_orders
where order_count = (select max(order_count) from ( select count(orderid) as order_count from orders
        group by customerid
    ) as order_counts
);

-- q7: find the most popular product (highest quantity ordered)
select productid, productname, total_quantity
from (
    select p.productid, p.productname, sum(od.quantity) as total_quantity
    from products p
    join orderdetails od on p.productid = od.productid
    group by p.productid, p.productname
) as product_sales
where total_quantity = (
    select max(total_quantity)
    from (
        select sum(quantity) as total_quantity
        from orderdetails
        group by productid
    ) as totals
);

-- q8: find the customer who has spent the most
select customerid, firstname, lastname, total_spent
from (
    select c.customerid, c.firstname, c.lastname, sum(od.quantity * p.price) as total_spent
    from customers c
    join orders o on c.customerid = o.customerid
    join orderdetails od on o.orderid = od.orderid
    join products p on od.productid = p.productid
    group by c.customerid, c.firstname, c.lastname
) as spending
where total_spent = (
    select max(total_spent) from (
        select sum(od.quantity * p.price) as total_spent
        from orders o
        join orderdetails od on o.orderid = od.orderid
        join products p on od.productid = p.productid
        group by o.customerid
    ) as totals
);

-- q9: calculate average order value (total revenue / total number of orders)
select sum(od.quantity * p.price) / count(distinct o.orderid) as avg_order_value
from orders o
join orderdetails od on o.orderid = od.orderid
join products p on od.productid = p.productid;

-- q10: total number of orders placed by each customer
select c.customerid, c.firstname, c.lastname, count(o.orderid) as total_orders
from customers c
left join orders o on c.customerid = o.customerid
group by c.customerid, c.firstname, c.lastname;
