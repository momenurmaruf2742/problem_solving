# Write your MySQL query statement below
WITH perDayAmount AS ( SELECT visited_on, sum(amount) AS amount
                FROM Customer
                GROUP BY visited_on)
SELECT  c2.visited_on AS visited_on, sum(c1.amount) AS amount, round((sum(c1.amount)/7),2) AS average_amount
FROM perDayAmount c1, perDayAmount c2
WHERE DATEDIFF(c2.visited_on, c1.visited_on) BETWEEN 0 and 6
GROUP BY c2.visited_on
HAVING c2.visited_on >= (SELECT MIN(visited_on) FROM Customer) + 6
ORDER BY c2.visited_on;
