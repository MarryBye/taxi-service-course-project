-- Update order status on:
-- 1. On cancel change status
-- 2. On finish create ratings
-- 3.

CREATE OR REPLACE FUNCTION update_car_status_on_driver() RETURNS trigger AS $$
DECLARE
    car_on_maintenance BOOLEAN;
BEGIN
    car_on_maintenance := is_car_on_maintenance(NEW.id);
    IF (NOT car_on_maintenance) THEN
        IF (OLD.driver_id IS DISTINCT FROM NEW.driver_id AND NOT NEW.driver_id IS NULL) THEN
            NEW.status := 'busy';
        END IF;
        IF (OLD.driver_id IS DISTINCT FROM NEW.driver_id AND NEW.driver_id IS NULL) THEN
            NEW.status := 'available';
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_car_status_on_driver_trigger
AFTER UPDATE ON cars
FOR EACH ROW EXECUTE PROCEDURE update_car_status_on_driver();