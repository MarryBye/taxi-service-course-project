SELECT
    c.id,
    driver_id,
    mark,
    model,
    car_number,
    cc.name AS car_class,
    cs.name AS car_status
FROM Car c
JOIN Car_class cc ON c.car_class_id = cc.id
JOIN Car_status cs ON c.car_status_id = cs.id;