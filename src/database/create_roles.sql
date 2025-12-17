-- БД

CREATE DATABASE "taxi_service";

-- Роли
CREATE ROLE "guest"         NOLOGIN;
CREATE ROLE "client"        NOLOGIN;
CREATE ROLE "driver"        NOLOGIN;
CREATE ROLE "admin"         NOLOGIN CREATEROLE;

GRANT "client" TO "admin" WITH ADMIN OPTION;
GRANT "driver" TO "admin" WITH ADMIN OPTION;

-- Схемы

CREATE SCHEMA "private" AUTHORIZATION "db_owner";
CREATE SCHEMA "admin" AUTHORIZATION "db_owner";
CREATE SCHEMA "authorized" AUTHORIZATION "db_owner";
CREATE SCHEMA "workers" AUTHORIZATION "db_owner";

REVOKE ALL ON SCHEMA "private" FROM PUBLIC;
REVOKE ALL ON SCHEMA "admin" FROM PUBLIC;
REVOKE ALL ON SCHEMA "authorized" FROM PUBLIC;
REVOKE ALL ON SCHEMA "workers" FROM PUBLIC;

GRANT USAGE ON SCHEMA "admin"       TO "admin";
GRANT USAGE ON SCHEMA "authorized"  TO "admin", "client", "driver";
GRANT USAGE ON SCHEMA "workers"     TO "admin", "driver";

GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA "admin" TO "admin";
GRANT EXECUTE ON ALL PROCEDURES IN SCHEMA "admin" TO "admin";
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA "authorized" TO "admin", "client", "driver";
GRANT EXECUTE ON ALL PROCEDURES IN SCHEMA "authorized" TO "admin", "client", "driver";
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA "workers" TO "admin", "driver";
GRANT EXECUTE ON ALL PROCEDURES IN SCHEMA "workers" TO "admin", "driver";

GRANT SELECT ON TABLE
    admin.users_view,
    admin.drivers_view,
    admin.admins_view,
    admin.cars_view,
    admin.orders_view,
    admin.transactions_view,
    admin.maintenance_view
TO "admin";

GRANT SELECT ON TABLE
    public.users
TO "admin", "client", "driver", "guest";

-- Технический пользователь

CREATE USER "guest_account" WITH PASSWORD 'guest_account';
GRANT "guest" TO guest_account;

