CREATE OR REPLACE FUNCTION WriteHistoryOrder()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.status_id IS DISTINCT FROM NEW.status_id THEN
        INSERT INTO orders_status_history
        (order_id, order_status_id)
        VALUES
        (OLD.id, NEW.status_id);
    END IF;

    IF OLD.driver_id IS DISTINCT FROM NEW.driver_id THEN
        INSERT INTO orders_driver_history
        (order_id, driver_id)
        VALUES
        (OLD.id, NEW.driver_id);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION WriteHistoryOrderFirst()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO orders_status_history
        (order_id, order_status_id)
    VALUES
        (NEW.id, NEW.status_id);

    INSERT INTO orders_driver_history
        (order_id, driver_id)
    VALUES
        (NEW.id, NEW.driver_id);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER WriteHistoryOrderTrigger
AFTER UPDATE ON orders FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryOrder();

CREATE OR REPLACE TRIGGER WriteHistoryOrderFirstTrigger
AFTER INSERT ON orders FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryOrderFirst();