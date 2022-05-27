WITH t1 AS (
    SELECT product_id, new_price, change_date, MAX(change_date) OVER (PARTITION BY product_id) AS latest
    FROM Products
    WHERE change_date <= '2019-08-16'
),
t2 AS (
    SELECT t1.product_id, new_price
    FROM t1
    RIGHT OUTER JOIN (SELECT DISTINCT product_id FROM Products) AS p
    ON t1.product_id = p.product_id
    WHERE change_date = latest
)
SELECT p.product_id, COALESCE(new_price,10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS p
LEFT OUTER JOIN t2
ON p.product_id = t2.product_id
ORDER BY product_id;
