-- To sort a column
SELECT col1, col2, col3
FROM table_name
ORDER BY col_name ASC; --> by default order is Ascending, so no need to address ASC.
			            DESC; --> for Descending order

-- To sort multiple columns
SELECT col1, col2 -- or replace with *
FROM table_name
ORDER BY col1_name ASC, col2_name DESC; -- can sort by each column.


SELECT id, firstName, lastName, nationality
FROM students_tbl
ORDER BY nationality;  -- ASC by default if not mentioned

-- WHERE CLAUSE
SELECT *
FROM students_tbl
WHERE faculty = 'Engineering';

SELECT *
FROM students_tbl
WHERE 	date_of_birth BETWEEN '2010-01-01' AND '2010-06-30';
-- OR * the % character is a wild card character that represents 0, 1, or multiple characters.
-- underscore _ can also be used to represent one single character
WHERE   faculty LIKE 'Sc%';
-- below will find and select the records with value 'USA' and 'UK', used to find multiple values in a column
WHERE   country IN ('USA', 'UK');