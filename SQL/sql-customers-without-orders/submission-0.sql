-- Write your query below

WITH cte1 AS
(
    SELECT customers.id, customers.name, orders.customer_id
    FROM customers
    LEFT JOIN orders
    ON customers.id = orders.customer_id
)
SELECT name
FROM cte1
WHERE customer_id IS NULL



