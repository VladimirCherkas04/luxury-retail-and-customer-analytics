SELECT
    DATE_TRUNC('month', order_date)::date AS month,
    COUNT(*) AS orders,
    SUM(order_value) AS revenue,
    ROUND(AVG(order_value), 2) AS average_order_value
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;