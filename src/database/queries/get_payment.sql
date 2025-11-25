SELECT
    p.id,
    p.order_id,
    pm.name AS payment_method,
    ps.name AS payment_status,
    p.price
FROM Payment p
JOIN Payment_method pm ON p.payment_method_id = pm.id
JOIN Payment_status ps ON p.payment_status_id = ps.id;