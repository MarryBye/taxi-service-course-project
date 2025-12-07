-- Active: 1764877667177@@127.0.0.1@5432@taxi_db
CREATE OR REPLACE VIEW users_view AS
SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.email,
    u.tel_number,
    u.created_at,
    u.role
FROM users AS u;

CREATE OR REPLACE VIEW cars_view AS
SELECT
    c.id AS id,
    c.mark AS mark,
    c.model AS model,
    c.car_number AS car_number,
    c.class AS car_class,
    c.status AS car_status,
    c.created_at AS created_at,

    CASE
        WHEN u.id IS NULL THEN NULL
    ELSE
        json_build_object(
            'id', u.id,
            'first_name', u.first_name,
            'last_name', u.last_name,
            'email', u.email,
            'tel_number', u.tel_number,
            'created_at', u.created_at,
            'role', u.role
        )
    END AS driver
        
FROM cars AS c
LEFT JOIN users_view AS u ON c.driver_id = u.id;

CREATE OR REPLACE VIEW drivers_view AS
SELECT
    u.*,
    CASE
        WHEN c.id IS NULL THEN NULL
    ELSE
        json_build_object(
            'id', c.id,
            'mark', c.mark,
            'model', c.model,
            'car_number', c.car_number,
            'car_class', c.class,
            'car_status', c.status,
            'created_at', c.created_at
        ) 
    END AS car
FROM users_view AS u
LEFT JOIN cars AS c ON c.driver_id = u.id;

CREATE OR REPLACE VIEW orders_view AS
SELECT
    o.id,
    o.status,
    o.finished_at,
    o.created_at,

    CASE
        WHEN c.id IS NULL THEN NULL
    ELSE
        json_build_object(
            'id', c.id,
            'first_name', c.first_name,
            'last_name', c.last_name,
            'email', c.email,
            'tel_number', c.tel_number,
            'created_at', c.created_at,
            'role', c.role
        )
    END AS client,

    CASE
        WHEN d.id IS NULL THEN NULL
    ELSE
        json_build_object(
            'id', d.id,
            'first_name', d.first_name,
            'last_name', d.last_name,
            'email', d.email,
            'tel_number', d.tel_number,
            'created_at', d.created_at,
            'role', d.role
        )
    END AS driver,

    orat_client.mark AS client_rating,
    orat_client.comment AS client_comment,
    orat_client.created_at AS client_rating_created_at,

    orat_driver.mark AS driver_rating,
    orat_driver.comment AS driver_comment,
    orat_driver.created_at AS driver_rating_created_at,

    ocan.canceled_by AS order_canceled_by,
    ocan.comment AS order_cancel_comment

FROM orders AS o
JOIN users AS c ON o.client_id = c.id
LEFT JOIN users AS d ON o.driver_id = d.id
LEFT JOIN order_ratings AS orat_client ON 
    o.id = orat_client.order_id AND orat_client.mark_by = o.client_id
LEFT JOIN order_ratings AS orat_driver ON 
    o.id = orat_driver.order_id AND orat_driver.mark_by = o.driver_id
LEFT JOIN order_cancels AS ocan ON 
    o.id = ocan.order_id;
