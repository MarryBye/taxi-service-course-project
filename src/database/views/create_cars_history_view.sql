CREATE OR REPLACE VIEW cars_driver_history_view AS
SELECT
    c.id AS car_id,
    cd.driver_id AS historical_driver,
    cd.changed_at AS driver_changed_at
FROM cars c
JOIN cars_driver_history cd ON cd.car_id = c.id;

CREATE OR REPLACE VIEW cars_status_history_view AS
SELECT
    c.id AS car_id,
    cs2.name AS historical_status,
    cs.changed_at AS status_changed_at
FROM cars c
JOIN cars_status_history cs ON cs.car_id = c.id
JOIN car_statuses cs2 ON cs2.id = cs.status_id;