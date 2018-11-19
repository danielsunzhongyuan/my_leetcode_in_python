select Name
from Customers
where Id not in (
select distinct CustomerId
from Orders
)
;


select c.Name
from Customers c
left join Orders o on c.Id = o.CustomerId
where o.id is null
