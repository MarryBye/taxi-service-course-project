-- Active: 1764877667177@@127.0.0.1@5432@TaxiDBProject@public
CREATE OR REPLACE FUNCTION check_car_number(car_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (car_number ~* '^[A-Z]{2}\d{4}[A-Z]{2}$');
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_email(email TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (email ~* '^[\w\.-]+@[\w\.-]+\.\w+$');
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_license_number(license_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (license_number ~* '^[A-Z0-9]{8}$');
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_tel(tel_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (tel_number ~* '^\+\d{1,3}-\d{3}-\d{3}-\d{2}-\d{2}$');
END;
$$ LANGUAGE plpgsql;