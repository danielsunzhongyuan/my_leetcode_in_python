select
distinct l1.Num
from Logs l1, Logs l2, Logs l3
where l2.Id = l1.Id + 1
and l3.Id = l1.Id + 2
and l2.Num = l1.Num
and l3.Num = l1.Num
