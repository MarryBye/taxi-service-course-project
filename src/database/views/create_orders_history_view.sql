CREATE OR REPLACE VIEW orders_status_history_view AS
SELECT
    o.id AS order_id,
    os.name AS historical_order_status,
    osh.changed_at
FROM orders AS o
JOIN orders_status_history AS osh ON o.id = osh.order_id
JOIN order_statuses AS os ON os.id = osh.order_status_id;

CREATE OR REPLACE VIEW orders_driver_history_view AS
SELECT
    o.id AS order_id,
    odh.driver_id,
    odh.changed_at
FROM orders AS o
JOIN orders_driver_history AS odh ON o.id = odh.order_id;