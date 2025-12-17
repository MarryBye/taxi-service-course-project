CREATE OR REPLACE VIEW users AS
SELECT id, role, login FROM private.users;