CREATE OR REPLACE PROCEDURE delete_car (
    par_car_id BIGINT
)
AS $$
BEGIN
    DELETE FROM cars WHERE id = par_car_id;
END;
$$ LANGUAGE plpgsql;