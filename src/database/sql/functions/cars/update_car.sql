CREATE OR REPLACE FUNCTION update_car(
    par_id BIGINT,
    par_mark VARCHAR(32),
    par_model VARCHAR(32),
    par_car_number VARCHAR(32),
    par_class car_classes,
    par_status car_statuses,
    par_driver_id BIGINT
)
RETURNS SETOF cars_view AS $$
BEGIN
    UPDATE cars
    SET
        mark = COALESCE(par_mark, mark),
        model = COALESCE(par_model, model),
        car_number = COALESCE(par_car_number, car_number),
        class = COALESCE(par_class, car_class),
        status = COALESCE(par_status, car_status),
        driver_id = COALESCE(par_driver_id, driver_id)
    WHERE id = par_id;
    RETURN QUERY SELECT * FROM cars_view WHERE id = par_id;
END;
$$ LANGUAGE plpgsql;
