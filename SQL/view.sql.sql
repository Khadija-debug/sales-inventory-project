CREATE VIEW vw_products_clean AS SELECT 
product_id ,
--Fix Null Category 
ISNULL (product_category_name ,
'Unknown Category') AS 
product_category_name,
product_name_lenght,
product_description_lenght,
product_photos_qty
FROM products;