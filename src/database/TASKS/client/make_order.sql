CREATE OR REPLACE PROCEDURE make_order(
    client_id BIGINT,
    price NUMERIC,
    payment_method payment_methods,
    order_class car_classes,
    addresses address[]
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    new_order_id BIGINT;
    new_route_id BIGINT;
    addr address;
    idx INT := 0;
BEGIN
    -- 1. Создать заказ
    INSERT INTO orders(client_id, status, order_class)
    VALUES (client_id, 'searching_for_driver', order_class)
    RETURNING id INTO new_order_id;

    -- 2. Создать маршрут (первый и последний адрес)
    INSERT INTO routes(order_id, start_location, end_location, distance)
    VALUES (
        new_order_id,
        addresses[1],
        addresses[array_length(addresses,1)],
        0 -- расстояние можно рассчитывать отдельно
    )
    RETURNING id INTO new_route_id;

    -- 3. Создать точки маршрута
    FOREACH addr IN ARRAY addresses LOOP
        INSERT INTO route_points(route_id, position_index, location)
        VALUES (new_route_id, idx, addr);
        idx := idx + 1;
    END LOOP;

    -- 4. Создать транзакцию (платёж)
    INSERT INTO transactions(user_id, balance_type, transaction_type, payment_method, amount, order_id)
    VALUES (client_id, 'payment', 'debit', payment_method, price, new_order_id);

END;
$$;
