SELECT
    m.id,
    m.order_id,
    m.distance
FROM Marchrute m
WHERE m.id = ?;