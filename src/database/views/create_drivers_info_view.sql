CREATE VIEW drivers_view AS
SELECT
    d.user_id AS driver_id,
    u.first_name,
    u.last_name,
    u.tel_number,
    c.id AS car_id,
    AVG(orh.driver_mark) AS avg_rating,
    COUNT(o.id) AS rides_count,
    AVG(o.price) AS average_ride_price
FROM drivers d
JOIN users u ON d.user_id = u.id
LEFT JOIN cars_driver_history cdh ON d.user_id = cdh.driver_id
LEFT JOIN cars c ON cdh.car_id = c.id
LEFT JOIN car_classes cc ON c.class_id = cc.id
LEFT JOIN car_statuses cs ON c.status_id = cs.id
LEFT JOIN orders o ON o.driver_id = d.user_id
LEFT JOIN orders_rating orh ON orh.order_id = o.id
GROUP BY d.user_id, u.first_name, u.last_name, u.tel_number, c.id, c.car_number, cc.name, cs.name;