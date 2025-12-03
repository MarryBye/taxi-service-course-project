CREATE OR REPLACE FUNCTION delete_car(
    arg_car_id BIGINT
) RETURNS cars_view AS $$
DECLARE
    deleted_car cars_view%ROWTYPE;
BEGIN
    SELECT * INTO deleted_car FROM cars_view WHERE id = arg_car_id;

    IF (deleted_car IS NULL) THEN
        RAISE EXCEPTION 'Car with this id does not exist';
    END IF;

    DELETE FROM cars WHERE id = arg_car_id;

    RETURN deleted_car;
END;
$$ LANGUAGE plpgsql;