select id, 
coalesce(case when id%2=0 then lag(student) over() else lead(student) over() end, student) as student
from seat