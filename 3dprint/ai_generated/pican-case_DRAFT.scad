// --- PI 5 + PICAN3 ENCLOSURE (TALL VERSION WITH PRESS-FIT LID) ---
$fn = 60;
// Mechanical Constants
wall = 2.0;           
gap = 0.5;            // Tolerance for the Pi PCB
lid_gap = 0.2;        // Tolerance for the lid fit
lip_h = 3.0;          // Height of the press-fit lip
lip_clearance = 0.15; // Tight fit clearance for press-fit
pcb_l = 92.0; pcb_w = 56.0;  // Increased length from 88mm to 92mm
hole_x = 58.0; hole_y = 49.0; edge_off = 3.5;
// Vertical Stack
base_pillar_h = 3.5;  
hat_gap_h = 11.0;     
pcb_t = 1.6;          
total_int_h = 40.0;
module base_pillars() {
    locs = [[0,0], [hole_x, 0], [0, hole_y], [hole_x, hole_y]];
    for (p = locs) {
        translate([p[0] + wall + gap + edge_off, p[1] + wall + gap + edge_off, wall]) {
            difference() {
                cylinder(h = base_pillar_h, r = 3.5);
                cylinder(h = base_pillar_h + 1, r = 1.25); // M2.5 screw hole
            }
        }
    }
}
module side_cutouts() {
    bx = wall + gap;
    by = wall + gap;
    pi_z = wall + base_pillar_h + 2.5; 
    pican_z = wall + base_pillar_h + pcb_t + hat_gap_h + pcb_t;
    // --- LONG SIDE (USB-C, HDMI, PICAN3 DB9/Terminal) ---
    // Pi 5 Lower Ports
    translate([bx + 11.2, by - wall, pi_z]) cube([10, wall*3, 5], center=true);
    translate([bx + 25.8, by - wall, pi_z]) cube([8, wall*3, 5], center=true);
    translate([bx + 39.2, by - wall, pi_z]) cube([8, wall*3, 5], center=true);
    
    // PiCAN3 Ports (Aligned vertically above Pi ports)
    translate([bx + 15.0, by - wall, pican_z + 4.5]) cube([16, wall*3, 9], center=true); 
    translate([bx + 46.5, by - wall, pican_z + 7.5]) cube([32, wall*3, 15], center=true);
    // --- SHORT SIDE (Ethernet / USB Stack) ---
    eth_z = wall + base_pillar_h + 6.5;
    translate([bx + pcb_l + wall, by + 10.2, eth_z]) cube([wall*3, 16, 13], center=true);
    translate([bx + pcb_l + wall, by + 29.1, eth_z + 1.5]) cube([wall*3, 15, 16], center=true);
    translate([bx + pcb_l + wall, by + 47.0, eth_z + 1.5]) cube([wall*3, 15, 16], center=true);
    
    // SD Card
    translate([bx - wall, by + 28, wall + 1.5]) cube([wall*3, 12, 3], center=true);
}
module main_body() {
    difference() {
        // Outer box
        cube([pcb_l + (wall+gap)*2, pcb_w + (wall+gap)*2, total_int_h + wall]);
        
        // Inner cavity
        translate([wall, wall, wall]) 
            cube([pcb_l + gap*2, pcb_w + gap*2, total_int_h + 5]);
        
        // Groove for press-fit lip (recessed area for lid to sit in)
        translate([wall/2 + lip_clearance, wall/2 + lip_clearance, total_int_h + wall - lip_h])
            cube([pcb_l + gap*2 + wall - 2*lip_clearance, 
                  pcb_w + gap*2 + wall - 2*lip_clearance, 
                  lip_h + 1]);
        
        side_cutouts();
    }
}
module lid() {
    l_w = pcb_l + gap*2 + wall - lid_gap;
    l_d = pcb_w + gap*2 + wall - lid_gap;
    lip_w = l_w - wall - 2*lip_clearance;
    lip_d = l_d - wall - 2*lip_clearance;
    
    translate([0, 80, 0]) { // Moved aside for visibility
        union() {
            // Main lid plate
            difference() {
                cube([l_w, l_d, 2]);
                
                // Ventilation Slots
                for (i = [10 : 6 : l_w - 10]) {
                    translate([i, 5, -1]) cube([3, l_d - 10, 4]);
                }
            }
            
            // Press-fit lip that goes into the groove
            translate([wall/2 + lip_clearance, wall/2 + lip_clearance, 2])
                difference() {
                    cube([lip_w, lip_d, lip_h]);
                    // Hollow out the center to create a perimeter lip
                    translate([wall, wall, -1])
                        cube([lip_w - 2*wall, lip_d - 2*wall, lip_h + 2]);
                }
        }
    }
}
// Render Everything
union() {
    main_body();
    base_pillars();
}
lid(); // Rendered next to the case