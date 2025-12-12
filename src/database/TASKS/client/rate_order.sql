CREATE OR REPLACE PROCEDURE rate_order(
    p_order_id BIGINT,
    p_client_id BIGINT,
    p_mark NUMERIC,
    p_tag driver_tags,
    p_comment VARCHAR
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO order_ratings(order_id, mark_by, mark, comment)
    VALUES (p_order_id, p_client_id, p_mark, p_comment);

    INSERT INTO order_driver_tags(order_id, tag)
    VALUES (p_order_id, p_tag);
END;
$$;