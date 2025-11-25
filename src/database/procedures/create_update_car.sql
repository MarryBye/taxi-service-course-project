CREATE OR REPLACE FUNCTION update_car(
    arg_car_id BIGINT,
    arg_new_driver_id BIGINT DEFAULT NULL,
    arg_new_mark VARCHAR(32) DEFAULT NULL,
    arg_new_model VARCHAR(32) DEFAULT NULL,
    arg_new_car_number VARCHAR(32) DEFAULT NULL,
    arg_new_class VARCHAR(32) DEFAULT NULL,
    arg_new_status VARCHAR(32) DEFAULT NULL
) RETURNS cars_view AS $$
DECLARE
    updated_car cars_view%ROWTYPE;

    var_class_id BIGINT;
    var_status_id BIGINT;
BEGIN
    SELECT * INTO updated_car FROM cars_view WHERE id = arg_car_id;

    IF (updated_car IS NULL) THEN
        RAISE EXCEPTION 'Car with this id does not exist';
    END IF;

    IF (arg_new_class IS NOT NULL) THEN
        SELECT id INTO var_class_id FROM car_classes WHERE name = arg_new_class;
        IF (var_class_id IS NULL) THEN
            RAISE EXCEPTION 'Invalid car class!';
        END IF;
    END IF;

    IF (arg_new_status IS NOT NULL) THEN
        SELECT id INTO var_status_id FROM car_statuses WHERE name = arg_new_status;
        IF (var_status_id IS NULL) THEN
            RAISE EXCEPTION 'Invalid car status!';
        END IF;
    END IF;

    UPDATE cars
    SET
        driver_id = arg_new_driver_id,
        mark = COALESCE(arg_new_mark, updated_car.mark),
        model = COALESCE(arg_new_model, updated_car.model),
        car_number = COALESCE(arg_new_car_number, updated_car.car_number),
        class_id = COALESCE(var_class_id, (SELECT c.class_id FROM cars AS c WHERE c.id = arg_car_id)),
        status_id = COALESCE(var_status_id, (SELECT c.status_id FROM cars AS c WHERE c.id = arg_car_id))
    WHERE id = arg_car_id;

    SELECT * INTO updated_car FROM cars_view WHERE id = arg_car_id;

    RETURN updated_car;
END;
$$ LANGUAGE plpgsql;