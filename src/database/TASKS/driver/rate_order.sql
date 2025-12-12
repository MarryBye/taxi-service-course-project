CREATE OR REPLACE PROCEDURE driver_schema.rate_order(
    p_order_id BIGINT,
    p_driver_id BIGINT,
    p_mark NUMERIC,
    p_tag client_tags,
    p_comment VARCHAR
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    INSERT INTO order_ratings(order_id, mark_by, mark, comment)
    VALUES (p_order_id, p_driver_id, p_mark, p_comment);

    INSERT INTO order_client_tags(order_id, tag)
    SELECT p_order_id, p_tag;
END;
$$;
