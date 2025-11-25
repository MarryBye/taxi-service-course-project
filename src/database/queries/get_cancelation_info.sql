SELECT
    cro.id,
    cro.order_id,
    cro.canceled_by,
    cro.comment
FROM Canceled_rideorder cro
WHERE cro.order_id = ?;