CREATE OR REPLACE FUNCTION list_drivers(
    par_filter_id BIGINT DEFAULT NULL,
    par_filter_email VARCHAR(128) DEFAULT NULL,
    par_filter_tel_number VARCHAR(32) DEFAULT NULL,
    par_filter_first_name VARCHAR(32) DEFAULT NULL,
    par_filter_last_name VARCHAR(32) DEFAULT NULL,
    par_filter_country country_names DEFAULT NULL,
    par_filter_city city_names DEFAULT NULL,
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF drivers_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM drivers_view
        WHERE
            (par_filter_id IS NULL OR id = par_filter_id) AND
            (par_filter_email IS NULL OR email = par_filter_email) AND
            (par_filter_tel_number IS NULL OR tel_number = par_filter_tel_number) AND
            (par_filter_first_name IS NULL OR first_name = par_filter_first_name) AND
            (par_filter_last_name IS NULL OR last_name = par_filter_last_name) AND
            (par_filter_country IS NULL OR country = par_filter_country) AND
            (par_filter_city IS NULL OR city = par_filter_city)
        LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

