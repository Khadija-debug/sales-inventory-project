SELECT 
    o.order_id,
    o.customer_id,
    o.order_status,
    oi.product_id,
    oi.price,
    oi.freight_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id;