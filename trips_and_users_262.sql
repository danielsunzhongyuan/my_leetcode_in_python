# Write your MySQL query statement below
select t.Request_at as "Day", 
-- round(sum(case when t.Status = "cancelled_by_client" or t.Status = "cancelled_by_driver" then 1 else 0 end)/count(1), 2) as "Cancellation Rate"
round(sum(if (t.Status in ("cancelled_by_client", "cancelled_by_driver"), 1, 0))/count(1), 2) as "Cancellation Rate"
# truncate 不行，没有四舍五入了
# format 不行, 返回的是字符串而不是数字了

from Trips t
join Users u on t.Client_Id = u.Users_Id and u.Role = "client" and u.Banned = "No"
where t.Request_at between "2013-10-01" and "2013-10-03"
group by t.Request_at
order by t.Request_at
