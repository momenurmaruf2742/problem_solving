select p.product_name ,sum(o.unit) as unit from Products p left join Orders o on p.product_id=o.product_id where o.order_date like '2020-02%' group by o.product_id having sum(o.unit) >= "100"