-- Create balances for a new user

CREATE OR REPLACE FUNCTION create_user_balance() RETURNS trigger AS $$
BEGIN

    INSERT INTO
        balances(user_id, balance_type)
    VALUES
        (NEW.id, 'payment'),
        (NEW.id, 'earning');

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER create_user_balance_trigger
AFTER INSERT ON users
FOR EACH ROW EXECUTE PROCEDURE create_user_balance();