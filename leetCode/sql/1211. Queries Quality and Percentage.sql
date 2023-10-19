# Write your MySQL query statement below
select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(sum(case when rating < 3 then 1 else 0 end) * 100 / count(*), 2) as poor_query_percentage
from
queries
group by
query_name;



-- Create table If Not Exists Queries (query_name varchar(30), result varchar(50), position int, rating int)
-- Truncate table Queries
-- insert into Queries (query_name, result, position, rating) values ('Dog', 'Golden Retriever', '1', '5')
-- insert into Queries (query_name, result, position, rating) values ('Dog', 'German Shepherd', '2', '5')
-- insert into Queries (query_name, result, position, rating) values ('Dog', 'Mule', '200', '1')
-- insert into Queries (query_name, result, position, rating) values ('Cat', 'Shirazi', '5', '2')
-- insert into Queries (query_name, result, position, rating) values ('Cat', 'Siamese', '3', '3')
-- insert into Queries (query_name, result, position, rating) values ('Cat', 'Sphynx', '7', '4')