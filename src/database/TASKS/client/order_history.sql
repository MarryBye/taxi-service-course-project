CREATE OR REPLACE FUNCTION order_history(
    p_client_id BIGINT
) RETURNS SETOF orders_view AS $$
BEGIN
    RETURN QUERY SELECT * FROM orders_view WHERE client_id = p_client_id;
END;
$$ LANGUAGE plpgsql;