CREATE OR REPLACE FUNCTION WriteHistoryMaintenance()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.status_id IS DISTINCT FROM NEW.status_id THEN
        INSERT INTO maintenance_status_history
        (maintenance_id, status_id)
        VALUES
        (OLD.id, NEW.status_id);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION WriteHistoryMaintenanceFirst()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO maintenance_status_history
        (maintenance_id, status_id)
    VALUES
        (NEW.id, NEW.status_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER WriteHistoryMaintenanceTrigger
AFTER UPDATE ON maintenances FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryMaintenance();

CREATE OR REPLACE TRIGGER WriteHistoryMaintenanceFirstTrigger
AFTER INSERT ON maintenances FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryMaintenanceFirst();