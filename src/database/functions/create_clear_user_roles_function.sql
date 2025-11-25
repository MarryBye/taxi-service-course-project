CREATE OR REPLACE FUNCTION ClearUserRoles(
    p_user_id UUID
) RETURNS void
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM Driver        WHERE user_id = p_user_id;
    DELETE FROM Mechanic      WHERE user_id = p_user_id;
    DELETE FROM Dispatcher    WHERE user_id = p_user_id;
    DELETE FROM Administrator WHERE user_id = p_user_id;
END;
$$;