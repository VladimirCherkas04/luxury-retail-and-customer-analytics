SELECT
    p.product_category,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(o.units) AS units_sold,
    ROUND(SUM(o.order_value), 2) AS revenue,
    ROUND(AVG(o.order_value), 2) AS average_order_value
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.product_category
ORDER BY revenue DESC;