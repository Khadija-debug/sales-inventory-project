SELECT 
customer_id,
COUNT(order_id) AS total_orders,
SUM(total_value) AS total_spent
FROM fact_sales
GROUP BY customer_id
ORDER BY total_spent DESC;