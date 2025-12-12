CREATE OR REPLACE FUNCTION check_car_number(car_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (car_number IS NOT NULL);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_email(email TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (email ~* '^[\w\.-]+@[\w\.-]+\.\w+$');
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_license_number(license_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN license_number IS NOT NULL;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_tel(tel_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN tel_number IS NOT NULL;
END;
$$ LANGUAGE plpgsql;