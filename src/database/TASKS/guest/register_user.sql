CREATE OR REPLACE PROCEDURE guest_schema.register_user(
    p_login VARCHAR,
    p_email VARCHAR,
    p_tel_number VARCHAR,
    p_password_hash VARCHAR,
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_role user_roles,
    p_country country_names,
    p_city city_names
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO users(login, email, tel_number, password_hash, first_name, last_name, role, country, city)
    VALUES (p_login, p_email, p_tel_number, p_password_hash, p_first_name, p_last_name, p_role, p_country, p_city);
END;
$$;