select
f.Department,
f.Employee,
f.Salary
from (
select 
d.Name as Department, d.Id, e1.Name as Employee, e1.Salary,
(select count(distinct Salary) from Employee e2
where e1.Salary < e2.Salary and e1.DepartmentId = e2.DepartmentId
) as Rank
from Employee e1
join Department d on e1.DepartmentId = d.Id
order by d.Id asc, e1.Salary desc

) f
where f.Rank < 3
order by f.Id asc, f.Salary desc
