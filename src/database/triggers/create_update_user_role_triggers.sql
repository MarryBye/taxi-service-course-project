CREATE OR REPLACE FUNCTION AddUserRole() 
RETURNS TRIGGER AS $$
DECLARE
    new_role_id BIGINT;
    has_role BOOLEAN;
BEGIN
    IF (TG_TABLE_NAME = 'drivers') THEN
        new_role_id := (SELECT id FROM roles WHERE name = 'Driver');
    ELSIF (TG_TABLE_NAME = 'dispatchers') THEN
        new_role_id := (SELECT id FROM roles WHERE name = 'Dispatcher');
    ELSIF (TG_TABLE_NAME = 'mechanics') THEN
        new_role_id := (SELECT id FROM roles WHERE name = 'Mechanic');
    ELSIF (TG_TABLE_NAME = 'administrators') THEN
        new_role_id := (SELECT id FROM roles WHERE name = 'Administrator');
    END IF;

    has_role := (EXISTS (SELECT 1 FROM users_roles WHERE user_id = NEW.user_id AND role_id = new_role_id));

    IF (has_role) THEN
        RETURN NEW;
    END IF;

    INSERT INTO users_roles
        (user_id, role_id)
    VALUES 
        (NEW.user_id, new_role_id);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION RemoveUserRole()
RETURNS TRIGGER AS $$
DECLARE
    old_role_id BIGINT;
    has_role BOOLEAN;
BEGIN
    IF (TG_TABLE_NAME = 'drivers') THEN
        old_role_id := (SELECT id FROM roles WHERE name = 'Driver');
    ELSIF (TG_TABLE_NAME = 'dispatchers') THEN
        old_role_id := (SELECT id FROM roles WHERE name = 'Dispatcher');
    ELSIF (TG_TABLE_NAME = 'mechanics') THEN
        old_role_id := (SELECT id FROM roles WHERE name = 'Mechanic');
    ELSIF (TG_TABLE_NAME = 'administrators') THEN
        old_role_id := (SELECT id FROM roles WHERE name = 'Administrator');
    END IF;

    has_role := (EXISTS (SELECT 1 FROM users_roles WHERE user_id = OLD.user_id AND role_id = old_role_id));

    IF (NOT has_role) THEN
        RETURN OLD;
    END IF;

    DELETE FROM users_roles
    WHERE user_id = OLD.user_id AND role_id = old_role_id;

    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER AddDriverRoleTrigger
AFTER INSERT ON drivers FOR EACH ROW
EXECUTE PROCEDURE AddUserRole();

CREATE OR REPLACE TRIGGER AddDispatcherRoleTrigger
AFTER INSERT ON dispatchers FOR EACH ROW
EXECUTE PROCEDURE AddUserRole();

CREATE OR REPLACE TRIGGER AddMechanicRoleTrigger
AFTER INSERT ON mechanics FOR EACH ROW
EXECUTE PROCEDURE AddUserRole();

CREATE OR REPLACE TRIGGER AddAdministratorRoleTrigger
AFTER INSERT ON administrators FOR EACH ROW
EXECUTE PROCEDURE AddUserRole();

CREATE OR REPLACE TRIGGER RemoveDriverRoleTrigger
AFTER DELETE ON drivers FOR EACH ROW
EXECUTE PROCEDURE RemoveUserRole();

CREATE OR REPLACE TRIGGER RemoveDispatcherRoleTrigger
AFTER DELETE ON dispatchers FOR EACH ROW
EXECUTE PROCEDURE RemoveUserRole();

CREATE OR REPLACE TRIGGER RemoveMechanicRoleTrigger
AFTER DELETE ON mechanics FOR EACH ROW
EXECUTE PROCEDURE RemoveUserRole();

CREATE OR REPLACE TRIGGER RemoveAdministratorRoleTrigger
AFTER DELETE ON administrators FOR EACH ROW
EXECUTE PROCEDURE RemoveUserRole();