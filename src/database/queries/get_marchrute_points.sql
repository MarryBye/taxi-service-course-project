SELECT 
    mp.id,
    mp.position,
    mp.address,
    mp.marchrute_id
FROM Marchrute_point mp
WHERE mp.marchrute_id = ?
ORDER BY mp.position ASC;