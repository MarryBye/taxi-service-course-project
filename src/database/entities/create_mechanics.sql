CREATE TABLE IF NOT EXISTS mechanics (
    user_id BIGINT PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    license_number VARCHAR(32) NOT NULL UNIQUE CHECK (check_license_number(license_number))
)