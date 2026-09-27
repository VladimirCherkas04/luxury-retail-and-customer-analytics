SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT o.customer_id) AS active_customers,
    SUM(o.order_value) AS total_revenue,
    ROUND(AVG(o.order_value), 2) AS average_order_value,
    ROUND(AVG(o.satisfaction_score), 2) AS average_satisfaction,
    COUNT(DISTINCT o.product_id) AS products_sold,
    COUNT(DISTINCT o.region_id) AS regions_active
FROM orders o;