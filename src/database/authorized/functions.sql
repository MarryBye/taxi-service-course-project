CREATE OR REPLACE FUNCTION authorized.get_current_order()
RETURNS admin.orders_view SECURITY DEFINER AS $$
DECLARE
    result admin.orders_view;
    p_client_id BIGINT;
BEGIN
    p_client_id := public.get_current_user();
    SELECT * INTO result FROM admin.orders_view AS ov
    WHERE ov.client_id = p_client_id AND
          ov.status != 'canceled' AND
          ov.status != 'completed'
    ORDER BY ov.created_at DESC
    LIMIT 1;

    RETURN result;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE authorized.make_order(
    p_order_class public.car_classes,
    p_payment_method public.payment_methods,
    p_amount NUMERIC,
    p_adresses address[]
) SECURITY DEFINER AS $$
DECLARE
    has_active_order BOOLEAN;
    p_client_id BIGINT;
BEGIN
    p_client_id := public.get_current_user();
    has_active_order := (SELECT id FROM authorized.get_current_order()) IS NOT NULL;
    IF (has_active_order) THEN
        RAISE EXCEPTION 'Client with id % already has active order', p_client_id;
    END IF;
    CALL admin.create_order(
        p_client_id,
        'searching_for_driver',
        p_order_class,
        p_payment_method,
        p_amount,
        p_adresses
    );
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION authorized.get_client_history() RETURNS SETOF admin.orders_view SECURITY DEFINER AS $$
DECLARE
    p_client_id BIGINT;
BEGIN
    p_client_id := public.get_current_user();
    RETURN QUERY
        SELECT * FROM admin.orders_view AS ov
        WHERE ov.client_id = p_client_id
        ORDER BY ov.created_at DESC;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE authorized.rate_order_by_client(
    p_mark INT,
    p_comment VARCHAR(256),
    p_driver_tags public.driver_tags[]
) SECURITY DEFINER AS $$
DECLARE
    p_client_id BIGINT;
    current_order admin.orders_view%ROWTYPE;
    is_waiting_for_mark BOOLEAN;
    tag public.driver_tags;
BEGIN
    p_client_id := public.get_current_user();
    current_order := (SELECT * FROM authorized.get_current_order());
    IF (current_order.id IS NULL) THEN
        RAISE EXCEPTION 'You have not active orders to mark';
    END IF;
    is_waiting_for_mark := current_order.status = 'waiting_for_mark';
    IF (NOT is_waiting_for_mark) THEN
        RAISE EXCEPTION 'You cant mark this order for now';
    END IF;
    INSERT INTO private.order_ratings
        (order_id, mark_by, mark, comment)
    VALUES
        (current_order.id, p_client_id, p_mark, p_comment);
    FOREACH tag IN ARRAY p_driver_tags LOOP
        INSERT INTO private.order_driver_tags
            (order_id, tag)
        VALUES
            (current_order.id, tag);
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE authorized.cancel_current_order(
    p_comment VARCHAR(256),
    p_driver_tags public.driver_cancel_tags[]
) SECURITY DEFINER AS $$
DECLARE
    p_client_id BIGINT;
    current_order_id BIGINT;
    tag public.driver_cancel_tags;
BEGIN
    p_client_id := public.get_current_user();
    current_order_id := (SELECT id FROM authorized.get_current_order());

    IF (current_order_id IS NULL) THEN
        RAISE EXCEPTION 'No active orders found for client with id %', p_client_id;
    END IF;

    CALL admin.cancel_order(current_order_id);

    INSERT INTO private.order_cancels
        (order_id, canceled_by, comment)
    VALUES
        (current_order_id, p_client_id, p_comment);

    FOREACH tag IN ARRAY p_driver_tags LOOP
        INSERT INTO private.order_driver_tags
            (order_id, tag)
        VALUES
            (current_order_id, tag);
    END LOOP;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE authorized.update_profile(
    p_email VARCHAR(128) DEFAULT NULL,
    p_tel_number VARCHAR(32) DEFAULT NULL,
    p_password VARCHAR(512) DEFAULT NULL,
    p_first_name VARCHAR(32) DEFAULT NULL,
    p_last_name VARCHAR(32) DEFAULT NULL,
    p_country public.country_names DEFAULT NULL,
    p_city public.city_names DEFAULT NULL
) SECURITY DEFINER AS $$
DECLARE
    p_client_id BIGINT;
    updated_user_login VARCHAR(32);
BEGIN
    p_client_id := public.get_current_user();
    UPDATE private.users
    SET
        email = coalesce(p_email, email),
        tel_number = coalesce(p_tel_number, tel_number),
        password_hash = coalesce(p_password, password_hash),
        first_name = coalesce(p_first_name, first_name),
        last_name = coalesce(p_last_name, last_name),
        country = coalesce(p_country, country),
        city = coalesce(p_city, city)
    WHERE id = p_client_id
    RETURNING login INTO updated_user_login;

    IF (NOT p_password IS NULL) THEN
        CALL admin.change_psql_user_password(updated_user_login, p_password);
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION authorized.get_profile() RETURNS admin.clients_view SECURITY DEFINER AS $$
DECLARE
    p_client_id BIGINT;
    p_client_info admin.users_view;
BEGIN
    p_client_id := public.get_current_user();
    p_client_info := (SELECT * FROM admin.clients_view WHERE id = p_client_id);
    return p_client_info;
END;
$$ LANGUAGE plpgsql;