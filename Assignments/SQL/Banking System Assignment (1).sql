-- Database creation----
CREATE DATABASE HMBank1;
---Use Database---
USE HMBank1;   

                                                          -------------TASK1----------

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    email VARCHAR(100),
    phone_number VARCHAR(15),
    address VARCHAR(100));

CREATE TABLE Accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(20),
    balance DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id));

CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_type VARCHAR(20),
    amount DECIMAL(10, 2),
    transaction_date DATE,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id));


                                               -------------TASK2-----------


INSERT INTO customers (customer_id, first_name, last_name, dob, email, address, phone_number) VALUES
(1, 'Aarav', 'Mehta', '2001-04-12', 'aarav.mehta@example.com', 'New York', '9876543210'),
(2, 'Kiara', 'Singh', '2016-07-23', 'kiara.singh@example.com', 'Bangkok', '9123456789'),
(3, 'Zayn', 'Ali', '2004-10-30', 'zayn.ali@example.com', 'Las Vegas', '9012345678'),
(4, 'Mira', 'Kapoor', '2005-01-05', 'mira.kapoor@example.com', 'Los Angeles', '9998887776'),
(5, 'Rian', 'Sharma', '2008-09-12', 'rian.sharma@example.com', 'Paris', '9871234560'),
(6, 'Avni', 'Joshi', '2009-03-19', 'avni.joshi@example.com', 'Italy', '9823456789'),
(7, 'Dev', 'Desai', '2005-06-07', 'dev.desai@example.com', 'Milan', '9745612389'),
(8, 'Inaya', 'Reddy', '2006-08-15', 'inaya.reddy@example.com', 'Venice', '9638527410'),
(9, 'Arjun', 'Malik', '2007-11-21', 'arjun.malik@example.com', 'Oakland', '9988776655'),
(10, 'Saanvi', 'Patel', '2013-12-11', 'saanvi.patel@example.com', 'Seoul', '9090909090');



insert into accounts (account_id, customer_id, account_type, balance) values
(101, 1, 'savings', 1500.00),
(102, 2, 'current', 2500.00),
(103, 3, 'zero_balance', 0.00),
(104, 4, 'savings', 0.00),
(105, 5, 'current', 3200.00),
(106, 6, 'savings', 800.00),
(107, 7, 'current', 1200.00),
(108, 8, 'savings', 0.00),
(109, 9, 'zero_balance', 50.00),
(110, 10, 'savings', 700.00);

insert into transactions (transaction_id, account_id, transaction_type, amount, transaction_date) values
(1001, 101, 'deposit', 500.00, '2024-04-01'),
(1002, 102, 'withdrawal', 200.00, '2024-04-02'),
(1003, 103, 'deposit', 50.00, '2024-04-03'),
(1004, 104, 'withdrawal', 50.00, '2024-04-04'),
(1005, 105, 'transfer', 300.00, '2024-04-05'),
(1006, 106, 'deposit', 200.00, '2024-04-06'),
(1007, 107, 'withdrawal', 100.00, '2024-04-07'),
(1008, 108, 'deposit', 150.00, '2024-04-08'),
(1009, 109, 'transfer', 50.00, '2024-04-08'),
(1010, 110, 'deposit', 100.00, '2024-04-08');

---------1.Write a SQL query to retrieve the name, account type and email of all customers. 
select c.first_name, c.last_name, 
a.account_type, c.email
from customers c
join accounts a on c.customer_id = a.customer_id;

---2.Write a SQL query to list all transaction corresponding customer
select t.transaction_id, t.transaction_type, 
t.amount, c.first_name, c.last_name 
from transactions t 
join accounts a on t.account_id = a.account_id
join customers c on a.customer_id = c.customer_id;

---3.Write a SQL query to increase the balance of a specific account by a certain amount.
update accounts 
set balance = balance + 200 
where account_id = 101;

---4Write a SQL query to Combine first and last names of customers as a full_name.
select concat(first_name, ' ', last_name) 
as full_name 
from customers;

--5.Write a SQL query to remove accounts with a balance of zero where the account type is savings.
delete from accounts 
where balance = 0 
and account_type = 'savings';

---6.Write a SQL query to Find customers living in a specific city
select * from customers 
where address like 'Paris';

---7.Write a SQL query to Get the account balance for a specific account.
select balance 
from accounts
where account_id = 105;

---8.Write a SQL query to List all current accounts with a balance greater than $1,000.
select * from accounts 
where account_type = 'current'
and balance > 1000;

--9.Write a SQL query to Retrieve all transactions for a specific account.
select * from transactions
where account_id = 101;

----10.Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate

select account_id,customer_id,
balance,
balance * 0.05 as interest_accrued 
from accounts 
where account_type = 'savings';

----11.Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit.
select *from accounts
where balance < 100.00;

-- 12.Write a SQL query to Find customers not living in a specific city
select 
*from customers 
where address not like 'Venice';
                                           ------------TASK3-------------

---1.Write a SQL query to Find the average account balance for all customers
select avg(balance) 
as average_balance
from accounts;

----2.Write a SQL query to Retrieve the top 10 highest account balances
select top 10 
*from accounts 
order by balance desc;

----3.Write a SQL query to Calculate Total Deposits for All Customers in specific date.
select sum(amount) as total_deposits 
from transactions
where transaction_type = 'deposit'
and transaction_date  = '2024-04-06'; 

--4.Write a SQL query to Find the Oldest and Newest Customers.
select top 1 * from customers order by dob;         
select top 1 * from customers order by dob desc; 

-----5.-Write a SQL query to Retrieve transaction details along with the account type
select t.*, a.account_typE
from transactions t 
join accounts a 
on t.account_id = a.account_id;

--6.Write a SQL query to Get a list of customers along with their account details.
select c.*, a.account_id, a.account_type, a.balance 
from customers c 
join accounts a on c.customer_id = a.customer_id;

---7.Write a SQL query to Retrieve transaction details along with customer information for a specific account
select t.*, c.first_name, c.last_name, c.email 
from transactions t 
join accounts a on t.account_id = a.account_id 
join customers c on a.customer_id = c.customer_id 
where t.account_id = 1001;

---8.Write a SQL query to Identify customers who have more than one account.
select customer_id, count(*) as account_count 
from accounts group by 
customer_id having count(*) > 1;

-----9.Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawals.
select sum(case when transaction_type = 'deposit' then amount else 0 end) as total_deposits,
sum(case when transaction_type = 'withdrawal' then amount else 0 end) as total_withdrawals,
sum(case when transaction_type = 'deposit' then amount else 0 end) -
sum(case when transaction_type = 'withdrawal' then amount else 0 end)
as difference from transactions;

-----10.Write a SQL query to Calculate the average daily balance for each account over a specified period.
select account_id, avg(balance) as avg_daily_balance 
from (select a.account_id, a.balance, t.transaction_date
from accounts a
join transactions t on a.account_id = t.account_id 
where t.transaction_date
between '2025-04-01' and '2025-04-07')
as sub group by account_id;

---11.Calculate the total balance for each account type
select account_type, 
sum(balance) as total_balance 
from accounts
group by account_type;

-----12.Identify accounts with the highest number of transactions order by descending order.
select account_id, 
count(*) as transaction_count 
from transactions
group by account_id 
order by transaction_count desc;

---13.List customers with high aggregate account balances, along with their account types
select c.customer_id, c.first_name, 
c.last_name, a.account_type, 
sum(a.balance) as total_balance
from customers c 
join accounts a on c.customer_id = a.customer_id
group by c.customer_id, c.first_name, 
c.last_name, a.account_type
having sum(a.balance) > 10000;

---14.Identify and list duplicate transactions based on transaction amount, date, and account.
select amount, transaction_date, 
account_id, count(*) as dup_count 
from transactions
group by amount, transaction_date, 
account_id having count(*) > 1;

                                                 ----------TASK4--------------


---1.Retrieve the customer(s) with the highest account balance.
select c.* from customers c 
join accounts a on c.customer_id = a.customer_id 
where a.balance = (select max(balance) 
from accounts);

----2.Calculate the average account balance for customers who have more than one account
select avg(balance) 
as avg_balance 
from accounts 
where customer_id in (select customer_id 
from accounts 
group by customer_id
having count(account_id) > 1);

-----3.Retrieve accounts with transactions whose amounts exceed the average transaction amount
select distinct account_id
from transactions 
where amount > (select avg(amount)
from transactions);

------4.Identify customers who have no recorded transactions
select c.* from customers c 
where c.customer_id 
not in (select distinct a.customer_id 
from accounts a 
join transactions t
on a.account_id = t.account_id);

---5.Calculate the total balance of accounts with no recorded transactions
select sum(balance) as total_balance
from accounts 
where account_id not in 
(select distinct account_id from transactions);
-----6.Retrieve transactions for accounts with the lowest balance.
select *from transactions 
where account_id in (select account_id 
from accounts
where balance = (select min(balance) 
from accounts));

-----7.Identify customers who have accounts of multiple types.
select customer_id 
from accounts 
group by customer_id
having count(distinct account_type) > 1;

-----8.Calculate the percentage of each account type out of the total number of accounts.
select account_type,
count(*) * 100.0 / 
(select count(*) from accounts) as percentage 
from accounts 
group by account_type;

---9.Retrieve all transactions for a customer with a given customer_id
select t.*from transactions t 
join accounts a on t.account_id = a.account_id 
where a.customer_id = 1;

------10.Calculate the total balance for each account type, including a subquery within the SELECT clause
select distinct account_type, 
(select sum(balance) 
from accounts a2 
where a2.account_type = a1.account_type) 
as total_balance 
from accounts a1;










