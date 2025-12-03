CREATE OR REPLACE VIEW show_driver_popular_tag AS
SELECT oct.tag
FROM order_client_tags AS oct
JOIN orders AS o ON oct.order_id = o.id
GROUP BY oct.tag
ORDER BY COUNT(*) DESC
LIMIT 1