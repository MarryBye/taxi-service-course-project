CREATE OR REPLACE FUNCTION workers.orders_history()
RETURNS SETOF admin.orders_view
SECURITY DEFINER
SET search_path = private, admin, workers, public
AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    RETURN QUERY
        SELECT *
        FROM admin.orders_view AS orders
        WHERE (orders.driver->>'id')::BIGINT = user_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION workers.acceptable_orders()
RETURNS SETOF admin.orders_view
SECURITY DEFINER
SET search_path = private, admin, workers, public
AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
    car_rec private.cars%ROWTYPE;
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    SELECT *
    INTO car_rec
    FROM private.cars AS cars
    WHERE cars.driver_id = user_id;

    IF car_rec.id IS NULL THEN
        RAISE EXCEPTION 'Driver has no car';
    END IF;

    RETURN QUERY
        SELECT orders.*
        FROM admin.orders_view AS orders
        WHERE
            orders.driver IS NULL
            AND orders.status = 'searching_for_driver'
            AND orders.order_class = car_rec.car_class
            AND (orders.client->'city'->>'id')::BIGINT = car_rec.city_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION workers.accept_order(
    p_order_id BIGINT
)
RETURNS SETOF admin.orders_view
SECURITY DEFINER
SET search_path = private, admin, workers, public
AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    UPDATE private.orders AS orders
    SET
        orders.order_class = user_id,
        orders.status = 'waiting_for_driver',
        orders.changed_at = NOW()
    WHERE
        orders.id = p_order_id
        AND orders.driver_id IS NULL
        AND orders.status = 'searching_for_driver';

    RETURN QUERY
        SELECT * FROM admin.orders_view WHERE id = p_order_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION workers.cancel_order(
    p_order_id BIGINT,
    p_comment VARCHAR(256),
    p_tags public.client_cancel_tags[]
)
RETURNS SETOF admin.orders_stat_view
SECURITY DEFINER
SET search_path = private, admin, workers, public
AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
    tag client_cancel_tags;
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    IF NOT (SELECT EXISTS(
        SELECT 1 FROM private.orders AS orders WHERE orders.id = p_order_id AND orders.driver_id = user_id
    )) THEN
        RAISE EXCEPTION 'Order not found';
    END IF;

    IF (array_length(p_tags, 1) < 1) OR (array_length(p_tags, 1) > 3) THEN
        RAISE EXCEPTION 'Invalid number of tags';
    END IF;

    UPDATE private.orders
    SET status = 'canceled', changed_at = NOW()
    WHERE id = p_order_id AND driver_id = user_id;

    INSERT INTO private.order_cancels(order_id, canceled_by, comment)
    VALUES (p_order_id, user_id, p_comment);

    FOREACH tag IN ARRAY p_tags LOOP
        INSERT INTO private.order_client_tags(order_id, tag)
        VALUES (p_order_id, tag);
    END LOOP;

    RETURN QUERY
        SELECT * FROM admin.orders_stat_view WHERE id = p_order_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION workers.current_order()
RETURNS SETOF admin.orders_view
SECURITY DEFINER
SET search_path = private, admin, workers, public
AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    RETURN QUERY
        SELECT *
        FROM admin.orders_view
        WHERE
            (driver->>'id')::BIGINT = user_id
            AND status NOT IN ('completed', 'canceled');
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.order_stat(
    p_order_id BIGINT
)
RETURNS SETOF admin.orders_stat_view SECURITY DEFINER AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    IF NOT (SELECT EXISTS(
        SELECT 1 FROM private.orders AS orders WHERE orders.id = p_order_id AND orders.driver_id = user_id
    )) THEN
        RAISE EXCEPTION 'Order not found';
    END IF;

    RETURN QUERY
        SELECT * FROM admin.orders_stat_view AS orders WHERE orders.id = p_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.rate_order(
    p_order_id BIGINT,
    p_mark INT,
    p_comment VARCHAR(256),
    p_tags public.client_tags[]
)
RETURNS SETOF admin.orders_stat_view
SECURITY DEFINER
SET search_path = private, admin, workers, public
AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
    tag client_tags;
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    IF NOT (SELECT EXISTS(
        SELECT 1 FROM private.orders AS orders WHERE orders.id = p_order_id AND orders.driver_id = user_id
    )) THEN
        RAISE EXCEPTION 'Order not found';
    END IF;

    IF (array_length(p_tags, 1) < 1) OR (array_length(p_tags, 1) > 3) THEN
        RAISE EXCEPTION 'Invalid number of tags';
    END IF;

    INSERT INTO private.order_ratings(order_id, mark_by, mark, comment)
    VALUES (p_order_id, user_id, p_mark, p_comment);

    FOREACH tag IN ARRAY p_tags LOOP
        INSERT INTO private.order_client_tags(order_id, tag)
        VALUES (p_order_id, tag);
    END LOOP;

    RETURN QUERY
        SELECT * FROM admin.orders_stat_view WHERE id = p_order_id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.submit_arrival()
RETURNS SETOF admin.orders_view SECURITY DEFINER AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
    current_order admin.orders_view%ROWTYPE := workers.current_order();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    UPDATE private.orders AS orders
    SET
        orders.status = 'waiting_for_client'
    WHERE orders.id = current_order.id AND orders.driver_id = user_id;

    RETURN QUERY SELECT * FROM admin.orders_view WHERE id = current_order.id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.submit_start()
RETURNS SETOF admin.orders_view SECURITY DEFINER AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
    current_order admin.orders_view%ROWTYPE := workers.current_order();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    UPDATE private.orders AS orders
    SET
        orders.status = 'in_progress'
    WHERE orders.id = current_order.id AND orders.driver_id = user_id;

    RETURN QUERY SELECT * FROM admin.orders_view WHERE id = current_order.id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.submit_finish()
RETURNS SETOF admin.orders_view SECURITY DEFINER AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
    current_order admin.orders_view%ROWTYPE := workers.current_order();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    UPDATE private.orders AS orders
    SET
        orders.status = 'waiting_for_marks'
    WHERE orders.id = current_order.id AND orders.driver_id = user_id;

    RETURN QUERY SELECT * FROM admin.orders_view WHERE id = current_order.id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.stats()
RETURNS SETOF admin.drivers_stat_view
SECURITY DEFINER
SET search_path = private, admin, workers, public
AS $$
DECLARE
    user_id BIGINT := public.get_current_user_from_session();
BEGIN
    IF user_id IS NULL THEN
        RAISE EXCEPTION 'User not found';
    END IF;

    RETURN QUERY
        SELECT *
        FROM admin.drivers_stat_view
        WHERE id = user_id;
END;
$$ LANGUAGE plpgsql;
