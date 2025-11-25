CREATE OR REPLACE FUNCTION UpdateCancelledOrder()
RETURNS TRIGGER AS $$
DECLARE
    cancel_status_id BIGINT;
BEGIN

    cancel_status_id := (SELECT id FROM order_statuses WHERE name = 'Cancelled');

    UPDATE orders SET status_id = cancel_status_id
    WHERE id = NEW.order_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER UpdateCancelledOrderTrigger
AFTER INSERT ON orders_cancels FOR EACH ROW
EXECUTE PROCEDURE UpdateCancelledOrder();