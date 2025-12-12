CREATE OR REPLACE PROCEDURE driver_schema.accept_order(
    p_order_id BIGINT,
    p_driver_id BIGINT
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    UPDATE orders
    SET driver_id = p_driver_id,
        status = 'waiting_for_driver'
    WHERE id = p_order_id;
END;
$$;