CREATE OR REPLACE FUNCTION get_driver(
    par_filter_id BIGINT
) RETURNS SETOF drivers_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM drivers_view
        WHERE
            id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

