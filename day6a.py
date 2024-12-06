"""
    AoC Day 6 - Part 1
    Brendan Swigart
"""

FILE_PATH = 'day6.txt'
with open(FILE_PATH, 'r', encoding="utf-8") as file:
    grid = file.read()

# get each row
rows = grid.strip().split('\n')

# get number of rows
row_count = len(rows)

# create a dictionary of coordinates and values
coordinates = {}
for y, row in enumerate(rows):
    for x, value in enumerate(row):
        # Get the guard's location
        if value not in {'.', '#'}:
            guard = [value, x, y]
            guard_back = [value, x, y]
        coordinates[(x, y)] = value

# Accounts for starting point of the guard
initial_coordinates = (int(guard[1]), int(guard[2]))  # pylint: disable=possibly-used-before-assignment
coordinates[initial_coordinates] = 'X'

# Dictionaries to tell us what to do
guard_map = {
    '^': [0, -1, '>'],
    '>': [1, 0, 'v'],
    'v': [0, 1, '<'],
    '<': [-1, 0, '^']
}

# Track visited states
visited_states = set()
visited_states.add((guard[1], guard[2], guard[0]))

# Main loop
def main_loop():
    """
        run all the things
    """
    global guard # pylint: disable=global-variable-not-assigned
    while True:
        current_direction = guard[0]
        coordinate_to_check = (
            guard[1] + guard_map[current_direction][0],
            guard[2] + guard_map[current_direction][1]
        )

        if coordinate_to_check in coordinates:
            if '#' in coordinates[coordinate_to_check]:
                # Obstacle ahead, turn right
                guard[0] = guard_map[current_direction][2]
            else:
                # Move forward
                guard[1] += guard_map[current_direction][0]
                guard[2] += guard_map[current_direction][1]
                coordinates[coordinate_to_check] = 'X'
        else:
            # Guard leaves the map
            break

        # Check for infinite loop
        current_state = (guard[1], guard[2], guard[0])
        if current_state in visited_states:
            print("Infinite loop detected!")
            break
        visited_states.add(current_state)

main_loop()

# Print out the map and count up unique locations by 'X'
counter = 0 # pylint: disable=invalid-name
for y, row in enumerate(rows):
    for x, value in enumerate(row):
        if 'X' in coordinates.get((x, y), '.'):
            counter += 1
        print(coordinates.get((x, y), '.'), end="")
    print("")
print(f"Unique locations visited: {counter}")
