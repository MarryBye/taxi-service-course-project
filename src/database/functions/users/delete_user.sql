CREATE OR REPLACE PROCEDURE delete_user(
    par_id BIGINT
) AS $$
BEGIN
    DELETE FROM users WHERE id = par_id;
END;
$$ LANGUAGE plpgsql;