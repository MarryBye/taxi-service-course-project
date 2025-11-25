CREATE OR REPLACE FUNCTION check_car_number(car_number TEXT) RETURNS BOOLEAN AS $$
BEGIN
  RETURN (car_number ~* '^[A-Z]{2}\d{4}[A-Z]{2}$');
END;
$$ LANGUAGE plpgsql;