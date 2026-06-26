CREATE VIEW vw_product_sales AS
SELECT 
    oi.product_id,
    p.product_category_name,
    COUNT(*) AS total_sold,
    SUM(oi.price) AS total_revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY 
    oi.product_id,
    p.product_category_name;