SELECT c.first_name, c.last_name
FROM Driver d
JOIN Client c ON c.id = d.user_id
WHERE NOT EXISTS (
    SELECT 1
    FROM RideOrder r
    WHERE r.driver_id = d.user_id
);
