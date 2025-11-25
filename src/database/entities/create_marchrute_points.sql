CREATE TABLE marchrute_points (
	id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	position INT NOT NULL,
	address ADDRESS,
	marchrute_id INT NOT NULL REFERENCES marchrutes(id) ON DELETE CASCADE,
	UNIQUE(marchrute_id, position)
)