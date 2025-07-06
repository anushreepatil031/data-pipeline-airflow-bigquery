Basic total sales query : 
SELECT city, SUM(total_amount) AS total_sales
FROM ecommerce_data.sales
GROUP BY city
ORDER BY total_sales DESC;


Query to get sales per city and product: 

SELECT city, product, SUM(total_amount) AS total_sales, COUNT(*) AS total_orders
FROM ecommerce_data.sales
GROUP BY city, product
ORDER BY total_sales DESC;



Query for partitioned table filtering (e.g., by order_date): 
SELECT *
FROM ecommerce_data.sales_partitioned
WHERE order_date BETWEEN '2023-01-01' AND '2023-01-15';



Example view creation (summary view): 
CREATE OR REPLACE VIEW ecommerce_data.sales_summary AS
SELECT city, 
       SUM(total_amount) AS total_sales, 
       AVG(total_amount) AS avg_order_value,
       COUNT(order_id) AS total_orders
FROM ecommerce_data.sales
GROUP BY city;



Query to read from the view: 

SELECT *
FROM ecommerce_data.sales_summary
ORDER BY total_sales DESC;






