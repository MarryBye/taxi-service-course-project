CREATE OR REPLACE FUNCTION update_user(
    par_id BIGINT,
    par_email VARCHAR(128),
    par_tel_number VARCHAR(32),
    par_password_hash VARCHAR(512),
    par_first_name VARCHAR(32),
    par_last_name VARCHAR(32),
    par_role user_roles
) RETURNS SETOF users_view AS $$
DECLARE
    updated_user_id BIGINT;
BEGIN
    UPDATE users
    SET 
        email = COALESCE(par_email, email),
        tel_number = COALESCE(par_tel_number, tel_number),
        password_hash = COALESCE(par_password_hash, password_hash),
        first_name = COALESCE(par_first_name, first_name),
        last_name = COALESCE(par_last_name, last_name),
        role = COALESCE(par_role, role)
    WHERE par_id = id
    RETURNING id INTO updated_user_id;
    RETURN QUERY 
    SELECT * FROM users_view WHERE id = updated_user_id;
END;
$$ LANGUAGE plpgsql;