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

CREATE OR REPLACE FUNCTION admin.list_users(
    p_offset INT DEFAULT 0,
    p_limit INT DEFAULT 100,
    p_f_country public.country_names DEFAULT NULL,
    p_f_city public.city_names DEFAULT NULL,
    p_f_role public.user_roles DEFAULT NULL
)
RETURNS SETOF admin.users_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.users_view
        WHERE
            (p_f_country IS NULL OR country = p_f_country) AND
            (p_f_city IS NULL OR city = p_f_city) AND
            (p_f_role IS NULL OR role = p_f_role)
        LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION admin.get_user(
    p_user_id BIGINT
)
RETURNS SETOF admin.users_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.users_view WHERE id = p_user_id;
END;
$$ LANGUAGE plpgsql;

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
    p_user_id BIGINT
) SECURITY DEFINER AS $$
DECLARE
    user_login VARCHAR(32);
BEGIN
    user_login := (SELECT login FROM private.users WHERE id = p_user_id);
    DELETE FROM private.users WHERE id = p_user_id;
    CALL admin.delete_psql_user(user_login);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.update_user(
    p_user_id BIGINT,
    p_email VARCHAR(128),
    p_tel_number VARCHAR(32),
    p_password VARCHAR(512),
    p_first_name VARCHAR(32),
    p_last_name VARCHAR(32),
    p_country public.country_names,
    p_city public.city_names,
    p_role public.user_roles
) SECURITY DEFINER AS $$
DECLARE
    updated_user_login VARCHAR(32);
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
    WHERE id = p_user_id
    RETURNING login INTO updated_user_login;

    IF (NOT p_role IS NULL) THEN
        CALL admin.set_psql_user_role(updated_user_login, p_role);
    END IF;

    IF (NOT p_password IS NULL) THEN
        CALL admin.change_psql_user_password(updated_user_login, p_password);
    END IF;
END;
$$ LANGUAGE plpgsql;

---------------------------------------
-- CARS TABLE USAGE
---------------------------------------

CREATE OR REPLACE FUNCTION admin.list_cars(
    p_offset INT DEFAULT 0,
    p_limit INT DEFAULT 100
) RETURNS SETOF admin.cars_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.cars_view LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION admin.get_car(
    p_car_id BIGINT
) RETURNS SETOF admin.cars_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.cars_view WHERE id = p_car_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.create_car(
    p_mark VARCHAR(32),
    p_model VARCHAR(32),
    p_car_number VARCHAR(32),
    p_country public.country_names,
    p_city public.city_names,
    p_color VARCHAR(32),
    p_car_class public.car_classes,
    p_car_status public.car_statuses,
    p_driver_id BIGINT DEFAULT NULL
) SECURITY DEFINER AS $$
BEGIN
    INSERT INTO private.cars AS c
        (mark, model, car_number, country, city, color, car_class, car_status, driver_id)
    VALUES
        (p_mark, p_model, p_car_number, p_country, p_city, p_color, p_car_class, p_car_status, p_driver_id);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.delete_car(
    p_car_id BIGINT
) SECURITY DEFINER AS $$
BEGIN
    DELETE FROM private.cars WHERE id = p_car_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.update_car(
    p_car_id BIGINT,
    p_driver_id BIGINT DEFAULT NULL,
    p_mark VARCHAR(32) DEFAULT NULL,
    p_model VARCHAR(32) DEFAULT NULL,
    p_car_number VARCHAR(32) DEFAULT NULL,
    p_country public.country_names DEFAULT NULL,
    p_city public.city_names DEFAULT NULL,
    p_color VARCHAR(32) DEFAULT NULL,
    p_car_class public.car_classes DEFAULT NULL,
    p_car_status public.car_statuses DEFAULT NULL
) SECURITY DEFINER AS $$
BEGIN
    UPDATE private.cars
    SET
        driver_id = coalesce(p_driver_id, driver_id),
        mark = coalesce(p_mark, mark),
        model = coalesce(p_model, model),
        car_number = coalesce(p_car_number, car_number),
        country = coalesce(p_country, country),
        city = coalesce(p_city, city),
        color = coalesce(p_color, color),
        car_class = coalesce(p_car_class, car_class),
        car_status = coalesce(p_car_status, car_status)
    WHERE id = p_car_id;
END;
$$ LANGUAGE plpgsql;

---------------------------------------
-- ORDERS TABLE USAGE
---------------------------------------

CREATE OR REPLACE FUNCTION admin.list_orders(
    p_offset INT DEFAULT 0,
    p_limit INT DEFAULT 100
) RETURNS SETOF admin.orders_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.orders_view LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION admin.get_order(
    p_order_id BIGINT
) RETURNS SETOF admin.orders_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.orders_view WHERE id = p_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.create_order(
    p_client_id BIGINT,
    p_status public.order_statuses,
    p_order_class public.car_classes,
    p_payment_method public.payment_methods,
    p_amount NUMERIC,
    p_adresses address[],
    p_driver_id BIGINT DEFAULT NULL
) SECURITY DEFINER AS $$
DECLARE
    new_transaction_id BIGINT;
    new_order_id BIGINT;
    new_route_id BIGINT;
    i INT;
    ad address;
BEGIN
    INSERT INTO private.transactions
        (user_id, balance_type, transaction_type, payment_method, amount)
    VALUES
        (p_client_id, 'payment', 'debit', p_payment_method, p_amount)
    RETURNING id INTO new_transaction_id;

    INSERT INTO private.orders
        (client_id, driver_id, status, order_class, transaction_id)
    VALUES
        (p_client_id, p_driver_id, p_status, p_order_class, new_transaction_id)
    RETURNING id INTO new_order_id;

    INSERT INTO private.routes
        (order_id, start_location, end_location, distance)
    VALUES
        (new_order_id, p_adresses[1], p_adresses[array_length(p_adresses, 1)], 0)
    RETURNING id INTO new_route_id;

    i := 1;
    FOREACH ad IN ARRAY p_adresses LOOP
        INSERT INTO private.route_points
            (route_id, position_index, location)
        VALUES
            (new_route_id, i, ad);
        i := i + 1;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.delete_order(
    p_order_id BIGINT
) SECURITY DEFINER AS $$
BEGIN
    DELETE FROM private.orders WHERE id = p_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.update_order(
    p_order_id BIGINT,
    p_status public.order_statuses DEFAULT NULL,
    p_order_class public.car_classes DEFAULT NULL
) SECURITY DEFINER AS $$
BEGIN
    UPDATE private.orders
    SET
        status = coalesce(p_status, status),
        order_class = coalesce(p_order_class, order_class)
    WHERE id = p_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.cancel_order(
    p_order_id BIGINT
) SECURITY DEFINER AS $$
BEGIN
    UPDATE private.orders
    SET status = 'cancelled'
    WHERE id = p_order_id;
END;
$$ LANGUAGE plpgsql;

---------------------------------------
-- MAINTENANCE TABLE USAGE
---------------------------------------

CREATE OR REPLACE FUNCTION admin.list_maintenances(
    p_offset INT DEFAULT 0,
    p_limit INT DEFAULT 100
) RETURNS SETOF admin.maintenance_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.maintenance_view LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION admin.get_maintenance(
    p_maintenance_id BIGINT
) RETURNS SETOF admin.maintenance_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.maintenance_view WHERE id = p_maintenance_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.create_maintenance(
    p_car_id BIGINT,
    p_description VARCHAR(2048),
    p_cost NUMERIC,
    p_status public.maintenance_statuses
) SECURITY DEFINER AS $$
BEGIN
    INSERT INTO private.maintenances
        (car_id, description, cost, status)
    VALUES
        (p_car_id, p_description, p_cost, p_status);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.delete_maintenance(
    p_maintenance_id BIGINT
) SECURITY DEFINER AS $$
BEGIN
    DELETE FROM private.maintenances WHERE id = p_maintenance_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.update_maintenance(
    p_maintenance_id BIGINT,
    p_description VARCHAR(2048) DEFAULT NULL,
    p_cost NUMERIC DEFAULT NULL,
    p_status public.maintenance_statuses DEFAULT NULL
) SECURITY DEFINER AS $$
BEGIN
    UPDATE private.maintenances
    SET
        description = coalesce(p_description, description),
        cost = coalesce(p_cost, cost),
        status = coalesce(p_status, status)
    WHERE id = p_maintenance_id;
END;
$$ LANGUAGE plpgsql;

---------------------------------------
-- TRANSACTION TABLE USAGE
---------------------------------------

CREATE OR REPLACE FUNCTION admin.get_transaction(
    p_transaction_id BIGINT
) RETURNS SETOF admin.transactions_view
SECURITY DEFINER AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM admin.transactions_view WHERE id = p_transaction_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE admin.create_transaction(
    p_user_id BIGINT,
    p_balance_type public.balance_types,
    p_transaction_type public.transaction_type,
    p_payment_method public.payment_methods,
    p_amount NUMERIC
) SECURITY DEFINER AS $$
BEGIN
    INSERT INTO private.transactions
        (user_id, balance_type, transaction_type, payment_method, amount)
    VALUES
        (p_user_id, p_balance_type, p_transaction_type, p_payment_method, p_amount);
END;
$$ LANGUAGE plpgsql;