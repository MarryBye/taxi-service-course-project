CREATE TABLE IF NOT EXISTS users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    login VARCHAR(32) NOT NULL UNIQUE,
    email VARCHAR(128) NOT NULL UNIQUE CHECK (check_email(email)),
    tel_number VARCHAR(32) NOT NULL UNIQUE CHECK (check_tel(tel_number)),
    password_hash VARCHAR(512) NOT NULL CHECK (check_password(password_hash)),
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    balance DOUBLE PRECISION NOT NULL CHECK (balance >= 0) DEFAULT 0,
    rating DOUBLE PRECISION NOT NULL CHECK (rating >= 0 AND rating <= 5) DEFAULT 0.0
)