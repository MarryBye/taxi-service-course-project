CREATE OR REPLACE PROCEDURE update_balance(par_user_id BIGINT, par_balance_type balance_types) AS $$
DECLARE
    last_update_date TIMESTAMP;
    update_to_date TIMESTAMP;
    new_balance NUMERIC;
BEGIN
    update_to_date := NOW();
    last_update_date := get_balance_last_update(par_user_id, par_balance_type);
    IF (par_balance_type = 'deposit') THEN
        new_balance := (
            (
                SELECT SUM(amount)
                FROM transactions
                WHERE user_id = par_user_id
                  AND created_at > last_update_date
                  AND created_at <= update_to_date
                  AND (transaction_type = 'deposit' OR transaction_type = 'refund')
            )
            -
            (
                SELECT SUM(amount)
                FROM transactions
                WHERE user_id = par_user_id
                  AND created_at > last_update_date
                  AND created_at <= update_to_date
                  AND (transaction_type = 'payment' OR transaction_type = 'penalty')
            )
        );
    ELSIF (par_balance_type = 'withdraw') THEN
            new_balance := (
            (
                SELECT SUM(amount)
                FROM transactions
                WHERE user_id = par_user_id
                  AND created_at > last_update_date
                  AND created_at <= update_to_date
                  AND transaction_type = 'income'
            )
            -
            (
                SELECT SUM(amount)
                FROM transactions
                WHERE user_id = par_user_id
                  AND created_at > last_update_date
                  AND created_at <= update_to_date
                  AND (transaction_type = 'withdraw' OR transaction_type = 'penalty' OR transaction_type = 'refund')
            )
        );
    END IF;
    IF (NOT new_balance IS NULL) THEN
        UPDATE balances
        SET balance = new_balance, updated_at = update_to_date
        WHERE user_id = par_user_id
          AND balance_type = par_balance_type;
    END IF;
END;
$$ LANGUAGE plpgsql;