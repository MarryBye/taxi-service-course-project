CREATE OR REPLACE FUNCTION check_email(email TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (email ~* '^[\w\.-]+@[\w\.-]+\.\w+$');
END;
$$ LANGUAGE plpgsql;