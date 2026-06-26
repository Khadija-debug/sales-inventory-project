
SELECT COUNT (*) AS missing_products
FROM products
WHERE product_category_ name IS NULL;