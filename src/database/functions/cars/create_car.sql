CREATE OR REPLACE FUNCTION create_car(
    par_mark VARCHAR(32),
    par_model VARCHAR(32),
    par_car_number VARCHAR(32),
    par_class car_classes,
    par_status car_statuses,
    par_driver_id BIGINT DEFAULT NULL
)
RETURNS SETOF cars_view AS $$
DECLARE
    created_car_id BIGINT;
BEGIN
    INSERT INTO cars (
        driver_id,
        mark,
        model,
        car_number,
        class,
        status
    )
    VALUES (
        par_driver_id,
        par_mark,
        par_model,
        par_car_number,
        par_class,
        par_status
    )
    RETURNING id INTO created_car_id;
    RETURN QUERY 
    SELECT * FROM cars_view WHERE id = created_car_id;
END;
$$ LANGUAGE plpgsql;