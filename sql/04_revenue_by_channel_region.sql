SELECT
    r.country,
    o.channel,
    COUNT(DISTINCT o.order_id) AS orders,
    COUNT(DISTINCT o.customer_id) AS customers,
    ROUND(SUM(o.order_value), 2) AS revenue,
    ROUND(AVG(o.order_value), 2) AS average_order_value
FROM orders o
JOIN regions r
    ON o.region_id = r.region_id
GROUP BY
    r.country,
    o.channel
HAVING COUNT(DISTINCT o.order_id) >= 20
ORDER BY
    revenue DESC;