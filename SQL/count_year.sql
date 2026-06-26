SELECT
    YEAR(order_purchase_timestamp) AS OrderYear,
    COUNT(*) AS TotalOrders
FROM vw_sales_dashboard
GROUP BY YEAR(order_purchase_timestamp)
ORDER BY OrderYear;