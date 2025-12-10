-- Роли

CREATE ROLE "guest_role";
CREATE ROLE "user_role";
CREATE ROLE "driver_role";
CREATE ROLE "admin_role";

-- ПОльзователи

CREATE USER "vluki" WITH PASSWORD '1234';
CREATE USER "aklatch" WITH PASSWORD '1234';
CREATE USER "mbombini" WITH PASSWORD '1234';
CREATE USER "nagent" WITH PASSWORD '1234';

-- Выдача прав

GRANT "guest_role" TO "vluki";
GRANT "user_role" TO "aklatch";
GRANT "driver_role" TO "mbombini";
GRANT "admin_role" TO "nagent";

-- Права

