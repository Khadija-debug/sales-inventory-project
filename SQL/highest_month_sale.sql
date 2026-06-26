SELECT TOP 1
YEAR(order_purchase_timestamp)AS year,
MONTH (order_purchase_timestamp) AS month,
SUM(total_value) AS monthly_sales FROM fact_sales
GROUP BY 
YEAR(order_purchase_timestamp),
MONTH(order_purchase_timestamp)
ORDER BY 
monthly_sales DESC;