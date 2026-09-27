WITH product_sales AS (
    SELECT
        p.product_id,
        p.product_category,
        p.product_type,
        COUNT(DISTINCT o.order_id) AS orders,
        SUM(o.units) AS units_sold,
        ROUND(SUM(o.order_value), 2) AS revenue,
        ROUND(AVG(o.order_value), 2) AS average_order_value
    FROM products p
    JOIN orders o
        ON p.product_id = o.product_id
    GROUP BY
        p.product_id,
        p.product_category,
        p.product_type
)

SELECT
    product_id,
    product_category,
    product_type,
    orders,
    units_sold,
    revenue,
    average_order_value,
    RANK() OVER (
        ORDER BY revenue DESC
    ) AS revenue_rank
FROM product_sales
ORDER BY revenue_rank;