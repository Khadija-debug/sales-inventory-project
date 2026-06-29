SELECT DISTINCT
    customer_zip_code_prefix,
    customer_city,
    customer_state
INTO dim_region
FROM customers;