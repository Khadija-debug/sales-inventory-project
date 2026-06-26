SELECT		
product_id,
product_category_name,
product_name_lenght,
product_description_lenght,
product_photos_qty
INTO dim_product
FROM vw_products_clean;