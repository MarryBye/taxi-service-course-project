CREATE OR REPLACE FUNCTION update_order_on_finish() RETURNS trigger AS $$
BEGIN
    IF (NEW.status = 'finished') THEN
        INSERT INTO order_ratings
            (order_id)
        VALUES
            (NEW.id);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_order_on_finish_trigger
AFTER UPDATE ON orders
FOR EACH ROW EXECUTE PROCEDURE update_order_on_finish();