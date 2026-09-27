SELECT
    c.customer_segment,
    c.loyalty_level,
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(SUM(o.order_value), 2) AS revenue,
    ROUND(
        SUM(o.order_value) / COUNT(DISTINCT c.customer_id),
        2
    ) AS revenue_per_customer,
    ROUND(AVG(o.order_value), 2) AS average_order_value
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_segment,
    c.loyalty_level
ORDER BY
    revenue DESC;