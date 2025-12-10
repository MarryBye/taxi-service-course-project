CREATE OR REPLACE FUNCTION auth_user(
    par_login VARCHAR(32)
) RETURNS TABLE(
    id BIGINT,
    login VARCHAR(32),
    password_hash VARCHAR(128),
    role user_roles
) AS $$
BEGIN
    RETURN QUERY
    SELECT u.id, u.login, u.password_hash, u.role FROM users AS u
    WHERE u.login = par_login;
END;
$$ LANGUAGE plpgsql;