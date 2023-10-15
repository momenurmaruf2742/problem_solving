SELECT E1.employee_id, E1.name, COUNT(E2.employee_id) reports_count,

ROUND(AVG(E2.age)) average_age FROM Employees E1 INNER JOIN Employees 

E2 ON E1.employee_id = E2.reports_to GROUP BY E1.employee_id, E1.name 

ORDER BY employee_id


-- Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int)
-- Truncate table Employees
-- insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', 'None', '43')
-- insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41')
-- insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36')
-- insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', 'None', '37')