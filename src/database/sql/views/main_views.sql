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
    c.id AS car_id,
    c.mark AS car_mark,
    c.model AS car_model,
    c.car_number AS car_number,
    c.class AS car_class,
    c.status AS car_status,
    c.created_at AS car_created_at,

    u.id AS driver_id,
    u.first_name AS driver_first_name,
    u.last_name AS driver_last_name,
    u.email AS driver_email,
    u.tel_number AS driver_tel_number,
    u.created_at AS driver_created_at,
    u.role AS driver_role
FROM cars AS c
LEFT JOIN users AS u ON c.driver_id = u.id;

CREATE OR REPLACE VIEW drivers_view AS
SELECT
    u.id AS driver_id,
    u.first_name AS driver_first_name,
    u.last_name AS driver_last_name,
    u.email AS driver_email,
    u.tel_number AS driver_tel_number,
    u.created_at AS driver_created_at,

    c.id AS car_id,
    c.mark AS car_mark,
    c.model AS car_model,
    c.car_number AS car_number,
    c.class AS car_class,
    c.status AS car_status,
    c.created_at AS car_created_at
FROM users AS u
LEFT JOIN cars AS c ON u.id = c.driver_id
WHERE u.role = 'driver';

CREATE OR REPLACE VIEW staff_view AS
SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.email,
    u.tel_number,
    u.created_at
FROM users AS u
WHERE u.role IN ('admin', 'manager');

CREATE OR REPLACE VIEW orders_view AS
SELECT
    o.id AS order_id,
    o.status AS order_status,
    o.finished_at AS order_finished_at,
    o.created_at AS order_created_at,

    o.client_id AS order_client_id,
    c.first_name AS client_first_name,
    c.last_name AS client_last_name,
    c.email AS client_email,
    c.tel_number AS client_tel_number,
    c.created_at AS client_created_at,
    orat_client.mark AS client_rating,
    orat_client.comment AS client_comment,
    orat_client.created_at AS client_rating_created_at,

    o.driver_id AS order_driver_id,
    d.first_name AS driver_first_name,
    d.last_name AS driver_last_name,
    d.email AS driver_email,
    d.tel_number AS driver_tel_number,
    d.created_at AS driver_created_at,
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
