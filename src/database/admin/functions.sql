---------------------------------------
-- PSQL USERS USAGE
---------------------------------------

CREATE OR REPLACE PROCEDURE admin.create_psql_user(
    p_login VARCHAR(32),
    p_password VARCHAR(512),
    p_role user_roles
) SECURITY DEFINER AS $$
BEGIN
    EXECUTE FORMAT('CREATE USER %I WITH PASSWORD %L;', p_login, p_password);
    EXECUTE FORMAT('GRANT %I TO %I;', p_role, p_login);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.set_psql_user_role(
    p_login VARCHAR(32),
    p_role user_roles
) SECURITY DEFINER AS $$
BEGIN
    IF p_login = 'postgres' THEN
        RAISE EXCEPTION 'You cannot change role for postgres user';
    END IF;
    IF p_role = 'guest' THEN
        RAISE EXCEPTION 'You cannot set guest role for user';
    END IF;
    IF p_role = 'postgres' THEN
        RAISE EXCEPTION 'You cannot set postgres role for user';
    END IF;
    EXECUTE FORMAT('REVOKE guest, client, driver, admin FROM %I;', p_login);
    EXECUTE FORMAT('GRANT %I TO %I;', p_role, p_login);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.change_psql_user_password(
    p_login VARCHAR(32),
    p_password VARCHAR(512)
) SECURITY DEFINER AS $$
BEGIN
    IF p_login = 'postgres' THEN
        RAISE EXCEPTION 'You cannot change password for postgres user';
    END IF;
    EXECUTE FORMAT('ALTER USER %I WITH PASSWORD %L;', p_login, p_password);
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

---------------------------------------
-- USERS TABLE USAGE
---------------------------------------

CREATE OR REPLACE PROCEDURE admin.create_user(
    p_login VARCHAR(32),
    p_email VARCHAR(128),
    p_tel_number VARCHAR(32),
    p_password VARCHAR(512),
    p_first_name VARCHAR(32),
    p_last_name VARCHAR(32),
    p_country public.country_names,
    p_city public.city_names,
    p_role public.user_roles
) SECURITY DEFINER AS $$
BEGIN
    INSERT INTO private.users(login, email, tel_number, password_hash, first_name, last_name, country, city, role)
    VALUES (p_login, p_email, p_tel_number, p_password, p_first_name, p_last_name, p_country, p_city, p_role);
    CALL admin.create_psql_user(p_login, p_password, p_role);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.delete_user(
    p_login VARCHAR(32)
) SECURITY DEFINER AS $$
BEGIN
    DELETE FROM private.users WHERE login = p_login;
    CALL admin.delete_psql_user(p_login);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.update_user(
    p_email VARCHAR(128),
    p_tel_number VARCHAR(32),
    p_password VARCHAR(512),
    p_first_name VARCHAR(32),
    p_last_name VARCHAR(32),
    p_country public.country_names,
    p_city public.city_names,
    p_role public.user_roles
) SECURITY DEFINER AS $$
BEGIN
    UPDATE private.users
    SET
        email = coalesce(p_email, email),
        tel_number = coalesce(p_tel_number, tel_number),
        password_hash = coalesce(p_password, password_hash),
        first_name = coalesce(p_first_name, first_name),
        last_name = coalesce(p_last_name, last_name),
        country = coalesce(p_country, country),
        city = coalesce(p_city, city),
        role = coalesce(p_role, role)
    WHERE login = current_user;

    CALL admin.set_psql_user_role(current_user, p_role);
    CALL admin.change_psql_user_password(current_user, p_password);
END;
$$ LANGUAGE plpgsql;