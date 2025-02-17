-- Active: 1739809230443@@127.0.0.1@5432@FastAPI@public
-- Basic sql command
-- 1. Selecting all rows
SELECT * from public."Products";

-- 2. Filtering rows based on a condition (price > 100)
SELECT * from public."Products" WHERE price > 100;

-- 3. Sorting rows in ascending order (price)
SELECT * from public."Products" ORDER BY price ASC;

-- 4. Limiting the number of rows to 10
SELECT * from public."Products" ORDER BY price ASC LIMIT 10;

-- 5. Selecting a specific column (product_name)
SELECT name from public."Products";

-- 6. Selecting multiple columns (product_name, price)
SELECT name, price from public."Products";

-- 7. Selecting distinct values from a column (distinct product_name)
SELECT DISTINCT name from public."Products";

-- Filtering: Using logical Operators (AND, OR, NOT), (Null, IS NOT NULL), (Between, NOT BETWEEN)

-- 8. Filtering rows where price > 100 AND product_name starts with 'A'

SELECT * from public."Products" WHERE price > 100 AND name LIKE 'T%';

-- Filter rows where the name ends with 'r'

SELECT * from public."Products" WHERE name LIKE '%r';

-- Filter rows where price is between 50 and 150

SELECT * from public."Products" WHERE price BETWEEN 50 AND 150;

-- Aggregate functions: COUNT, SUM, AVG, MAX, MIN

-- 9. Counting the number of products

SELECT COUNT(*) FROM public."Products";

-- 10. Calculating the total price of all products

SELECT SUM(price) FROM public."Products";

-- 11. Finding the average price of products

SELECT AVG(price) FROM public."Products";

-- Not Operator: find all product where inventory is not 0

SELECT * FROM public."Products" WHERE inventory NOT IN (0);
SELECT * FROM public."Products" WHERE inventory <> 0;

-- AND / OR
-- Find all product wgere inventory greater than 0 and price less than 100

SELECT * FROM public."Products" WHERE inventory > 0 AND price < 100;

-- Find all product where inventory greater than 0 or price less than 100
select * from public."Products" WHERE inventory > 0 OR price < 100;

-- IN/ NOT IN Operator

-- Find all product where inventory is 0 or 2

SELECT * FROM public."Products" WHERE inventory IN (0, 2);

-- Find all product where inventory is not 0 or 2

SELECT * FROM public."Products" WHERE inventory NOT IN (0, 2);


