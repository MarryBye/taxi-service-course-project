CREATE OR REPLACE FUNCTION CreateMarksForOrderFinish()
RETURNS TRIGGER AS $$
DECLARE
    finish_status_id BIGINT;
BEGIN

    finish_status_id := (SELECT id FROM order_statuses WHERE name = 'Finished');

    IF (NEW.status_id = finish_status_id) THEN
        INSERT INTO orders_rating
            (order_id)
        VALUES
            (NEW.id);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER CreateMarksForOrderFinishTrigger
AFTER UPDATE ON orders FOR EACH ROW
EXECUTE PROCEDURE CreateMarksForOrderFinish();