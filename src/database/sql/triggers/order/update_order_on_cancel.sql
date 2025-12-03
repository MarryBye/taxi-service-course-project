CREATE OR REPLACE FUNCTION update_order_on_cancel() RETURNS trigger AS $$
BEGIN
    UPDATE orders
    SET status = 'canceled', finished_at = NOW()
    WHERE id = NEW.order_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_order_on_cancel_trigger
AFTER INSERT ON order_cancels
FOR EACH ROW EXECUTE PROCEDURE update_order_on_cancel();