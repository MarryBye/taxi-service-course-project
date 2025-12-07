-- Active: 1764877667177@@127.0.0.1@5432@taxi_db@public
CREATE OR REPLACE FUNCTION create_order(
    par_client_id BIGINT
) RETURNS SETOF orders_view AS $$
DECLARE
    created_order_id BIGINT;
BEGIN
    INSERT INTO orders (
        client_id
    )
    VALUES (
        par_client_id
    )
    RETURNING id INTO created_order_id;
    RETURN QUERY 
    SELECT * FROM orders_view WHERE order_id = created_order_id;
END;
$$ LANGUAGE plpgsql;