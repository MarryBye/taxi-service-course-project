CREATE OR REPLACE PROCEDURE register(
    p_login VARCHAR(32),
    p_email VARCHAR(128),
    p_tel_number VARCHAR(32),
    p_password VARCHAR(512),
    p_first_name VARCHAR(32),
    p_last_name VARCHAR(32),
    p_country public.country_names,
    p_city public.city_names
) SECURITY DEFINER AS $$
BEGIN
    CALL admin.create_user(p_login, p_email, p_tel_number, p_password, p_first_name, p_last_name, p_country, p_city, 'client');
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION auth(
    p_login VARCHAR(32)
) RETURNS TABLE(
    id BIGINT,
    login VARCHAR(32),
    password_hash VARCHAR(512),
    role user_roles
) SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT u.id, u.login, u.password_hash, u.role
        FROM private.users AS u
        WHERE u.login = p_login;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_current_user() RETURNS BIGINT SECURITY DEFINER AS $$
BEGIN
    RETURN (SELECT id from private.users WHERE login = current_user);
END;
$$ LANGUAGE plpgsql;