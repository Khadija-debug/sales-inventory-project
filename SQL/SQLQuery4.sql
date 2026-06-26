SELECT  COUNT(*) AS total_rows,
COUNT (product_id) AS product_id_not_null,
COUNT (product_category_name) AS category_not_null FROM products;