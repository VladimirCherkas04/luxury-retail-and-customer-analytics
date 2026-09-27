WITH customer_sales AS (
    SELECT
        c.customer_id,
        c.customer_segment,
        c.loyalty_level,
        COUNT(DISTINCT o.order_id) AS orders,
        ROUND(SUM(o.order_value), 2) AS revenue,
        ROUND(AVG(o.order_value), 2) AS average_order_value
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY
        c.customer_id,
        c.customer_segment,
        c.loyalty_level
)

SELECT
    customer_id,
    customer_segment,
    loyalty_level,
    orders,
    revenue,
    average_order_value,
    RANK() OVER (
        ORDER BY revenue DESC
    ) AS revenue_rank
FROM customer_sales
ORDER BY revenue_rank
LIMIT 20;