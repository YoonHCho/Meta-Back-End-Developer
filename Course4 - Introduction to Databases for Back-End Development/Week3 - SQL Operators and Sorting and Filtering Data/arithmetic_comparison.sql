SELECT 10 + 15;
SELECT 100 % 10;

SELECT * FROM employee WHERE salary + allowance = 25000;
SELECT * FROM employee WHERE salary - tax = 50000;
SELECT * FROM employee WHERE tax * 2 = 4000;
SELECT * FROM employee WHERE allowance / salary * 100 >= 5;
SELECT * FROM employee WHERE hours % 2 = 0;
SELECT salary + 500 FROM employee;
SELECT id, name, salary + 5000 AS updated_salary
FROM employees;

-- SQL Comparison operators
SELECT * FROM employee WHERE salary = 96000;
SELECT * FROM employee WHERE salary + allowance = 25000;
SELECT ID, name FROM employees WHERE salary + 5000 > 100000;

-- NOT equal != or <>
SELECT * FROM employee WHERE salary != 100000;
SELECT * FROM employee WHERE salary <> 100000;