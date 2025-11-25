CREATE OR REPLACE FUNCTION UpdateCarStatusOnDriver()
RETURNS TRIGGER AS $$
DECLARE
    busy_status_id BIGINT;
    available_status_id BIGINT;
BEGIN

    busy_status_id := (SELECT id FROM car_statuses WHERE name = 'Busy');
    available_status_id := (SELECT id FROM car_statuses WHERE name = 'Available');

    IF (NEW.driver_id IS NOT NULL AND OLD.driver_id IS NULL) THEN
        UPDATE cars SET status_id = busy_status_id
        WHERE id = NEW.id;
    END IF;

    IF (NEW.driver_id is NULL AND OLD.driver_id IS NOT NULL) THEN
        UPDATE cars SET status_id = available_status_id
        WHERE id = NEW.id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER UpdateCarStatusOnDriverTrigger
AFTER UPDATE ON cars FOR EACH ROW
EXECUTE PROCEDURE UpdateCarStatusOnDriver();