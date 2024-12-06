"""
    AoC Day 6 - Part Two
    Brendan Swigart
    decided to put this in a second file since the first one
    was convoluted to all hell and back - this part is much
    cleaner and easier to follow and I'm too lazy to fix 
    part 1 at this moment in time.
"""

# read in the map
FILE_PATH = 'day6.txt'
with open(FILE_PATH, 'r', encoding="utf-8") as file:
    grid = file.read()

# split it out into rows and row length
rows = grid.strip().split('\n')
row_count = len(rows)

# create dictionary with x,y pairs as the keys
coordinates = {}
guard = None # pylint: disable=invalid-name
for y, row in enumerate(rows):
    for x, value in enumerate(row):
        if value not in {'.', '#'}:
            guard = [value, x, y]  # Guard's initial direction, x, y
        coordinates[(x, y)] = value

# This is so that we can automate how the guard moves
guard_map = {
    '^': [0, -1, '>'],
    '>': [1, 0, 'v'],
    'v': [0, 1, '<'],
    '<': [-1, 0, '^']
}


def simulate_guard_with_obstruction(obstruction):
    """
        Simulate the guard's movement with a specific obstruction in place.
        Returns True if the guard enters an infinite loop.
    """
    local_coordinates = coordinates.copy()
    local_coordinates[obstruction] = '#'  # Add the obstruction
    visited_states = set()
    local_guard = guard[:]
    visited_states.add((local_guard[1], local_guard[2], local_guard[0]))

    while True:
        current_direction = local_guard[0]
        next_position = (
            local_guard[1] + guard_map[current_direction][0],
            local_guard[2] + guard_map[current_direction][1]
        )

        # Check if the next position is within the map
        if next_position in local_coordinates:
            # turn if obstruction found
            if local_coordinates[next_position] == '#':
                local_guard[0] = guard_map[current_direction][2]
            else:
                # move forward if no obstruction
                local_guard[1] += guard_map[current_direction][0]
                local_guard[2] += guard_map[current_direction][1]
        else:
            # if guard leaves map
            return False

        # check for infinite loop
        current_state = (local_guard[1], local_guard[2], local_guard[0])
        if current_state in visited_states:
            return True
        visited_states.add(current_state)

def find_obstruction_positions():
    """
        Finds all obstructions that cause infinite loops
    """
    possible_positions = []
    for position, value in coordinates.items(): # pylint: disable=redefined-outer-name
        # not starting position
        if value == '.' and position != (guard[1], guard[2]):
            if simulate_guard_with_obstruction(position):
                possible_positions.append(position)
    return possible_positions


# find all possible obstructions
obstruction_positions = find_obstruction_positions()
print(f"Number of possible positions for the obstruction: {len(obstruction_positions)}")
print("Positions:", obstruction_positions)
