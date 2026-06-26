CREATE VIEW vw_sales_dashboard AS SELECT 
fs.order_id,
fs.customer_id,
fs.product_id,
fs.seller_id,

dp.product_category_name,

fs.order_status,
fs.order_purchase_timestamp,

fs.price,
fs.freight_value
FROM fact_sales fs 
LEFT JOIN dim_product dp
ON fs.product_id = dp.product_id;
