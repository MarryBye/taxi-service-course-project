CREATE OR REPLACE VIEW orders_cancels_view AS
SELECT
    oc.id AS cancel_id,
    oc.order_id,
    oc.canceled_by,
    oc.comment
FROM orders_cancels AS oc