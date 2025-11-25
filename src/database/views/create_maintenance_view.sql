CREATE OR REPLACE VIEW maintenances_view AS
SELECT
    m.id,
    m.comment,
    ms.name AS status,
    c.id AS car_id,
    m.maintenance_start,
    m.maintenance_end
FROM maintenances m
JOIN maintenance_statuses ms ON m.status_id = ms.id
JOIN cars c ON m.car_id = c.id
LEFT JOIN mechanics me ON m.mechanic_id = me.user_id