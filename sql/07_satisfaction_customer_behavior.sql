SELECT
    o.satisfaction_score,
    COUNT(DISTINCT o.customer_id) AS customers,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(SUM(o.order_value), 2) AS revenue,
    ROUND(AVG(o.order_value), 2) AS average_order_value,
    COUNT(DISTINCT CASE
        WHEN o.repeat_customer = 'Yes'
        THEN o.customer_id
    END) AS repeat_customers
FROM orders o
GROUP BY o.satisfaction_score
ORDER BY o.satisfaction_score;