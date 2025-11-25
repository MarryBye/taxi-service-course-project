CREATE OR REPLACE FUNCTION check_license_number(license_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (license_number ~* '^[A-Z0-9]{8}$');
END;
$$ LANGUAGE plpgsql;