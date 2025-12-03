CREATE OR REPLACE VIEW show_driver_popular_tag AS
SELECT odt.tag
FROM order_driver_tags AS odt
JOIN orders AS o ON odt.order_id = o.id
GROUP BY odt.tag
ORDER BY COUNT(*) DESC
LIMIT 1