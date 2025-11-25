CREATE OR REPLACE VIEW orders_view AS
SELECT
    o.id,
    o.price,
    o.client_id,
    o.driver_id,
    os.name AS status,
    orr.driver_mark,
    orr.client_mark,
    p.id AS payment_id,
    m.id AS marchrute_id,
    (SELECT mp.address FROM marchrute_points AS mp WHERE mp.marchrute_id = m.id ORDER BY mp.position ASC LIMIT 1) AS start_point,
    (SELECT mp.address FROM marchrute_points AS mp WHERE mp.marchrute_id = m.id ORDER BY mp.position DESC LIMIT 1) AS end_point
FROM orders as o
LEFT JOIN marchrutes AS m ON m.order_id = o.id
LEFT JOIN order_statuses AS os ON o.status_id = os.id
LEFT JOIN orders_rating AS orr ON o.id = orr.order_id
LEFT JOIN payments AS p ON o.id = p.order_id