-- CRUD Users

CREATE OR REPLACE PROCEDURE assign_role(par_login VARCHAR(32), role user_roles)
AS $$
DECLARE
    old_role name;
BEGIN
    SELECT u.role INTO old_role FROM users AS u WHERE login = par_login;
    IF NOT old_role IS NULL THEN
        EXECUTE FORMAT('REVOKE %I FROM %I;', old_role, par_login);
    END IF;
    EXECUTE FORMAT('GRANT %I TO %I;', role, par_login);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION list_users(
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF users_view AS $$
BEGIN
    SET ROLE "admin";
    RETURN QUERY
        SELECT *
        FROM users_view
        LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_user(
    par_filter_id BIGINT
) RETURNS SETOF users_view AS $$
BEGIN
    SET ROLE "admin";
    RETURN QUERY
        SELECT *
        FROM users_view
        WHERE
            id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_user(
    par_login VARCHAR(32),
    par_email VARCHAR(128),
    par_tel_number VARCHAR(32),
    par_password_hash VARCHAR(512),
    par_first_name VARCHAR(32),
    par_last_name VARCHAR(32),
    par_city city_names,
    par_country country_names,
    par_role user_roles DEFAULT 'client'
) RETURNS SETOF users_view AS $$
DECLARE
    created_user_id BIGINT;
BEGIN

    SET ROLE "admin";

    INSERT INTO users (
        login,
        email,
        tel_number,
        password_hash,
        first_name,
        last_name,
        city,
        country,
        role
    )
    VALUES (
        par_login,
        par_email,
        par_tel_number,
        par_password_hash,
        par_first_name,
        par_last_name,
        par_city,
        par_country,
        par_role
    )
    RETURNING id INTO created_user_id;

    INSERT INTO balances
        (user_id, balance, balance_type)
    VALUES
        (created_user_id, 0, 'payment'),
        (created_user_id, 0, 'earning');

    EXECUTE FORMAT('CREATE USER %I WITH PASSWORD %L;', par_login, par_password_hash);
    CALL assign_role(par_login, par_role);

    RETURN QUERY
    SELECT * FROM users_view WHERE id = created_user_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION register_user(
    par_login VARCHAR(32),
    par_email VARCHAR(128),
    par_tel_number VARCHAR(32),
    par_password_hash VARCHAR(512),
    par_city city_names,
    par_country country_names,
    par_first_name VARCHAR(32),
    par_last_name VARCHAR(32)
) RETURNS SETOF users_view
SECURITY DEFINER
AS $$
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
        city,
        country,
        role
    )
    VALUES (
        par_login,
        par_email,
        par_tel_number,
        par_password_hash,
        par_first_name,
        par_last_name,
        par_city,
        par_country,
        'client'
    )
    RETURNING id INTO created_user_id;

    INSERT INTO balances
        (user_id, balance, balance_type)
    VALUES
        (created_user_id, 0, 'payment'),
        (created_user_id, 0, 'earning');

    EXECUTE FORMAT('CREATE USER %I WITH PASSWORD %L;', par_login, par_password_hash);
    EXECUTE FORMAT('GRANT client TO %I;', par_login);

    RETURN QUERY
        SELECT * FROM users_view WHERE id = created_user_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_user(
    par_id BIGINT
) RETURNS VOID AS $$
DECLARE
    user_login VARCHAR(32);
BEGIN
    SET ROLE "admin";
    user_login := (SELECT login FROM users WHERE id = par_id);
    DELETE FROM users WHERE id = par_id;
    EXECUTE FORMAT('DROP USER IF EXISTS %I', user_login);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_user(
    par_id BIGINT,
    par_email VARCHAR(128) DEFAULT NULL,
    par_tel_number VARCHAR(32) DEFAULT NULL,
    par_first_name VARCHAR(32) DEFAULT NULL,
    par_last_name VARCHAR(32) DEFAULT NULL,
    par_password_hash VARCHAR(512) DEFAULT NULL,
    par_role user_roles DEFAULT NULL,
    par_city city_names DEFAULT NULL,
    par_country country_names DEFAULT NULL
) RETURNS SETOF users_view AS $$
DECLARE
    updated_user_id BIGINT;
    user_login VARCHAR(32);
BEGIN
    SET ROLE "admin";
    SELECT login INTO user_login FROM users WHERE id = par_id;

    UPDATE users
    SET
        email = COALESCE(par_email, email),
        tel_number = COALESCE(par_tel_number, tel_number),
        first_name = COALESCE(par_first_name, first_name),
        last_name = COALESCE(par_last_name, last_name),
        password_hash = COALESCE(par_password_hash, password_hash),
        city = COALESCE(par_city, city),
        country = COALESCE(par_country, country),
        role = COALESCE(par_role, role)
    WHERE par_id = id
    RETURNING id INTO updated_user_id;

    IF par_password_hash IS NOT NULL THEN
        EXECUTE FORMAT('ALTER USER %I WITH PASSWORD %L;', user_login, par_password_hash);
    END IF;

    IF par_role IS NOT NULL THEN
        CALL assign_role(user_login, par_role);
    END IF;

    RETURN QUERY
    SELECT * FROM users_view WHERE id = updated_user_id;
END;
$$ LANGUAGE plpgsql;

-- CRUD Drivers

CREATE OR REPLACE FUNCTION list_drivers(
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF drivers_view AS $$
BEGIN
    SET ROLE "admin";
    RETURN QUERY
        SELECT *
        FROM drivers_view
        LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_driver(
    par_filter_id BIGINT
) RETURNS SETOF drivers_view AS $$
BEGIN
    SET ROLE "admin";
    RETURN QUERY
        SELECT *
        FROM drivers_view
        WHERE
            id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_driver(
    par_login VARCHAR(32),
    par_email VARCHAR(128),
    par_tel_number VARCHAR(32),
    par_password_hash VARCHAR(512),
    par_first_name VARCHAR(32),
    par_last_name VARCHAR(32),
    par_city city_names,
    par_country country_names,
    par_car_id BIGINT DEFAULT NULL
) RETURNS SETOF drivers_view AS $$
DECLARE
    new_driver_id BIGINT;
BEGIN
    SET ROLE "admin";
    SELECT id INTO new_driver_id FROM create_user(
        par_login,
        par_email,
        par_tel_number,
        par_password_hash,
        par_first_name,
        par_last_name,
        par_city,
        par_country,
        'driver'
    );

    IF par_car_id IS NOT NULL THEN
        UPDATE cars SET driver_id = new_driver_id WHERE id = par_car_id;
    END IF;

    RETURN QUERY SELECT * FROM drivers_view WHERE id = new_driver_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_driver(
    par_id BIGINT,
    par_email VARCHAR(128) DEFAULT NULL,
    par_tel_number VARCHAR(32) DEFAULT NULL,
    par_password_hash VARCHAR(512) DEFAULT NULL,
    par_first_name VARCHAR(32) DEFAULT NULL,
    par_last_name VARCHAR(32) DEFAULT NULL,
    par_role user_roles DEFAULT NULL,
    par_city city_names DEFAULT NULL,
    par_country country_names DEFAULT NULL,
    par_car_id BIGINT DEFAULT NULL
) RETURNS SETOF drivers_view AS $$
DECLARE
    updated_driver_id BIGINT;
BEGIN
    SET ROLE "admin";
    SELECT id INTO updated_driver_id FROM update_user(
        par_id,
        par_email,
        par_tel_number,
        par_first_name,
        par_last_name,
        par_password_hash,
        par_role,
        par_city,
        par_country
    );

    IF par_car_id IS NOT NULL THEN
        UPDATE cars SET driver_id = updated_driver_id WHERE id = par_car_id;
    END IF;

    RETURN QUERY SELECT * FROM drivers_view WHERE id = updated_driver_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_driver(
    par_id BIGINT
) RETURNS VOID AS $$
BEGIN
    SET ROLE "admin";
    PERFORM delete_user(par_id);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION list_admins(
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF admins_view AS $$
BEGIN
    SET ROLE "admin";
    RETURN QUERY
    SELECT * FROM admins_view LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_admin(
    par_filter_id BIGINT
) RETURNS SETOF admins_view AS $$
BEGIN
    SET ROLE "admin";
    RETURN QUERY
    SELECT * FROM admins_view WHERE id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_admin(
    par_login VARCHAR(32),
    par_email VARCHAR(128),
    par_tel_number VARCHAR(32),
    par_password_hash VARCHAR(512),
    par_first_name VARCHAR(32),
    par_last_name VARCHAR(32),
    par_city city_names,
    par_country country_names
) RETURNS SETOF admins_view AS $$
DECLARE
    created_user_id BIGINT;
BEGIN
    SET ROLE "admin";
    SELECT id INTO created_user_id FROM create_user(
        par_login,
        par_email,
        par_tel_number,
        par_password_hash,
        par_first_name,
        par_last_name,
        par_city,
        par_country,
        'admin'
    );

    RETURN QUERY
    SELECT * FROM admins_view WHERE id = created_user_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_admin(
    par_id BIGINT
) RETURNS VOID AS $$
BEGIN
    SET ROLE "admin";
    PERFORM delete_user(
        par_id
    );
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_admin(
    par_id BIGINT,
    par_email VARCHAR(128) DEFAULT NULL,
    par_tel_number VARCHAR(32) DEFAULT NULL,
    par_password_hash VARCHAR(512) DEFAULT NULL,
    par_first_name VARCHAR(32) DEFAULT NULL,
    par_last_name VARCHAR(32) DEFAULT NULL,
    par_role user_roles DEFAULT NULL,
    par_city city_names DEFAULT NULL,
    par_country country_names DEFAULT NULL
) RETURNS SETOF admins_view AS $$
DECLARE
    updated_user_id BIGINT;
BEGIN
    SET ROLE "admin";
    SELECT id INTO updated_user_id FROM update_user(
        par_id,
        par_email,
        par_tel_number,
        par_password_hash,
        par_first_name,
        par_last_name,
        par_role,
        par_city,
        par_country
    );

    RETURN QUERY
        SELECT * FROM admins_view WHERE id = updated_user_id;
END;
$$ LANGUAGE plpgsql;

-- CRUD Orders

CREATE OR REPLACE FUNCTION list_orders(
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF orders_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM orders_view
        LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_order(
    par_filter_id BIGINT
) RETURNS SETOF orders_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM orders_view
        WHERE id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_order(
    par_client_id BIGINT,
    par_price NUMERIC,
    par_payment_method payment_methods,
    par_order_class car_classes,
    par_addresses address[]
)
RETURNS SETOF orders_view AS $$
DECLARE
    new_order_id BIGINT;
    new_route_id BIGINT;
    addr address;
    idx INT := 0;
BEGIN
    -- 1. Создать заказ
    INSERT INTO orders(client_id, status, order_class)
    VALUES (par_client_id, 'searching_for_driver', par_order_class)
    RETURNING id INTO new_order_id;

    -- 2. Создать маршрут (первый и последний адрес)
    INSERT INTO routes(order_id, start_location, end_location, distance)
    VALUES (
        new_order_id,
        par_addresses[1],
        par_addresses[array_length(par_addresses,1)],
        0 -- расстояние можно рассчитывать отдельно
    )
    RETURNING id INTO new_route_id;

    -- 3. Создать точки маршрута
    FOREACH addr IN ARRAY par_addresses LOOP
        INSERT INTO route_points(route_id, position_index, location)
        VALUES (new_route_id, idx, addr);
        idx := idx + 1;
    END LOOP;

    -- 4. Создать транзакцию (платёж)
    INSERT INTO transactions(user_id, balance_type, transaction_type, payment_method, amount, order_id)
    VALUES (par_client_id, 'payment', 'debit', par_payment_method, par_price, new_order_id);

    RETURN QUERY
        SELECT * FROM orders_view WHERE id = new_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_order(
    par_order_id BIGINT,
    par_status order_statuses
) RETURNS SETOF orders_view AS $$
BEGIN
    UPDATE orders SET status = par_status WHERE id = par_order_id;
    RETURN QUERY SELECT * FROM orders_view WHERE id = par_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_order(
    par_order_id BIGINT
) RETURNS VOID AS $$
BEGIN
    DELETE FROM orders WHERE id = par_order_id;
END;
$$ LANGUAGE plpgsql;

-- CRUD Cars

CREATE OR REPLACE FUNCTION list_cars(
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF cars_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM cars_view
        LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_car(
    par_filter_id BIGINT
) RETURNS SETOF cars_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM cars_view
        WHERE id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_car(
    par_mark VARCHAR(32),
    par_model VARCHAR(32),
    par_car_number VARCHAR(32),
    par_country country_names,
    par_city city_names,
    par_color VARCHAR(32),
    par_car_class car_classes,
    par_car_status car_statuses,
    par_driver_id BIGINT DEFAULT NULL
) RETURNS SETOF cars_view AS $$
DECLARE
    new_car_id BIGINT;
BEGIN
    INSERT INTO cars(driver_id, mark, model, car_number, country, city, color, car_class, car_status)
    VALUES (par_driver_id, par_mark, par_model, par_car_number, par_country, par_city, par_color, par_car_class, par_car_status)
    RETURNING id INTO new_car_id;
    RETURN QUERY SELECT * FROM cars_view WHERE id = new_car_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_car(
    par_id BIGINT,

    par_driver_id BIGINT DEFAULT NULL,
    par_mark VARCHAR(32) DEFAULT NULL,
    par_model VARCHAR(32) DEFAULT NULL,
    par_car_number VARCHAR(32) DEFAULT NULL,
    par_country country_names DEFAULT NULL,
    par_city city_names DEFAULT NULL,
    par_color VARCHAR(32) DEFAULT NULL,
    par_car_class car_classes DEFAULT NULL,
    par_car_status car_statuses DEFAULT NULL
) RETURNS SETOF cars_view AS $$
BEGIN
    UPDATE cars SET
        driver_id = COALESCE(par_driver_id, driver_id),
        mark = COALESCE(par_mark, mark),
        model = COALESCE(par_model, model),
        car_number = COALESCE(par_car_number, car_number),
        country = COALESCE(par_country, country),
        city = COALESCE(par_city, city),
        color = COALESCE(par_color, color),
        car_class = COALESCE(par_car_class, car_class),
        car_status = COALESCE(par_car_status, car_status)
    WHERE id = par_id;
    RETURN QUERY SELECT * FROM cars_view WHERE id = par_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_car(
    par_id BIGINT
) RETURNS VOID AS $$
BEGIN
    DELETE FROM cars WHERE id = par_id;
END;
$$ LANGUAGE plpgsql;

-- CRUD Maintenances

CREATE OR REPLACE FUNCTION list_maintenances (
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF maintenance_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM maintenance_view
        LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_maintenance(
    par_filter_id BIGINT
) RETURNS SETOF maintenance_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM maintenance_view
        WHERE id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_maintenance(
    par_car_id BIGINT,
    par_description VARCHAR(256),
    par_cost NUMERIC
) RETURNS SETOF maintenance_view AS $$
DECLARE
    maintenance_id BIGINT;
BEGIN
    INSERT INTO maintenances(car_id, description, cost)
    VALUES (par_car_id, par_description, par_cost)
    RETURNING id INTO maintenance_id;
    RETURN QUERY
        SELECT * FROM maintenance_view WHERE id = maintenance_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_maintenance(
    par_maintenance_id BIGINT,
    par_description VARCHAR(256) DEFAULT NULL,
    par_status maintenance_statuses DEFAULT NULL,
    par_cost NUMERIC DEFAULT NULL,
    par_maintenance_end TIMESTAMP DEFAULT NULL
) RETURNS SETOF maintenance_view AS $$
BEGIN
    UPDATE maintenances SET
        description = COALESCE(par_description, description),
        status = COALESCE(par_status, status),
        cost = COALESCE(par_cost, cost),
        maintenance_end = COALESCE(par_maintenance_end, maintenance_end)
    WHERE id = par_maintenance_id;
    RETURN QUERY
        SELECT * FROM maintenance_view WHERE id = par_maintenance_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_maintenance(
    par_maintenance_id BIGINT
) RETURNS VOID AS $$
BEGIN
    DELETE FROM maintenances WHERE id = par_maintenance_id;
END;
$$ LANGUAGE plpgsql;

-- CRUD Transactions

CREATE OR REPLACE FUNCTION list_transactions(
    limit_number INT DEFAULT 100,
    offset_number INT DEFAULT 0
) RETURNS SETOF transactions_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM transactions_view
        LIMIT limit_number OFFSET offset_number;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_transaction(
    par_filter_id BIGINT
) RETURNS SETOF transactions_view AS $$
BEGIN
    RETURN QUERY
        SELECT *
        FROM transactions_view
        WHERE id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION create_transaction(
    par_user_id BIGINT,
    par_balance_type balance_types,
    par_transaction_type transaction_type,
    par_payment_method payment_methods,
    par_amount NUMERIC,
    par_order_id BIGINT DEFAULT NULL
) RETURNS SETOF transactions_view AS $$
DECLARE
    new_transaction_id BIGINT;
BEGIN
    INSERT INTO transactions(user_id, balance_type, transaction_type, payment_method, amount, order_id
    )
    VALUES (par_user_id, par_balance_type, par_transaction_type, par_payment_method,
        par_amount, par_order_id)
    RETURNING id INTO new_transaction_id;
    RETURN QUERY
        SELECT * FROM transactions_view WHERE id = new_transaction_id;
END;
$$ LANGUAGE plpgsql;

-- CRUD Profiles

CREATE OR REPLACE FUNCTION get_profile(
    par_filter_id BIGINT
) RETURNS SETOF users_view AS $$
BEGIN
    RETURN QUERY
        SELECT * FROM users_view WHERE id = par_filter_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_profile(
    par_id BIGINT,
    par_first_name VARCHAR(32) DEFAULT NULL,
    par_last_name VARCHAR(32) DEFAULT NULL,
    par_city city_names DEFAULT NULL,
    par_country country_names DEFAULT NULL
) RETURNS SETOF users_view AS $$
DECLARE
    updated_user_id BIGINT;
BEGIN
    UPDATE users SET
        first_name = COALESCE(par_first_name, first_name),
        last_name = COALESCE(par_last_name, last_name),
        city = COALESCE(par_city, city),
        country = COALESCE(par_country, country)
    WHERE id = par_id RETURNING id INTO updated_user_id;
    RETURN QUERY
        SELECT * FROM users_view WHERE id = updated_user_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION delete_profile(
    par_id BIGINT
) RETURNS VOID AS $$
DECLARE
    user_login VARCHAR(32);
BEGIN
    user_login := (SELECT login FROM users WHERE id = par_id);
    DELETE FROM users WHERE id = par_id;
    EXECUTE FORMAT('DROP USER IF EXISTS %I;', user_login);
END;
$$ LANGUAGE plpgsql;