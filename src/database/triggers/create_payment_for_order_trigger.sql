CREATE OR REPLACE FUNCTION CreatePaymentForOrder()
RETURNS TRIGGER AS $$
DECLARE
    waiting_for_payment_id BIGINT;
    payment_method_id BIGINT;
    car_class_price DOUBLE PRECISION;
    full_price DOUBLE PRECISION;
BEGIN
    waiting_for_payment_id := (SELECT 1 FROM payment_statuses WHERE name = 'Waiting');
    payment_method_id := (SELECT 1 FROM payment_methods WHERE name = 'Credit card');

    car_class_price := (
        SELECT cc.min_price
        FROM orders as o
        JOIN drivers as d on d.user_id = o.driver_id
        JOIN cars as c on c.driver_id = d.user_id
        JOIN car_classes as cc on c.class_id = cc.id
        WHERE o.id = NEW.id
    );

    full_price := NEW.price + car_class_price;

    UPDATE orders SET price = full_price WHERE id = NEW.id;

    INSERT INTO payments
        (order_id, method_id, status_id, price)
    VALUES
        (NEW.id, waiting_for_payment_id, payment_method_id, full_price);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER CreatePaymentForOrderTrigger
AFTER INSERT ON orders FOR EACH ROW
EXECUTE PROCEDURE CreatePaymentForOrder();