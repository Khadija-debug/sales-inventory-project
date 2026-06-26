SELECT 
    o.order_id,
    o.customer_id,
    SUM(oi.price + oi.freight_value) AS total_order_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY 
    o.order_id,
    o.customer_id
ORDER BY 
    total_order_value DESC;