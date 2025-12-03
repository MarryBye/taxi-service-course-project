-- Active: 1763469782117@@127.0.0.1@5432@taxi_db@public
CREATE TYPE address AS (
	country_name VARCHAR(32),
	city_name VARCHAR(32),
	street_name VARCHAR(32),
	house_number VARCHAR(9),
	latitude DOUBLE PRECISION,
	longitude DOUBLE PRECISION 
);