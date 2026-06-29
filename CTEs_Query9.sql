WITH CustomerRevenue AS
(
    SELECT
        customer_id,
        SUM(total_value) AS total_revenue
    FROM fact_sales
    GROUP BY customer_id
)

SELECT TOP 10
    customer_id,
    total_revenue
FROM CustomerRevenue
ORDER BY total_revenue DESC;