SELECT
    sell_date,
    COUNT(*) AS num_sold,
    GROUP_CONCAT(product order by product asc ) AS products
FROM (SELECT DISTINCT sell_date, product
    FROM Activities) as Activities
GROUP BY sell_date
ORDER BY sell_date;