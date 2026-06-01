# What is PosgreSQL?&#x20;

- relational database with much more features than a traditional excel spreadsheet
- - can be much bigger
  - can have multipler users access it
  - strict rule enforcement
  - very fast accessing
  - safe and persistent

---

## Core Concepts:

1. Database: A folder that holds many tables
2. Table: A singular spreadsheet instance
3. Row: One record
4. Column: A field with a type (like age Integer)
5. Schema:&#x20;
6. Primary Key: Unique ID for a particular row
7. Foreign Key: A reference to another table

---

## Basic Usage in Locally:

Step 1: Initialization and accessing:

```bash
psql postgres # to open up the PostgreSQL shell

CREATE DATABASE test; # to create a database named test

\q # to exit out the postgresql shell with postgresql database open
# so that we can open the test database that we just created
```

```bash
psql test # to connect to the database you just created
```

Step 2: Basic Table Creation Syntax:

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY, --serial means auto incrementing. primary key is the unique identifier
  name TEXT NOT NULL,
  email TEXT UNIQUE,
  age INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  --TEXT, INT, TIMESTAMP, BOOLEAN, NUMERIC, DECIMAL, etc are datatypes
);
```

Step 3: Basic Insertion Syntax:

```sql
INSERT INTO users (name, email, age)
VALUES('Alice', 'alice.in@wonderland.com', 21);
```

Step 4: Reading Data:

```sql
SELECT * FROM users; -- select everything in the users table

SELECT name, age FROM users WHERE age > 20; -- reading but with certain conditions applied

ORDER BY name ASC; -- reads data in a particular order from ascending to descending
```

Step 5: Updating Syntax:

```sql
UPDATE users
SET age = 22
WHERE id = 1;

UPDATE users
SET email = 'alice.inwonderland@gmail.com'
WHERE name = 'Alice'
```

Step 6: Deleting Syntax:

```sql
DELETE FROM users WHERE id = 1;
DELETE FROM users WHERE name = 'Alice';
```

Step 7: User Management:

```sql
CREATE USER user_name WITH PASSWORD 'some_password';
GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;
```

Step 8 (Not something that we do lol): Deleting a Table:

```sql
DROP TABLE users;
```

---

## Defining Schemas / Models:
