-- create table
CREATE TABLE IF NOT EXISTS second_table (id, int,
name VARCHAR(256),
score INT);

INSERT INTO second_table(id, name, score) VALUE (1, 'John', 10)
INSERT INTO second_table(id, name, score) VALUE (2, 'Alex', 3)
INSERT INTO second_table(id, name, score) VALUE (1, 'Bob', 14)
INSERT INTO second_table(id, name, score) VALUE (1, 'George', 18)
