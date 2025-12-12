CREATE OR REPLACE PROCEDURE user_schema.update_data(
    p_user_id BIGINT,
    p_email VARCHAR,
    p_tel_number VARCHAR,
    p_password_hash VARCHAR,
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_country country_names,
    p_city city_names
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    UPDATE users
    SET email = p_email,
        tel_number = p_tel_number,
        password_hash = p_password_hash,
        first_name = p_first_name,
        last_name = p_last_name,
        country = p_country,
        city = p_city,
        changed_at = NOW()
    WHERE id = p_user_id;
END;
$$;