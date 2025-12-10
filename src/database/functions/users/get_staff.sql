CREATE OR REPLACE FUNCTION get_staff(
    par_filter_id BIGINT
) RETURNS SETOF users_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM users_view
        WHERE
            id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

