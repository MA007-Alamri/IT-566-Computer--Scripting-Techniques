-- create the family expenses database
CREATE DATABASE IF NOT EXISTS family_expenses_db;

USE family_expenses_db;

-- Define the family_expenses table
CREATE TABLE family_expenses (
   expense_id INTEGER NOT NULL,
   expense_category VARCHAR(50) NOT NULL,
   expense_amount DECIMAL(10, 2) NOT NULL,
   expense_date DATE NOT NULL
);

-- Set expense_id as the primary key
ALTER TABLE family_expenses
    ADD PRIMARY KEY (expense_id);

-- Assign a unique ID to each new expense
ALTER TABLE family_expenses
    MODIFY expense_id INTEGER NOT NULL AUTO_INCREMENT;

