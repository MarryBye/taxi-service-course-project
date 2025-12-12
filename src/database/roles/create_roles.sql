-- БД

CREATE DATABASE "taxi_service";

-- Роли

CREATE ROLE "guest";
CREATE ROLE "client";
CREATE ROLE "driver";
CREATE ROLE "admin" WITH CREATEROLE;
CREATE ROLE "superadmin" WITH CREATEROLE;

GRANT "driver" TO "admin" WITH ADMIN OPTION;
GRANT "client" TO "admin" WITH ADMIN OPTION;
GRANT "admin" TO "postgres" WITH ADMIN OPTION;
GRANT "admin" TO "superadmin" WITH ADMIN OPTION;

-- Технический пользователь

CREATE USER guest_account WITH PASSWORD 'guest_account';

-- Выдача прав тех. пользователю

GRANT "guest" TO "guest_account";
GRANT "superadmin" TO "postgres";

-- Выдача доступов для ролей

GRANT EXECUTE ON FUNCTION
    list_users,
    get_user,
    create_user,
    delete_user,
    update_user,
    list_drivers,
    get_driver,
    create_driver,
    update_driver,
    delete_driver,
    list_admins,
    get_admin,
    create_admin,
    delete_admin,
    update_admin,
    list_orders,
    get_order,
    create_order,
    update_order,
    delete_order,
    list_cars,
    get_car,
    create_car,
    update_car,
    delete_car,
    list_maintenances,
    get_maintenance,
    create_maintenance,
    update_maintenance,
    delete_maintenance,
    create_transaction,
    list_transactions,
    get_transaction
TO "admin";

GRANT EXECUTE ON PROCEDURE
    assign_role
TO "admin";

GRANT EXECUTE ON FUNCTION
    get_profile,
    update_profile,
    delete_profile
    -- make_order,
    -- cancel_order,
    -- get_order_now,
    -- get_order_history,
    -- rate_order
TO "client";

-- GRANT EXECUTE ON FUNCTION
--     get_driver_profile,
--     update_profile,
--     accept_order,
--     cancel_order,
--     finish_order,
--     get_order_now,
--     get_order_history,
--     list_acceptable_orders,
--     rate_order
-- TO "driver"

GRANT SELECT ON users_view, drivers_view, admins_view, cars_view, transactions_view, maintenance_view TO admin;
GRANT SELECT, INSERT, UPDATE, DELETE ON users, orders, maintenances, cars TO admin;
GRANT SELECT, INSERT ON transactions, routes, route_points TO admin;
GRANT SELECT, INSERT ON balances TO admin;

CALL assign_role('TestUser546', 'client');
SELECT * FROM get_role('TestUser');

SELECT *
FROM pg_roles
WHERE rolname = 'TestUser546' AND rolcanlogin = true;