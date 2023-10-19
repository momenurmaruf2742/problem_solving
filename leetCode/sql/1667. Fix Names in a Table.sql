SELECT user_id,
CONCAT(UPPER(LEFT(name,1)),
LOWER(RIGHT(name,LENGTH(name)-1)))
AS name FROM Users  
ORDER BY user_id ASC;

-- Create table If Not Exists Users (user_id int, name varchar(40))
-- Truncate table Users
-- insert into Users (user_id, name) values ('1', 'aLice')
-- insert into Users (user_id, name) values ('2', 'bOB')