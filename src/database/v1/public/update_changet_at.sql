CREATE OR REPLACE FUNCTION update_changed_at() RETURNS trigger AS $$
BEGIN
    NEW.changed_at := now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_changed_at_trigger
BEFORE UPDATE ON balances
FOR EACH ROW EXECUTE PROCEDURE update_changed_at();

CREATE OR REPLACE TRIGGER update_changed_at_trigger
BEFORE UPDATE ON cars
FOR EACH ROW EXECUTE PROCEDURE update_changed_at();

CREATE OR REPLACE TRIGGER update_changed_at_trigger
BEFORE UPDATE ON maintenances
FOR EACH ROW EXECUTE PROCEDURE update_changed_at();

CREATE OR REPLACE TRIGGER update_changed_at_trigger
BEFORE UPDATE ON order_cancels
FOR EACH ROW EXECUTE PROCEDURE update_changed_at();

CREATE OR REPLACE TRIGGER update_changed_at_trigger
BEFORE UPDATE ON order_ratings
FOR EACH ROW EXECUTE PROCEDURE update_changed_at();

CREATE OR REPLACE TRIGGER update_changed_at_trigger
BEFORE UPDATE ON orders
FOR EACH ROW EXECUTE PROCEDURE update_changed_at();

CREATE OR REPLACE TRIGGER update_changed_at_trigger
BEFORE UPDATE ON users
FOR EACH ROW EXECUTE PROCEDURE update_changed_at();