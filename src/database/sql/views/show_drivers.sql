CREATE OR REPLACE VIEW show_drivers AS
SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.email,
    u.tel_number,
    u.created_at,
    c.id AS car_id,
    AVG(r.driver_mark) AS average_mark,
    COUNT(o.id) AS orders_count,
    AVG(rt.distance) AS average_distance,
    SUM(rt.distance) AS total_distance,
    (
        SELECT odt_in.tag
        FROM order_driver_tags AS odt_in
        JOIN orders AS o_in ON odt_in.order_id = o.id
        WHERE o_in.driver_id = u.id
        GROUP BY odt_in.tag
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ) AS most_popular_tag
FROM users AS u
JOIN cars AS c ON u.id = c.driver_id
JOIN orders AS o ON u.id = o.driver_id
JOIN order_ratings AS r ON o.id = r.order_id
JOIN routes AS rt ON rt.order_id = o.id
WHERE u.role = 'driver'
GROUP BY u.id, c.id, o.id;