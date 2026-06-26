SELECT order_id,
COUNT(*) AS duplicate_count 
FROM orders 
GROUP BY order_id HAVING COUNT (*) > 1;
