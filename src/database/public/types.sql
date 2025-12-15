CREATE TYPE public.car_statuses AS ENUM (
    'available',
    'on_maintenance',
    'busy',
    'not_working'
);

CREATE TYPE public.car_classes AS ENUM (
    'standard',
    'comfort',
    'business'
);

CREATE TYPE public.maintenance_statuses AS ENUM (
    'diagnosis',
    'in_progress',
    'completed'
);

CREATE TYPE public.order_statuses AS ENUM (
    'searching_for_driver',
    'waiting_for_driver',
    'waiting_for_client',
    'in_progress',
    'waiting_for_marks',
    'canceled',
    'completed'
);

CREATE TYPE public.transaction_type AS ENUM (
    'debit',
    'credit',
    'refund',
    'penalty'
);

CREATE TYPE public.payment_methods AS ENUM (
    'credit_card',
    'cash'
);

CREATE TYPE public.balance_types AS ENUM (
    'payment',
    'earning'
);

CREATE TYPE public.user_roles AS ENUM (
    'admin',
    'driver',
    'client'
);

CREATE TYPE public.city_names AS ENUM (
    'Kyiv',
    'Lviv',
    'Odessa',
    'Dnipro',
    'Kharkiv'
);

CREATE TYPE public.client_tags AS ENUM (
    'accurate',
    'friendly',
    'respectful',
    'communicative',
    'polite'
);

CREATE TYPE public.driver_tags AS ENUM (
    'accurate',
    'fast',
    'friendly',
    'clean',
    'modern_car',
    'polite',
    'communicative',
    'helpful'
);

CREATE TYPE public.driver_cancel_tags AS ENUM (
    'reason 1',
    'reason 2',
    'reason 3'
);

CREATE TYPE public.client_cancel_tags AS ENUM (
    'reason 1',
    'reason 2',
    'reason 3'
);

CREATE TYPE public.country_names AS ENUM (
    'Ukraine'
);

CREATE TYPE public.address AS (
	country_name country_names,
	city_name city_names,
	street_name VARCHAR(32),
	house_number VARCHAR(9),
	latitude DOUBLE PRECISION,
	longitude DOUBLE PRECISION 
);