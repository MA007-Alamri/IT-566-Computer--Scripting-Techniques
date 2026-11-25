-- create the family expenses database
CREATE DATABASE IF NOT EXISTS family_expenses_db;

USE family_expenses_db;

-- Define the family_expenses table
CREATE TABLE family_expenses (
   expense_id INTEGER NOT NULL,
   category_id INTEGER NOT NULL,
   expense_amount DECIMAL(10, 2) NOT NULL,
   expense_date DATE NOT NULL
);

-- Set expense_id as the primary key
ALTER TABLE family_expenses
    ADD PRIMARY KEY (expense_id);

-- Assign a unique ID to each new expense
ALTER TABLE family_expenses
    MODIFY expense_id INTEGER NOT NULL AUTO_INCREMENT;

-- Define the category table
CREATE TABLE expense_category (
    category_id INTEGER NOT NULL,
    category_name VARCHAR(50) NOT NULL
    );

-- Set category_id as the primary key
ALTER TABLE expense_category
    ADD PRIMARY KEY (category_id);

-- Automatically generate category ID
ALTER TABLE expense_category
    MODIFY category_id INTEGER NOT NULL AUTO_INCREMENT;

-- connect the family_expenses table to the expense_category table
ALTER TABLE family_expenses
    ADD CONSTRAINT fk_category
    FOREIGN KEY (category_id) REFERENCES expense_category(category_id)
    ON UPDATE CASCADE;