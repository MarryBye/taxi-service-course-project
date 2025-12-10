CREATE OR REPLACE FUNCTION update_order(
    par_id BIGINT,
    par_driver_id BIGINT DEFAULT NULL,
    par_status order_statuses DEFAULT NULL,
    par_finished_at TIMESTAMP DEFAULT NULL
) RETURNS SETOF orders_view AS $$
DECLARE
    updated_order_id BIGINT;
BEGIN
    UPDATE orders
    SET 
        driver_id = COALESCE(par_driver_id, driver_id),
        status = COALESCE(par_status, status),
        finished_at = COALESCE(par_finished_at, finished_at)
    WHERE par_id = id
    RETURNING id INTO updated_order_id;
    RETURN QUERY 
    SELECT * FROM orders_view WHERE order_id = updated_order_id;
END;
$$ LANGUAGE plpgsql;