CREATE OR REPLACE FUNCTION list_cars(
    arg_start_number INT DEFAULT 1,
    arg_limit_number INT DEFAULT 100
) RETURNS SETOF cars_view AS $$
BEGIN
    RETURN QUERY
        SELECT id, car_number, driver_id, car_class, car_status, mark, model
        FROM (
            SELECT *,
                   ROW_NUMBER() OVER (ORDER BY id) AS rn
            FROM cars_view AS cv
        ) t
        WHERE rn BETWEEN arg_start_number AND arg_start_number + arg_limit_number - 1;
END;
$$ LANGUAGE plpgsql;