-- Active: 1739809230443@@127.0.0.1@5432@FastAPI@public

-- Creating Tables
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL
);

-- Inserting Sample Data
INSERT INTO users (username, email, password, date_of_birth) 
VALUES ('john_doe', 'john.doe@example.com', '$2b$12$y/KZOjX0tU0c9h2K3j9g', '1990-01-01'),
       ('samantha_jones','samantha.jones@example.com', '$2b$12$y/KZOjX0tU0c9h2K3', '1985-12-25');

INSERT INTO public."Products" (name, price) 
VALUES 
    ('School Bag', 10.99),
    ('Laptop', 1299.99),
    ('Monitor', 249.99);

SELECT * FROM public."Products";

INSERT INTO public."Products" (name, price) 
VALUES 
    ('Mathematical Set', 12.99),
    ('Mac Laptop', 1299),
    ('Desktop Monitor', 249)
RETURNING *; -- This will return the newly inserted rows


-- Updating

UPDATE public."users"
SET email = 'john.doe25@example.com'
WHERE username = 'john_doe';


-- Deleting

DELETE FROM public."users"
WHERE username = 'john_doe';

SELECT * FROM public."users";

-- Upsert
-- 
-- INSERT INTO table_name (column1, column2, column3)
-- VALUES (value1, value2, value3)
-- ON CONFLICT (unique_column)
-- DO UPDATE SET 
    -- column1 = EXCLUDED.column1,
    -- column2 = EXCLUDED.column2;

Alter table public."users" add column age INTEGER NULL;
INSERT INTO users (username, email, password, date_of_birth, age) 
VALUES ('john_doe', 'john.doe@example.com', 'johndoe_tyjghdf', '1998-01-31', 30)
ON CONFLICT (username)
DO UPDATE SET 
    email = EXCLUDED.email,
    age = EXCLUDED.age;

-- If john_doe does not exist, it will be inserted.
-- If john_doe already exists, only the email and age will be updated.

SELECT * FROM public."users";
