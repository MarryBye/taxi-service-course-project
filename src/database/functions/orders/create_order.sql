-- Active: 1764877667177@@127.0.0.1@5432@taxi_db@public
CREATE OR REPLACE FUNCTION create_order(
    par_client_id BIGINT,
    par_car_class car_classes,
    par_payment_method payment_methods,
    par_addresses address[],
    par_amount NUMERIC
) RETURNS SETOF orders_view AS $$
DECLARE
    created_order_id BIGINT;
    created_route_id BIGINT;
BEGIN

    -- Створення замовлення

    INSERT INTO orders (
        client_id
    )
    VALUES (
        par_client_id
    )
    RETURNING id INTO created_order_id;

    -- Створення транзакції для замовлення

    INSERT INTO transactions (
        user_id,
        balance_type,
        transaction_type,
        payment_method,
        amount,
        order_id
    ) VALUES 
        (par_client_id, 'payment', 'credit', par_payment_method, par_amount, created_order_id);

    -- Створення запису routes зі шляхом поїздки

    INSERT INTO routes (
        order_id,
        start_location,
        end_location,
        distance
    ) VALUES (
        created_order_id, par_addresses[1], par_addresses[array_length(par_addresses, 1)], 0
    ) RETURNING id INTO created_route_id;

    -- Створення записів route_points 
    FOR i IN 1..array_length(par_addresses, 1) LOOP
        INSERT INTO route_points (
            route_id,
            position_index,
            location
        ) VALUES (
            created_route_id, i - 1, par_addresses[i]
        );
    END LOOP;

    RETURN QUERY 
    SELECT * FROM orders_view WHERE id = created_order_id;
END;
$$ LANGUAGE plpgsql;

SELECT * FROM create_order(
    3,
    'standard',
    'credit_card',
    ARRAY[
        ROW('Ukraine', 'Kyiv', 'Shevchenko Blvd', 10, 50.4501, 30.5234)::address,
        ROW('Ukraine', 'Kyiv', 'Khreshchatyk St', 10, 50.4505, 30.5250)::address,
        ROW('Ukraine', 'Kyiv', 'Podil St', 5, 50.4477, 30.5220)::address
    ],
    150.00
);