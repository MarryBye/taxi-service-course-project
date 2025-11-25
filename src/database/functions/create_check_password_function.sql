CREATE OR REPLACE FUNCTION check_password(password TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (password ~* '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!*?#&])[A-Za-z\d@$!*?&]{8,}$');
END;
$$ LANGUAGE plpgsql;