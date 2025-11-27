CREATE OR REPLACE FUNCTION update_user_balance() RETURNS trigger AS $$
DECLARE
    current_balance NUMERIC;
    adjust_amount NUMERIC;
BEGIN
    current_balance := (
        SELECT balance
        FROM balances
        WHERE user_id = NEW.user_id
        AND balance_type = NEW.balance_type
    );
    if (NEW.transaction_type = 'debit') THEN
        adjust_amount := NEW.amount;
    ELSIF (NEW.transaction_type = 'credit') THEN
        adjust_amount := -NEW.amount;
    ELSIF (NEW.transaction_type = 'refund') THEN
        adjust_amount := NEW.amount;
    ELSIF (NEW.transaction_type = 'penalty') THEN
        adjust_amount := -NEW.amount;
    END IF;
    IF ((current_balance + adjust_amount) < 0) THEN
        IF (NOT NEW.transaction_type = 'penalty') THEN
            RAISE NOTICE 'Insufficient funds! You need to add money to your account.';
            RETURN NULL;
        END IF;
    END IF;
    UPDATE balances
    SET balance = (balance + adjust_amount), updated_at = NOW()
    WHERE user_id = NEW.user_id
    AND balance_type = NEW.balance_type;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_user_balance_trigger
AFTER INSERT OR UPDATE ON transactions
FOR EACH ROW EXECUTE PROCEDURE update_user_balance();