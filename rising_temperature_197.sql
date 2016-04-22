select
w2.Id
from Weather w1, Weather w2
where w1.Temperature < w2.Temperature
and datediff(w2.Date, w1.Date) = 1
