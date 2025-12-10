-- Active: 1764877667177@@127.0.0.1@5432@taxi_db
CREATE OR REPLACE VIEW users_view AS
SELECT
    u.id,
    u.email,
    u.tel_number,
    u.first_name,
    u.last_name,
    u.country,
    u.city,
    u.role,
    u.created_at,
    u.changed_at,
    b.balance AS payment_balance
FROM users AS u
LEFT JOIN balances AS b ON u.id = b.user_id AND b.balance_type = 'payment';

CREATE OR REPLACE VIEW cars_view AS
SELECT
    c.id AS id,
    c.mark,
    c.model,
    c.car_number,
    c.country,
    c.city,
    c.color,
    c.car_class,
    c.car_status,
    c.created_at,
    c.changed_at,

    json_build_object(
        'id', u.id,
        'email', u.email,
        'tel_number', u.tel_number,
        'first_name', u.first_name,
        'last_name', u.last_name,
        'country', u.country,
        'city', u.city,
        'role', u.role,
        'created_at', u.created_at,
        'changed_at', u.changed_at
    ) AS driver

FROM cars AS c
LEFT JOIN users AS u ON c.driver_id = u.id;

CREATE OR REPLACE VIEW drivers_view AS
SELECT
    u.id,
    u.login,
    u.first_name,
    u.last_name,
    u.email,
    u.tel_number,
    u.country,
    u.city,
    u.role,
    u.created_at,
    u.changed_at,
    b.balance AS earning_balance,

    json_build_object(
        'id', c.id,
        'mark', c.mark,
        'model', c.model,
        'car_number', c.car_number,
        'car_class', c.car_class,
        'car_status', c.car_status,
        'country', c.country,
        'city', c.city,
        'color', c.color,
        'created_at', c.created_at,
        'changed_at', c.changed_at
    ) AS car
FROM users AS u
LEFT JOIN cars AS c ON c.driver_id = u.id
LEFT JOIN balances AS b ON u.id = b.user_id AND b.balance_type = 'earning'
WHERE u.role = 'driver';

CREATE OR REPLACE VIEW orders_view AS
SELECT
    o.id,
   json_build_object(
        'id', client.id,
        'email', client.email,
        'tel_number', client.tel_number,
        'first_name', client.first_name,
        'last_name', client.last_name,
        'country', client.country,
        'city', client.city,
        'role', client.role,
        'created_at', client.created_at,
        'changed_at', client.changed_at
    ) AS client,
    json_build_object(
        'id', driver.id,
        'email', driver.email,
        'tel_number', driver.tel_number,
        'first_name', driver.first_name,
        'last_name', driver.last_name,
        'country', driver.country,
        'city', driver.city,
        'role', driver.role,
        'created_at', driver.created_at,
        'changed_at', driver.changed_at
    ) AS driver,
    json_build_object(
        'id', orat_client.id,
        'mark', orat_client.mark,
        'comment', orat_client.comment,
        'created_at', orat_client.created_at,
        'changed_at', orat_client.changed_at
    ) AS client_rating,
    
    json_build_object(
        'id', orat_driver.id,
        'mark', orat_driver.mark,
        'comment', orat_driver.comment,
        'created_at', orat_driver.created_at,
        'changed_at', orat_driver.changed_at
    ) AS driver_rating,
    json_build_object(
        'id', ocan.id,
        'canceled_by', ocan.canceled_by,
        'comment', ocan.comment,
        'created_at', ocan.created_at,
        'changed_at', ocan.changed_at
    ) AS cancel_info,
    json_build_object(
        'id', t.id,
        'balance_type', t.balance_type,
        'transaction_type', t.transaction_type,
        'payment_method', t.payment_method,
        'amount', t.amount,
        'created_at', t.created_at
    ) AS transaction_info,
    json_build_object(
        'id', r.id,
        'start_location', r.start_location,
        'end_location', r.end_location,
        'distance', r.distance
    ) AS route_info,
    o.status,
    o.finished_at,
    o.created_at,
    o.changed_at
FROM orders AS o
JOIN users AS client ON o.client_id = client.id
LEFT JOIN users AS driver ON o.driver_id = driver.id
LEFT JOIN order_ratings AS orat_client ON 
    o.id = orat_client.order_id AND orat_client.mark_by = o.client_id
LEFT JOIN order_ratings AS orat_driver ON 
    o.id = orat_driver.order_id AND orat_driver.mark_by = o.driver_id
LEFT JOIN order_cancels AS ocan ON 
    o.id = ocan.order_id
JOIN transactions AS t ON o.id = t.order_id AND t.user_id = o.client_id
JOIN routes AS r ON o.id = r.order_id;

CREATE OR REPLACE VIEW routes_view AS
SELECT
    r.id,
    r.start_location,
    r.end_location,
    r.distance,
    json_agg(
        json_build_object(
            'position_index', rp.position_index,
            'location', rp.location
        ) ORDER BY rp.position_index
    ) AS route_points
FROM routes AS r
JOIN route_points AS rp ON r.id = rp.route_id
GROUP BY r.id, r.start_location, r.end_location, r.distance;

CREATE OR REPLACE VIEW transactions_view AS
SELECT
    t.id,
    t.user_id,
    json_build_object(
        'id', u.id,
        'email', u.tel_number,
        'first_name', u.first_name,
        'last_name', u.last_name,
        'country', u.country,
        'city', u.city,
        'role', u.role,
        'created_at', u.created_at,
        'changed_at', u.changed_at
    ) AS user_account,
    t.balance_type,
    t.transaction_type,
    t.payment_method,
    t.amount,
    t.created_at
FROM transactions AS t
JOIN users AS u ON t.user_id = u.id;

CREATE OR REPLACE VIEW maintenances_view AS
SELECT
    m.id,
    json_build_object(
        'id', manager.id,
        'email', manager.email,
        'tel_number', manager.tel_number,
        'first_name', manager.first_name,
        'last_name', manager.last_name,
        'country', manager.country,
        'city', manager.city,
        'role', manager.role,
        'created_at', manager.created_at,
        'changed_at', manager.changed_at
    ) AS manager,
    json_build_object(
        'id', c.id,
        'mark', c.mark,
        'model', c.model,
        'car_number', c.car_number,
        'car_class', c.car_class,
        'car_status', c.car_status,
        'country', c.country,
        'city', c.city,
        'color', c.color,
        'created_at', c.created_at,
        'changed_at', c.changed_at
    ) AS car,
    m.description,
    m.cost,
    m.status,
    m.maintenance_start,
    m.maintenance_end,
    m.created_at,
    m.changed_at
FROM maintenances AS m
JOIN users AS manager ON m.manager_id = manager.id
JOIN cars AS c ON m.car_id = c.id;