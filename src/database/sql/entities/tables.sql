CREATE DATABASE taxi_db;

CREATE TABLE IF NOT EXISTS users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    login VARCHAR(32) NOT NULL UNIQUE,
    email VARCHAR(128) NOT NULL UNIQUE CHECK (check_email(email)),
    tel_number VARCHAR(32) NOT NULL UNIQUE CHECK (check_tel(tel_number)),
    password_hash VARCHAR(512) NOT NULL,
    first_name VARCHAR(32) NOT NULL,
    last_name VARCHAR(32) NOT NULL,
    role user_roles NOT NULL DEFAULT 'client',

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    changed_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cars (
	id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    driver_id BIGINT UNIQUE REFERENCES users(id) ON DELETE SET NULL,
	mark VARCHAR(32) NOT NULL,
	model VARCHAR(32) NOT NULL,
	car_number VARCHAR(32) UNIQUE NOT NULL CHECK (check_car_number(car_number)),
	class car_classes NOT NULL DEFAULT 'standard',
    status car_statuses NOT NULL DEFAULT 'available',

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    changed_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS orders (
	id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	client_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    driver_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    status order_statuses NOT NULL DEFAULT 'searching_for_driver',
    finished_at TIMESTAMP,

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    changed_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_ratings (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    mark_by BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    mark NUMERIC NOT NULL CHECK (mark >= 0 AND mark <= 5),
    comment VARCHAR(256),
    UNIQUE (order_id, mark_by),

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    changed_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_cancels (
	id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	order_id BIGINT NOT NULL UNIQUE REFERENCES orders(id) ON DELETE CASCADE,
	canceled_by BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
	comment VARCHAR(256),

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    changed_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_client_tags (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    tag client_tags NOT NULL,
    UNIQUE(order_id, tag),

    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_driver_tags (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    tag driver_tags NOT NULL,
    UNIQUE(order_id, tag),

    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS transactions (
	id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    balance_type balance_types NOT NULL,
    transaction_type transaction_type NOT NULL,
    amount NUMERIC NOT NULL DEFAULT 0 CHECK (amount >= 0),
    order_id BIGINT REFERENCES orders(id) ON DELETE SET NULL,

    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS balances (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    balance NUMERIC NOT NULL DEFAULT 0,
    balance_type balance_types NOT NULL,

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    changed_at TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE(user_id, balance_type)
);

CREATE TABLE IF NOT EXISTS routes (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id BIGINT NOT NULL UNIQUE REFERENCES orders(id) ON DELETE CASCADE,
    start_location address NOT NULL,
    end_location address NOT NULL,
    distance NUMERIC NOT NULL CHECK (distance >= 0)
);

CREATE TABLE IF NOT EXISTS route_points (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    route_id BIGINT NOT NULL REFERENCES routes(id) ON DELETE CASCADE,
    position_index INT NOT NULL CHECK (position_index >= 0),
    location address NOT NULL,
    UNIQUE (route_id, position_index)
);

CREATE TABLE IF NOT EXISTS maintenances (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    manager_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    car_id BIGINT NOT NULL REFERENCES cars(id) ON DELETE CASCADE,
    description VARCHAR(2048) NOT NULL,
    cost NUMERIC NOT NULL DEFAULT 0 CHECK (cost >= 0),
    status maintenance_statuses NOT NULL DEFAULT 'diagnosis',
    maintenance_start TIMESTAMP NOT NULL DEFAULT NOW(),
    maintenance_end TIMESTAMP NOT NULL DEFAULT NOW() + INTERVAL '7 DAY',

    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    changed_at TIMESTAMP NOT NULL DEFAULT NOW()
);