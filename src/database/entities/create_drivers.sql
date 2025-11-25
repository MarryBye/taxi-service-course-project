CREATE TABLE IF NOT EXISTS drivers (
    user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    balance DOUBLE PRECISION NOT NULL CHECK (balance >= 0) DEFAULT 0.0,
    rating DOUBLE PRECISION NOT NULL CHECK (rating >= 0 AND rating <= 5) DEFAULT 0.0,
    license_number VARCHAR(32) NOT NULL UNIQUE CHECK (check_license_number(license_number))
)