CREATE OR REPLACE VIEW users_view AS
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
    c.driver_id
FROM cars AS c;

CREATE OR REPLACE VIEW drivers_view AS
SELECT
    u.*,
    b.balance AS earning_balance,
    c.id AS car_id
FROM users_view AS u
LEFT JOIN cars AS c ON c.driver_id = u.id
LEFT JOIN balances AS b ON u.id = b.user_id AND b.balance_type = 'earning'
WHERE u.role = 'driver';

CREATE OR REPLACE VIEW admins_view AS
SELECT
    u.*
FROM users_view AS u
LEFT JOIN balances AS b ON u.id = b.user_id AND b.balance_type = 'payment'
WHERE u.role = 'admin';

CREATE OR REPLACE VIEW orders_view AS
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

CREATE OR REPLACE VIEW maintenance_view AS
SELECT
    *
FROM maintenances;

CREATE OR REPLACE VIEW transactions_view AS
SELECT
    t.id,
    t.amount,
    t.transaction_type,
    t.balance_type,
    t.created_at,
    t.user_id,
    t.order_id,
    t.payment_method
FROM transactions AS t;