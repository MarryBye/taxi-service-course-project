CREATE OR REPLACE FUNCTION create_user(
    par_login VARCHAR(32),
    par_email VARCHAR(128),
    par_tel_number VARCHAR(32),
    par_password_hash VARCHAR(512),
    par_first_name VARCHAR(32),
    par_last_name VARCHAR(32),
    par_role user_roles,
    par_city city_names,
    par_country country_names
) RETURNS SETOF users_view AS $$
DECLARE
    created_user_id BIGINT;
BEGIN
    INSERT INTO users (
        login,
        email,
        tel_number,
        password_hash,
        first_name,
        last_name,
        role,
        city,
        country
    )
    VALUES (
        par_login,
        par_email,
        par_tel_number,
        par_password_hash,
        par_first_name,
        par_last_name,
        par_role,
        par_city,
        par_country
    )
    RETURNING id INTO created_user_id;
    RETURN QUERY 
    SELECT * FROM users_view WHERE id = created_user_id;
END;
$$ LANGUAGE plpgsql;