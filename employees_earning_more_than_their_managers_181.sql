select
e.name as Employee
from Employee e, Employee m
where e.ManagerId = m.Id and e.Salary > m.Salary
;




select
e.name as Employee
from Employee e
join Employee m on e.ManagerId = m.Id and e.Salary > m.Salary
