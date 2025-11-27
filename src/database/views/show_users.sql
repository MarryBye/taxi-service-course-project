CREATE OR REPLACE VIEW show_users AS
SELECT
    u.id,
    u.first_name,
    u.last_name,
    u.email,
    u.tel_number,
    u.created_at,
    u.role
FROM users AS u;