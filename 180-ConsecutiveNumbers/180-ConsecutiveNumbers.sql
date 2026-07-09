-- Last updated: 7/9/2026, 3:07:48 PM
# Write your MySQL query statement below
select distinct num as ConsecutiveNums 
from Logs l2 where 3<=(
    select count(*) from Logs l1
    where l2.num=l1.num and
    (l1.id between l2.id and l2.id+2) 
    )