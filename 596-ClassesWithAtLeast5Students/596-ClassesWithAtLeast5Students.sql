-- Last updated: 7/17/2026, 9:35:24 AM
select Class
from Courses group by Class having count(student)>=5;