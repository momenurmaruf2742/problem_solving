SELECT s.user_id,
       IFNULL(ROUND(sum(c.action = 'confirmed') / COUNT(c.action), 2),0.00) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id order by confirmation_rate asc