USE family_expenses_db;

-- Add family expenses categories
INSERT INTO `expense_category` (category_name)
    VALUES ('Home');

INSERT INTO `expense_category` (category_name)
    VALUES ('Kids');

INSERT INTO `expense_category` (category_name)
    VALUES ('Personal');

INSERT INTO `expense_category` (category_name)
    VALUES ('Bill');

INSERT INTO `expense_category` (category_name)
    VALUES ('Car');

INSERT INTO `expense_category` (category_name)
    VALUES ('Food');

INSERT INTO `expense_category` (category_name)
    VALUES ('Coffee');

-- Add family expenses
INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (1, 2000.00, '2026-11-09');

INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (2, 1200.00, '2026-11-09');

INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (3, 1000.00, '2026-11-09');

INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (1, 1000.00, '2026-11-09');

INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (4, 400.00, '2026-11-16');

INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (5, 400.00, '2026-11-16');

INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (6, 1000.00, '2026-11-16');

INSERT INTO `family_expenses` (category_id, expense_amount, expense_date)
    VALUES (7, 200.00, '2026-11-16');
