SELECT 
    m.user_id AS id,
    c.first_name,
    c.last_name,
    c.email,
    c.tel_number,
    m.rating,
    m.license_number,
    m.role
FROM 
    Mechanic m
JOIN Client c ON c.id = m.user_id;