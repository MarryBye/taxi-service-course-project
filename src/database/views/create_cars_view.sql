CREATE OR REPLACE VIEW cars_view AS
SELECT
    c.id,
    c.car_number,
    c.driver_id,
    cc.name AS car_class,
    cs.name AS car_status,
    c.mark,
    c.model
FROM cars AS c
JOIN car_classes AS cc ON c.class_id = cc.id
JOIN car_statuses AS cs ON c.status_id = cs.id
