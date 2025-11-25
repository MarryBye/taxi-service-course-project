SELECT
    ro.id,
    ro.client_id,
    ro.driver_id,
    os.name AS order_status,
    ro.ride_date,
    ro.ride_date_end,
    ro.price,
    ror.client_mark AS client_mark,
    ror.driver_mark AS driver_mark
FROM RideOrder ro
JOIN RideOrder_status os ON ro.order_status_id = os.id
JOIN RideOrder_Rating ror ON ror.order_id = ro.id;