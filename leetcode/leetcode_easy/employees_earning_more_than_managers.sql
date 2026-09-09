# 181. Employees Earning More Than Their Managers
#  
# 
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.



SELECT e.name FROM employees e WHERE e.salary > (
  SELECT m.salary FROM employees m WHERE m.id = e.managerId
);


# OR

SELECT e.name as Employee
FROM Employee e
JOIN employee m
ON e.managerId = m.id
WHERE e.salary > m.salary
