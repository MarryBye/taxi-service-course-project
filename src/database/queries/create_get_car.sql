CREATE OR REPLACE FUNCTION get_car(
    arg_car_id BIGINT
) RETURNS SETOF cars_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM cars_view WHERE id = arg_car_id;
END;
$$ LANGUAGE plpgsql;