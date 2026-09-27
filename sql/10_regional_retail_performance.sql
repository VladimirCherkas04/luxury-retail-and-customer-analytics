WITH regional_sales AS (
    SELECT
        r.country,
        r.subregion,
        r.market,
        COUNT(DISTINCT o.order_id) AS orders,
        COUNT(DISTINCT o.customer_id) AS customers,
        ROUND(SUM(o.order_value), 2) AS revenue,
        ROUND(AVG(o.order_value), 2) AS average_order_value
    FROM regions r
    JOIN orders o
        ON r.region_id = o.region_id
    GROUP BY
        r.country,
        r.subregion,
        r.market
)

SELECT
    country,
    subregion,
    market,
    orders,
    customers,
    revenue,
    average_order_value,
    RANK() OVER (
        ORDER BY revenue DESC
    ) AS revenue_rank
FROM regional_sales
ORDER BY revenue_rank;