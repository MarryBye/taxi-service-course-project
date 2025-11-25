SELECT 
    a.user_id AS id,
    c.first_name,
    c.last_name,
    c.email,
    c.tel_number,
    a.rating,
    a.role
FROM 
    Administrator a
JOIN Client c ON c.id = a.user_id;