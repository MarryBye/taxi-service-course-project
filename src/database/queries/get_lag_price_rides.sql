select 
    d.user_id,
    c.first_name,
    p.price,
    LAG(p.price) OVER (PARTITION BY d.user_id ORDER BY r.id) as prev_ride,
    p.price - LAG(p.price) OVER (PARTITION BY d.user_id ORDER BY r.id) as difference
from rideorder r
join driver d on r.driver_id = d.user_id
join payment p on r.payment_id = p.id
join client c on c.id = d.user_id
