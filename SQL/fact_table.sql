SELECT 
oi.order_id,
o.customer_id,
oi.product_id,
oi.seller_id,
o.order_status,
o.order_purchase_timestamp,

oi.price,
oi.freight_value,

(oi.price+oi.freight_value) AS total_value
INTO fact_sales 
FROM order_items oi
JOIN orders o
ON oi.order_id = o.order_id;