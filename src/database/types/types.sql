-- Active: 1764877667177@@127.0.0.1@5432@taxi_db@public
CREATE TYPE address AS (
	country_name country_names,
	city_name city_names,
	street_name VARCHAR(32),
	house_number VARCHAR(9),
	latitude DOUBLE PRECISION,
	longitude DOUBLE PRECISION 
);