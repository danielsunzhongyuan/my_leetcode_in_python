select ifnull(
(SELECT distinct Salary as SecondHighestSalary FROM Employee order by Salary desc limit 1,1), null)
