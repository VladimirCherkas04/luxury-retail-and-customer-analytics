SELECT
    c.loyalty_level,
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(DISTINCT CASE
        WHEN o.repeat_customer = 'Yes'
        THEN c.customer_id
    END) AS repeat_customers,
    ROUND(
        100.0 * COUNT(DISTINCT CASE
            WHEN o.repeat_customer = 'Yes'
            THEN c.customer_id
        END)
        / COUNT(DISTINCT c.customer_id),
        2
    ) AS repeat_customer_rate,
    ROUND(SUM(o.order_value), 2) AS revenue,
    ROUND(AVG(o.order_value), 2) AS average_order_value
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.loyalty_level
ORDER BY repeat_customer_rate DESC;