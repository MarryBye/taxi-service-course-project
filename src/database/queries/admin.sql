CREATE OR REPLACE PROCEDURE admin.create_psql_user(
    p_login VARCHAR(32),
    p_hashed_password VARCHAR(512)
) SECURITY DEFINER AS $$
BEGIN
    EXECUTE FORMAT('CREATE USER %I WITH PASSWORD %L;', p_login, p_hashed_password);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.set_psql_user_role(
    p_login VARCHAR(32),
    p_role public.user_roles
) SECURITY DEFINER AS $$
BEGIN
    IF p_login = 'postgres' THEN
        RAISE EXCEPTION 'You cannot change role for postgres user';
    END IF;
    EXECUTE FORMAT('REVOKE client, driver, admin FROM %I;', p_login);
    EXECUTE FORMAT('GRANT %I TO %I;', p_role, p_login);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.change_psql_user_password(
    p_login VARCHAR(32),
    p_hashed_password VARCHAR(512)
) SECURITY DEFINER AS $$
BEGIN
    IF p_login = 'postgres' THEN
        RAISE EXCEPTION 'You cannot change password for postgres user';
    END IF;
    EXECUTE FORMAT('ALTER USER %I WITH PASSWORD %L;', p_login, p_hashed_password);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.delete_psql_user(
    p_login VARCHAR(32)
) SECURITY DEFINER AS $$
BEGIN
    IF p_login = 'postgres' THEN
        RAISE EXCEPTION 'You cannot delete postgres user';
    END IF;
    EXECUTE FORMAT('DROP USER %I;', p_login);
END;
$$ LANGUAGE plpgsql;

-----------------------------------------------------------------------------------