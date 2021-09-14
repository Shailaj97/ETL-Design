**Fact Table –**

fact\_table: employee\_id, department\_id, manager\_employee\_id,date\_id, salary,fte

**Dimension tables -** 

1. dim\_employee: employee\_id , manager\_employee\_id, first\_name, last\_name, employee\_role, dob, cost\_center, paycode , hours\_worked
1. dim\_manager: manager\_employee\_id, first\_name, last\_name
1. dim\_department: department\_id, department\_name, location,salary
1. dim\_date : date\_id,punch\_in\_time, punch\_out\_time, punch\_apply\_date, hire\_date, terminated\_date

Logical model for the above fact and dimension:


**Figure 1.0- Fact and dimension tables**



**Physical Model:**

`    `CREATE TABLE dim\_date(

`        `date\_id INT  NOT NULL PRIMARY KEY,

`        `punch\_in\_time TIMESTAMP,

`        `punch\_out\_time TIMESTAMP,

`        `punch\_apply\_date DATE,

`        `hire\_date DATE,

`        `terminated\_date DATE

`    `)

`    `CREATE TABLE dim\_department(

`        `department\_id INT NOT NULL PRIMARY KEY,

`        `department\_name VARCHAR(100),

`        `location TEXT,

`        `salary INT

`    `)

`    `CREATE TABLE dim\_department(

`        `department\_id INT NOT NULL PRIMARY KEY,

`        `department\_name VARCHAR(100),

`        `location TEXT,

`        `salary INT

`    `)

`    `CREATE TABLE dim\_manager(

`        `manager\_employee\_id INT NOT NULL PRIMARY KEY,

`        `first\_name,

`        `last\_name TEXT

`    `)

`    `CREATE TABLE dim\_employee(

`        `employee\_id INT NOT NULL PRIMARY KEY,

`        `manager\_employee\_id INT,

`        `first\_name TEXT,

`        `last\_name TEXT,

`        `employee\_role VARCHAR(100),

`        `dob DATE,

`        `cost\_centre INT,

`        `paycode VARCHAR(50),

`        `hours\_worked FLOAT

`    `)

`    `ALTER TABLE dim\_employee

`    `ADD FOREIGN KEY (manager\_employee\_id) REFERENCES dim\_manager(manager\_employee\_id);

`    `CREATE TABLE fact\_table(

`        `employee\_id INT NOT NULL,

`        `department\_id INT NOT NULL,

`        `manager\_employee\_id INT NOT NULL,

`        `date\_id INT NOT NULL,

`        `salary INT,

`        `fte FLOAT

`    `)

`    `ALTER TABLE fact\_table

`    `ADD FOREIGN KEY (employee\_id ) REFERENCES dim\_employee(employee\_id);

`    `ALTER TABLE fact\_table

`    `ADD FOREIGN KEY (department\_id ) REFERENCES dim\_department(department\_id);

`    `ALTER TABLE fact\_table

`    `ADD FOREIGN KEY (manager\_employee\_id ) REFERENCES dim\_manager(manager\_employee\_id);

`    `ALTER TABLE fact\_table

`    `ADD FOREIGN KEY (date\_id ) REFERENCES dim\_date(date\_id);







