select
s2.Score,
(select count(distinct s1.score) + 1 as counts
from Scores s1
where s1.score > s2.score
) as Rank
from Scores s2
order by 2
;


select sc.Score,
       (Select count(*)+1 from (select distinct (Score) from Scores)
        as uniqeScores where Score > sc.Score) as rank 
from Scores sc order by sc.Score desc;
