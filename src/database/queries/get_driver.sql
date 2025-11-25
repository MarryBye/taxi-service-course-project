SELECT 
    d.user_id AS id,
    c.first_name,
    c.last_name,
    c.email,
    c.tel_number,
    d.license_number,
    d.balance,
    d.rating
FROM 
    Driver d
JOIN Client c ON c.id = d.user_id;