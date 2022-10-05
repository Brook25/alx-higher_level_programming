-- creates table second_table in the database hbtn_0c_0 in my MySQL server and adds multiples rows
-- creates a new table
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
-- adds new rows to the table
INSERT INTO second_table VALUES (1, 'John', 10);
INSERT INTO second_table VALUES (2, 'Alex', 3);
INSERT INTO second_table VALUES (3, 'Bob', 14);
INSERT INTO second_table VALUES (4, 'George', 8);
