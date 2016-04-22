select
t.request_at as "Day",
round(sum(if(t.Status in ("cancelled_by_client", "cancelled_by_driver"), 1, 0))/count(1), 2) as "Cancellation Rate"

from Trips t
join Users u on t.client_id = u.users_id
where u.banned = "No" and u.Role = "client"
and t.request_at >= "2013-10-01" and t.request_at <= "2013-10-03"
group by t.request_at
order by t.request_at
