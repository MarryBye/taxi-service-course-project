CREATE OR REPLACE FUNCTION UpdateCarStatus()
RETURNS TRIGGER AS $$
DECLARE
    on_maintenance_status_id BIGINT;
BEGIN

    on_maintenance_status_id := (SELECT id FROM car_statuses WHERE name = 'On maintenance');

    UPDATE cars SET status_id = on_maintenance_status_id
    WHERE id = NEW.car_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER UpdateCarStatusTrigger
AFTER INSERT ON maintenances FOR EACH ROW
EXECUTE PROCEDURE UpdateCarStatus();