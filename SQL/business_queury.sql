SELECT 
    oi.product_id,
    COUNT(*) AS total_sold,
    SUM(oi.price) AS total_revenue
FROM order_items oi
GROUP BY oi.product_id
ORDER BY total_sold DESC;