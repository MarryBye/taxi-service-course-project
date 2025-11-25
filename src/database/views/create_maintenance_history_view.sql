-- Active: 1763469782117@@127.0.0.1@5432@taxi_db@public
CREATE OR REPLACE VIEW maintenance_history_view AS
SELECT
    m.id,
    m.car_id,
    m.mechanic_id,
    s.name AS historical_status,
    mh.changed_at
FROM maintenances m
LEFT JOIN maintenance_status_history mh ON mh.maintenance_id = m.id
LEFT JOIN maintenance_statuses s ON s.id = mh.status_id
ORDER BY m.id, mh.changed_at DESC;