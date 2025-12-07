-- Active: 1764877667177@@127.0.0.1@5432@taxi_db@public
CREATE OR REPLACE PROCEDURE delete_order(
    par_id BIGINT
) AS $$
BEGIN
    DELETE FROM orders WHERE id = par_id;
END;
$$ LANGUAGE plpgsql;