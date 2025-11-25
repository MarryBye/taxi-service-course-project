SELECT 
    d.user_id AS id,
    c.first_name,
    c.last_name,
    c.email,
    c.tel_number,
    d.rating,
    d.role
FROM 
    Dispatcher d
JOIN Client c ON c.id = d.user_id;