from itertools import combinations

def generate_ot_lookup(
    target_nth: int, 
    max_spaces: int, 
    lookup_name: str = None,
    char_class: str = "@CHARACTERS", 
    space_glyph: str = "space", 
    replacement_glyph: str = "space.blank"
) -> str:
    """
    Generates an OpenType lookup that substitutes the Nth character,
    ignoring up to `max_spaces` spaces inside the counting window.
    """
    if target_nth < 2:
        raise ValueError("target_nth must be at least 2.")
    
    if lookup_name is None:
        lookup_name = f"Target_{target_nth}"

    lines = [f"lookup {lookup_name} {{"]

    # Iterate from 0 spaces up to max_spaces
    for num_spaces in range(max_spaces + 1):
        lines.append(f"    # {num_spaces} space(s)")
        
        # After the 1st character (@CHARACTERS) and before the target (@CHARACTERS'),
        # there are (target_nth - 2) remaining characters plus (num_spaces) spaces.
        middle_slots = (target_nth - 2) + num_spaces
        
        # Choose which of those middle slots will be occupied by spaces.
        # Reversing combinations puts spaces near the end of the sequence first, 
        # matching the clean bottom-to-top cascading style.
        for space_indices in reversed(list(combinations(range(middle_slots), num_spaces))):
            space_set = set(space_indices)
            
            # The sequence always starts with a valid character (starts the count)
            sequence = [char_class]
            
            # Fill the middle slots with either spaces or characters
            for idx in range(middle_slots):
                if idx in space_set:
                    sequence.append(space_glyph)
                else:
                    sequence.append(char_class)
            
            # The sequence always ends with the target character marked with '
            sequence.append(f"{char_class}'")
            
            rule = f"    sub {' '.join(sequence)} by {replacement_glyph};"
            lines.append(rule)

    lines.append(f"}} {lookup_name};\n")
    return "\n".join(lines)


# ==========================================
# CONFIGURATION (Change your values here)
# ==========================================

# 1. Specify the target numbers and lookup names you want to generate:
# Format: (Target Nth Character, "LookupName")
TARGETS = [
    (5, "TargetFifth"),
    (6, "TargetSixth"),
    (7, "TargetSeventh"),
    (8, "TargetEight"),
    (9, "TargetNineth"),
]

# 2. Specify the maximum number of spaces to ignore inside the window:
MAX_SPACES = 4

# 3. Output file name (set to None if you only want to print to console)
OUTPUT_FILE = "generated_lookups.fea"


# ==========================================
# EXECUTION
# ==========================================
if __name__ == "__main__":
    all_lookups = []
    
    for nth, name in TARGETS:
        lookup_code = generate_ot_lookup(
            target_nth=nth, 
            max_spaces=MAX_SPACES, 
            lookup_name=name
        )
        all_lookups.append(lookup_code)
    
    final_fea_code = "\n".join(all_lookups)
    
    # Print to console / Macro window
    print(final_fea_code)
    
    # Save to file
    if OUTPUT_FILE:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(final_fea_code)
        print(f"// Successfully saved {len(TARGETS)} lookups to '{OUTPUT_FILE}'")