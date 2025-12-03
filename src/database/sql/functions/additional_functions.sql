CREATE OR REPLACE FUNCTION is_car_on_maintenance(par_car_id BIGINT) RETURNS boolean AS $$
DECLARE
    is_car_on_maintenance boolean;
BEGIN
    is_car_on_maintenance := EXISTS (
        SELECT 1
        FROM maintenances AS m
        WHERE m.car_id = par_car_id AND (m.maintenance_status = 'diagnosis' OR m.maintenance_status = 'in_progress')
    );
	RETURN is_car_on_maintenance;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION is_car_has_driver(par_car_id BIGINT) RETURNS boolean AS $$
DECLARE
    is_car_has_driver boolean;
BEGIN
    is_car_has_driver := EXISTS (
        SELECT 1
        FROM cars AS c
        WHERE c.id = par_car_id AND c.driver_id IS NOT NULL
    );
	RETURN is_car_has_driver;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_balance_last_update(par_user_id BIGINT, par_balance_type balance_types) RETURNS timestamp AS $$
DECLARE
    last_update TIMESTAMP;
BEGIN
    last_update := (
        SELECT updated_at
        FROM balances
        WHERE user_id = par_user_id
        AND balance_type = par_balance_type
    );
	RETURN last_update;
END;
$$ LANGUAGE plpgsql;