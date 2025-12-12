CREATE OR REPLACE PROCEDURE cancel_order(
    p_order_id BIGINT,
    p_client_id BIGINT,
    p_tag driver_tags,
    p_comment VARCHAR
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO order_cancels(order_id, canceled_by, comment)
    VALUES (p_order_id, p_client_id, p_comment);

    INSERT INTO order_driver_tags(order_id, tag)
    VALUES (p_order_id, p_tag);

    UPDATE orders
    SET status = 'canceled'
    WHERE id = p_order_id;
END;
$$;