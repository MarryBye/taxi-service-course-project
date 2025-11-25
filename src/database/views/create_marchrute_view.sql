CREATE OR REPLACE VIEW marchrutes_view AS
SELECT
    m.id,
    m.order_id,
    m.distance,
    (SELECT mp.address FROM marchrute_points AS mp WHERE mp.marchrute_id = m.id ORDER BY mp.position ASC LIMIT 1) AS start_point,
    (SELECT mp.address FROM marchrute_points AS mp WHERE mp.marchrute_id = m.id ORDER BY mp.position DESC LIMIT 1) AS end_point,
    ARRAY_AGG(mp.address) AS adresses
FROM marchrutes m
JOIN marchrute_points AS mp ON m.id = mp.marchrute_id
GROUP BY m.id
