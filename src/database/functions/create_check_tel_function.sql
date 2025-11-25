CREATE OR REPLACE FUNCTION check_tel(tel_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (tel_number ~* '^\+\d{1,3}-\d{3}-\d{3}-\d{2}-\d{2}$');
END;
$$ LANGUAGE plpgsql;