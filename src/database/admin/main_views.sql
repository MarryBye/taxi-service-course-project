CREATE OR REPLACE VIEW admin.users_view AS
SELECT
    u.id,
    u.email,
    u.tel_number,
    u.first_name,
    u.last_name,
    u.country,
    u.role,
    u.city,
    u.created_at,
    u.changed_at
FROM private.users AS u;

CREATE OR REPLACE VIEW admin.clients_view AS
SELECT
    u.*,
    b.balance AS earning_balance
FROM admin.users_view AS u
LEFT JOIN private.balances AS b ON u.id = b.user_id AND b.balance_type = 'payment';

CREATE OR REPLACE VIEW admin.drivers_view AS
SELECT
    u.*,
    b_e.balance AS earning_balance,
    b_p.balance AS payment_balance,
    c.id AS car_id
FROM admin.users_view AS u
LEFT JOIN private.cars AS c ON c.driver_id = u.id
LEFT JOIN private.balances AS b_e ON u.id = b_e.user_id AND b_e.balance_type = 'earning'
LEFT JOIN private.balances AS b_p ON u.id = b_p.user_id AND b_p.balance_type = 'payment'
WHERE u.role = 'driver';

CREATE OR REPLACE VIEW admin.admins_view AS
SELECT
    u.*
FROM admin.users_view AS u
LEFT JOIN private.balances AS b ON u.id = b.user_id AND b.balance_type = 'payment'
WHERE u.role = 'admin';

CREATE OR REPLACE VIEW admin.cars_view AS
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
    c.driver_id
FROM private.cars AS c;

CREATE OR REPLACE VIEW admin.orders_view AS
SELECT
    o.id,
    o.order_class,
    o.status,
    o.finished_at,
    o.created_at,
    o.changed_at,
    o.client_id,
    o.driver_id,
    orat_client.id AS client_rating_id,
    orat_driver.id AS driver_rating_id,
    ocan.id AS cancel_id,
    t.id AS transaction_id,
    r.id AS route_id
FROM private.orders AS o
JOIN private.users AS client ON o.client_id = client.id
LEFT JOIN private.users AS driver ON o.driver_id = driver.id
LEFT JOIN private.order_ratings AS orat_client ON
    o.id = orat_client.order_id AND orat_client.mark_by = o.client_id
LEFT JOIN private.order_ratings AS orat_driver ON
    o.id = orat_driver.order_id AND orat_driver.mark_by = o.driver_id
LEFT JOIN private.order_cancels AS ocan ON
    o.id = ocan.order_id
JOIN private.transactions AS t ON o.id = t.order_id AND t.user_id = o.client_id
JOIN private.routes AS r ON o.id = r.order_id;

CREATE OR REPLACE VIEW admin.maintenance_view AS
SELECT
    *
FROM private.maintenances;

CREATE OR REPLACE VIEW admin.transactions_view AS
SELECT
    t.id,
    t.amount,
    t.transaction_type,
    t.balance_type,
    t.created_at,
    t.user_id,
    t.order_id,
    t.payment_method
FROM private.transactions AS t;