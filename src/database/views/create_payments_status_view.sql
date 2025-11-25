CREATE OR REPLACE VIEW payments_history_view AS
SELECT
    p.id AS payment_id,
    ps.name AS historical_status,
    psh.changed_at AS status_changed_at
FROM payments as p
JOIN payment_status_history psh ON psh.payment_id = p.id
JOIN payment_statuses ps ON ps.id = psh.status_id;