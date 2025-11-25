CREATE OR REPLACE FUNCTION insert_car(
    arg_driver_id BIGINT,
    arg_mark VARCHAR(32),
    arg_model VARCHAR(32),
    arg_car_number VARCHAR(32),
    arg_class VARCHAR(32),
    arg_status VARCHAR(32)
) RETURNS cars_view AS $$
DECLARE
    var_class_id BIGINT;
    var_status_id BIGINT;
    new_car_id BIGINT;
    result cars_view%ROWTYPE;
BEGIN
    var_class_id := (SELECT id FROM car_classes WHERE name = arg_class);
    var_status_id := (SELECT id FROM car_statuses WHERE name = arg_status);

    IF (var_class_id IS NULL) OR (var_status_id IS NULL) THEN
        RAISE EXCEPTION 'No status or class to insert!';
    END IF;

    INSERT INTO cars (driver_id, mark, model, car_number, class_id, status_id)
    VALUES (arg_driver_id, arg_mark, arg_model, arg_car_number, var_class_id, var_status_id)
    RETURNING id INTO new_car_id;

    SELECT * INTO result FROM cars_view WHERE id = new_car_id;

    RETURN result;
END;
$$ LANGUAGE plpgsql;