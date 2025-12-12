CREATE OR REPLACE PROCEDURE driver_schema.cancel_order(
    p_driver_id BIGINT,
    p_order_id BIGINT,
    p_comment VARCHAR,
    p_client_tag client_tags
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    UPDATE orders
    SET status = 'canceled', finished_at = NOW()
    WHERE id = p_order_id;

    INSERT INTO order_cancels(order_id, canceled_by, comment)
    VALUES (p_order_id, p_driver_id, p_comment);

    INSERT INTO order_client_tags(order_id, tag)
    SELECT p_order_id, p_client_tag;
END;
$$;
