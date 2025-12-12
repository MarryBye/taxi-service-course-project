CREATE TYPE car_statuses AS ENUM (
    'available',
    'on_maintenance',
    'busy',
    'not_working'
);

CREATE TYPE car_classes AS ENUM (
    'standard',
    'comfort',
    'business'
);

CREATE TYPE maintenance_statuses AS ENUM (
    'diagnosis',
    'in_progress',
    'completed'
);

CREATE TYPE order_statuses AS ENUM (
    'searching_for_driver',
    'waiting_for_driver',
    'waiting_for_client',
    'in_progress',
    'canceled',
    'completed'
);

CREATE TYPE transaction_type AS ENUM (
    'debit',
    'credit',
    'refund',
    'penalty'
);

CREATE TYPE payment_methods AS ENUM (
    'credit_card',
    'cash'
);

CREATE TYPE balance_types AS ENUM (
    'payment',
    'earning'
);

CREATE TYPE user_roles AS ENUM (
    'admin',
    'driver',
    'client'
);

CREATE TYPE client_tags AS ENUM (
    'accurate',
    'friendly',
    'respectful',
    'communicative',
    'polite'
);

CREATE TYPE driver_tags AS ENUM (
    'accurate',
    'fast',
    'friendly',
    'clean',
    'modern_car',
    'polite',
    'communicative',
    'helpful'
);

CREATE TYPE city_names AS ENUM (
    'Kyiv',
    'Lviv',
    'Odessa',
    'Dnipro',
    'Kharkiv'
);

CREATE TYPE country_names AS ENUM (
    'Ukraine'
);

CREATE TYPE address AS (
	country_name country_names,
	city_name city_names,
	street_name VARCHAR(32),
	house_number VARCHAR(9),
	latitude DOUBLE PRECISION,
	longitude DOUBLE PRECISION 
);