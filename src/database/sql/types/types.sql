-- Active: 1764877667177@@127.0.0.1@5432@TaxiDBProject@public
CREATE TYPE address AS (
	country_name VARCHAR(32),
	city_name VARCHAR(32),
	street_name VARCHAR(32),
	house_number VARCHAR(9),
	latitude DOUBLE PRECISION,
	longitude DOUBLE PRECISION 
);

CREATE TYPE driver_type AS (
  id int,
  first_name text,
  last_name text,
  email text,
  tel_number text,
  created_at timestamptz
);