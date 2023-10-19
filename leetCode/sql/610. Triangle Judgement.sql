select  x,y,z,case when (x+y) > z and (x+z) > y and (y+z) > x then 'Yes' else 'No' end as triangle from Triangle

-- Create table If Not Exists Triangle (x int, y int, z int)
-- Truncate table Triangle
-- insert into Triangle (x, y, z) values ('13', '15', '30')
-- insert into Triangle (x, y, z) values ('10', '20', '15')