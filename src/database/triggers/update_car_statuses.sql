-- Update car status on 3 events:
-- 1. Driver gets assigned to a car
-- 2. Driver gets unassigned from a car
-- 3. Car gets on maintenance

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
    NEW.changed_at := NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_car_status_on_driver_trigger
AFTER UPDATE ON cars
FOR EACH ROW EXECUTE PROCEDURE update_car_status_on_driver();

CREATE OR REPLACE FUNCTION update_car_status_on_maintenance() RETURNS trigger AS $$
BEGIN
    UPDATE cars SET status = 'on_maintenance' WHERE id = NEW.car_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_car_status_on_maintenance_trigger
AFTER INSERT ON maintenances
FOR EACH ROW EXECUTE PROCEDURE update_car_status_on_maintenance();

CREATE OR REPLACE FUNCTION update_car_status_on_maintenance_finish() RETURNS trigger AS $$
DECLARE
    car_has_driver BOOLEAN;
BEGIN
    car_has_driver := is_car_has_driver(NEW.car_id);
    IF (NEW.maintenance_status IS DISTINCT FROM OLD.maintenance_status AND NEW.maintenance_status = 'completed') THEN
        IF (car_has_driver) THEN
            UPDATE cars SET status = 'busy' WHERE id = NEW.car_id;
        ELSIF (NOT car_has_driver) THEN
            UPDATE cars SET status = 'available' WHERE id = NEW.car_id;
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_car_status_on_maintenance_finish_trigger
AFTER UPDATE ON maintenances
FOR EACH ROW EXECUTE PROCEDURE update_car_status_on_maintenance_finish();