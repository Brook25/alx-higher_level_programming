-- creates a database hbtn_0d_usa and a table cities (in the database hbtn_0d_usa) on your MySQL server
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use a database
USE hbtn_0d_usa;
-- creates a table
CREATE TABLE IF NOT EXISTS cities (id INT PRIMARY KEY AUTO_INCREMENT,
state_id INT,
name VARCHAR(256) NOT NULL,
FOREIGN KEY(state_id) REFERENCES states(id));
