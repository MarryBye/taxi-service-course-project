SELECT 
    CONCAT(c.first_name, ' ', c.last_name) client_name,
    CONCAT(dr.first_name, ' ', dr.last_name) driver_name,
    cr.model car_model,
    p.price price,
    pm.name AS payment_method,
    (ro.ride_date_end - ro.ride_date) duration
FROM rideorder ro
JOIN Client c ON ro.client_id = c.id
JOIN Driver d ON ro.driver_id = d.user_id
JOIN Client dr ON dr.id = d.user_id
JOIN car cr ON d.car_id = cr.id
JOIN payment p ON ro.payment_id = p.id
JOIN payment_method pm on p.payment_method_id = pm.id
WHERE p.price > 300 AND (ro.ride_date_end - ro.ride_date) >= INTERVAL '15 minutes';
