INSERT INTO environmentprofile (
	created_at, 
	updated_at, 
	is_active,  
	name, 
	descr
) VALUES (1777245895, 1777245895, 1, 'Growth Stage', '18h daylight');

INSERT INTO environment (
    created_at,
    updated_at,
    is_active,
    can_id,
    name,
    descr,
    environment_profile_id,
    sort_order
) VALUES (1777245895, 1777245895, 1, 'can01', 'Primary Tent', 'Indoor grow tent', 1, 1);
