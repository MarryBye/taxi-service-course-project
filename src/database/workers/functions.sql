CREATE OR REPLACE FUNCTION workers.get_current_order()
RETURNS admin.orders_view SECURITY DEFINER AS $$
DECLARE
    result admin.orders_view;
    p_driver_id BIGINT;
BEGIN
    p_driver_id := public.get_current_user();
    SELECT * INTO result FROM admin.orders_view AS ov
    WHERE ov.driver_id = p_driver_id AND
          ov.status != 'canceled' AND
          ov.status != 'completed'
    ORDER BY ov.created_at DESC
    LIMIT 1;

    RETURN result;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.get_acceptable_orders() RETURNS SETOF admin.orders_view SECURITY DEFINER AS $$
DECLARE
    p_driver_id BIGINT;
    has_current_order BOOLEAN;
BEGIN
    p_driver_id := public.get_current_user();
    has_current_order := (SELECT id FROM workers.get_current_order()) IS NOT NULL;
    IF (has_current_order) THEN
        RAISE EXCEPTION 'You have an active order';
    END IF;
    RETURN QUERY
        SELECT o.* FROM private.orders AS o
        JOIN private.users AS u ON o.client_id = u.id
        JOIN private.cars AS c ON c.driver_id = p_driver_id
        JOIN private.users AS d ON d.id = p_driver_id
        WHERE o.driver_id IS NULL AND
              o.client_id != p_driver_id AND
              o.status = 'searching_for_driver' AND
              u.country = d.country AND
              u.city = d.city AND
              o.order_class = c.car_class
        ORDER BY o.created_at;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE workers.accept_order(
    p_order_id BIGINT
) SECURITY DEFINER AS $$
DECLARE
    p_driver_id BIGINT;
    has_current_order BOOLEAN;
BEGIN
    p_driver_id := public.get_current_user();
    has_current_order := (SELECT id FROM workers.get_current_order()) IS NOT NULL;
    IF (has_current_order) THEN
        RAISE EXCEPTION 'You have an active order';
    END IF;
    UPDATE private.orders SET driver_id = p_driver_id, status = 'waiting_for_driver'
    WHERE id = p_order_id AND
          driver_id IS NULL;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE workers.submit_arriving_time() SECURITY DEFINER AS $$
DECLARE
    current_order admin.orders_view%ROWTYPE;
BEGIN
    current_order := workers.get_current_order();
    IF current_order.id IS NULL THEN
        RAISE EXCEPTION 'You have no active order';
    END IF;
    UPDATE private.orders SET status = 'waiting_for_client' WHERE id = current_order.id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE workers.cancel_order(
    p_comment VARCHAR(256),
    p_client_tags public.client_cancel_tags[]
) SECURITY DEFINER AS $$
DECLARE
    p_driver_id BIGINT;
    current_order admin.orders_view%ROWTYPE;
    tag public.client_cancel_tags;
BEGIN
    p_driver_id := public.get_current_user();
    current_order := workers.get_current_order();
    IF (current_order.id IS NULL) THEN
        RAISE EXCEPTION 'You have no active order';
    END IF;
    UPDATE private.orders SET status = 'canceled' WHERE id = current_order.id;
    INSERT INTO private.order_cancels
        (order_id, canceled_by, comment)
    VALUES
        (current_order.id, p_driver_id, p_comment);
    FOREACH tag IN ARRAY p_client_tags LOOP
        INSERT INTO private.order_client_tags
            (order_id, tag)
        VALUES
            (current_order.id, tag);
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE workers.rate_order_by_driver(
    p_mark INT,
    p_comment VARCHAR(256),
    p_client_tags public.client_tags[]
) SECURITY DEFINER AS $$
DECLARE
    p_driver_id BIGINT;
    current_order admin.orders_view%ROWTYPE;
    is_waiting_for_mark BOOLEAN;
    tag public.client_tags;
BEGIN
    p_driver_id := public.get_current_user();
    current_order := workers.get_current_order();
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
        (current_order.id, p_driver_id, p_mark, p_comment);
    FOREACH tag IN ARRAY p_client_tags LOOP
        INSERT INTO private.order_client_tags
            (order_id, tag)
        VALUES
            (current_order.id, tag);
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE workers.complete_order() SECURITY DEFINER AS $$
DECLARE
    p_driver_id BIGINT;
    current_order admin.orders_view%ROWTYPE;
BEGIN
    p_driver_id := public.get_current_user();
    current_order := workers.get_current_order();
    IF (current_order.id IS NULL) THEN
        RAISE EXCEPTION 'You have no active order';
    END IF;
    UPDATE private.orders SET status = 'waiting_for_mark' WHERE id = current_order.id;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.get_driver_history() RETURNS SETOF admin.orders_view SECURITY DEFINER AS $$
DECLARE
    p_driver_id BIGINT;
BEGIN
    p_driver_id := public.get_current_user();
    RETURN QUERY
        SELECT * FROM admin.orders_view
        WHERE driver_id = p_driver_id
        ORDER BY created_at DESC;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION workers.get_own_stats() RETURNS admin.drivers_view SECURITY DEFINER AS $$
DECLARE
    p_driver_id BIGINT;
    result admin.drivers_view;
BEGIN
    p_driver_id := public.get_current_user();
    result := (SELECT * FROM admin.drivers_view WHERE id = p_driver_id);
    RETURN result;
END;
$$ LANGUAGE plpgsql;