CREATE OR REPLACE FUNCTION WriteHistoryCars()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.driver_id IS DISTINCT FROM NEW.driver_id THEN
        INSERT INTO cars_driver_history
        (car_id, driver_id)
        VALUES
        (OLD.id, NEW.driver_id);
    END IF;

    IF OLD.status_id IS DISTINCT FROM NEW.status_id THEN
        INSERT INTO cars_status_history
        (car_id, status_id)
        VALUES
        (OLD.id, NEW.status_id);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION WriteHistoryCarsFirst()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO cars_driver_history
        (car_id, driver_id)
    VALUES
        (NEW.id, NEW.driver_id);

    INSERT INTO cars_status_history
        (car_id, status_id)
    VALUES
        (NEW.id, NEW.status_id);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER WriteHistoryCarsTrigger
AFTER UPDATE ON cars FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryCars();

CREATE OR REPLACE TRIGGER WriteHistoryCarsFirstTrigger
AFTER INSERT ON cars FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryCarsFirst();