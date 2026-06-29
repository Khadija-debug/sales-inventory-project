SELECT DISTINCT
    CAST(order_purchase_timestamp AS DATE) AS order_date,
    YEAR(order_purchase_timestamp) AS year,
    MONTH(order_purchase_timestamp) AS month_number,
    DATENAME(MONTH, order_purchase_timestamp) AS month_name,
    DATEPART(QUARTER, order_purchase_timestamp) AS quarter,
    DAY(order_purchase_timestamp) AS day,
    DATENAME(WEEKDAY, order_purchase_timestamp) AS weekday_name
INTO dim_date
FROM orders
WHERE order_purchase_timestamp IS NOT NULL;