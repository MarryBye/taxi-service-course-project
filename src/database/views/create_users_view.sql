CREATE OR REPLACE VIEW users_view AS
SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.rating,
    u.balance,
    u.tel_number,
    AVG(orr.client_mark) AS average_rating,
    ARRAY_AGG(r.name) AS roles
FROM users AS u
LEFT JOIN users_roles AS ur ON u.id = ur.user_id
LEFT JOIN roles AS r ON ur.role_id = r.id
LEFT JOIN orders AS o ON o.client_id = u.id
LEFT JOIN orders_rating AS orr ON orr.order_id = o.id
GROUP BY u.id