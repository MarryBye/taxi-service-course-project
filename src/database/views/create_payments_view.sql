CREATE OR REPLACE VIEW payments_view AS
SELECT
    p.id,
    p.price,
    ps.name AS status,
    pm.name AS method,
    p.order_id
FROM payments p
JOIN payment_statuses ps ON p.status_id = ps.id
JOIN payment_methods pm ON p.method_id = pm.id