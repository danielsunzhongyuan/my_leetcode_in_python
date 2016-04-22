select d.Name as Department, e.Name as Employee, e.Salary
from Employee e
join Department d on e.DepartmentId = d.id
join 
(select e.DepartmentId, max(e.salary) as Salary
from Employee e
group by e.DepartmentId
) a on e.Salary = a.Salary and e.DepartmentId = a.DepartmentId
