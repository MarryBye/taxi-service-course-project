CREATE OR REPLACE FUNCTION WriteHistoryPayment()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.status_id IS DISTINCT FROM NEW.status_id THEN
        INSERT INTO payment_status_history
        (payment_id, status_id)
        VALUES
        (OLD.id, NEW.status_id);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION WriteHistoryPaymentFirst()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO payment_status_history
        (payment_id, status_id)
    VALUES
        (NEW.id, NEW.status_id);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER WriteHistoryPaymentTrigger
AFTER UPDATE ON payments FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryPayment();

CREATE OR REPLACE TRIGGER WriteHistoryPaymentFirstTrigger
AFTER INSERT ON payments FOR EACH ROW
EXECUTE PROCEDURE WriteHistoryPaymentFirst();