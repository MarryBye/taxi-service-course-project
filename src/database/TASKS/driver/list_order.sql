CREATE OR REPLACE FUNCTION driver_schema.list_acceptable_orders(
    p_driver_id BIGINT
)
RETURNS SETOF orders_view SECURITY DEFINER AS $$
DECLARE
    driver_data users%ROWTYPE;
BEGIN
    SELECT * INTO driver_data
    FROM users
    WHERE id = p_driver_id;

    RETURN QUERY
        SELECT o.*
        FROM orders_view AS o
        JOIN users AS c ON o.client_id = c.id
        JOIN cars AS cr ON cr.driver_id = p_driver_id
        WHERE o.driver_id IS NULL
          AND o.order_class = cr.car_class
          AND o.status = 'searching_for_driver'
          AND c.city = driver_data.city
          AND c.country = driver_data.country;
END;
$$ LANGUAGE plpgsql
