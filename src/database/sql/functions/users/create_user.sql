CREATE OR REPLACE FUNCTION create_user(
    login VARCHAR(32),
    email VARCHAR(128),
    tel_number VARCHAR(32),
    password_hash VARCHAR(512),
    first_name VARCHAR(32),
    last_name VARCHAR(32),
    role user_roles
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
        role
    )
    VALUES (
        login,
        email,
        tel_number,
        password_hash,
        first_name,
        last_name,
        role
    )
    RETURNING id INTO created_user_id;
    RETURN QUERY 
    SELECT * FROM users_view WHERE id = created_user_id;
END;
$$ LANGUAGE plpgsql;