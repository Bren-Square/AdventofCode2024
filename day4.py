""" 
    day4.py
    Advent of Code Day 4
    https://github.com/Bren-Square/AdventofCode2024
"""

# Part 1
def process_grid(grid: str) -> tuple:
    """ 
        And now for something slightly less stupid
        Args: grid (string): Same as it ever was.
        Returns: tuple: reasonable data structures
    """

    # Normal approach
    rows = grid.strip().split('\n')
    row_count = len(rows)
    col_count = len(rows[0])
    horizontals = rows

    # verts
    verticals = ["".join(row[i] for row in rows if i < len(row)) for i in range(col_count)]

    # empty lists for later
    l_diags, r_diags = [], []

    # top-left to bottom-right
    for k in range(-(row_count - 1), col_count):  # Ranges to cover all diagonals
        diag, coords = [], []
        for i in range(row_count):
            j = i - k
            if 0 <= j < col_count:
                diag.append(rows[i][j])
                coords.append([i + 1, j + 1])
        l_diags.append(["".join(diag), coords])

    # top-right to bottom left
    for k in range(0, row_count + col_count - 1):
        diag, coords = [], []
        for i in range(row_count):
            j = k - i
            if 0 <= j < col_count:
                diag.append(rows[i][j])
                coords.append([i + 1, j + 1])  # same shit, different shovel
        r_diags.append(["".join(diag), coords])

    return horizontals, verticals, l_diags, r_diags

# Get grid
FILE_PATH = 'day4.txt'
with open(FILE_PATH, 'r', encoding="utf-8") as file:
    block = file.read()
    h, v, l, r = process_grid(block)

# Add em up
total_count = sum(
    line.lower().count("xmas") + line.lower().count("samx")
        for line in h + v + [item[0] for item in l] + [item[0] for item in r])

print(total_count)


# Part 2
def get_coordinates(data_pairs: list) -> list:
    """_summary_
    A function which gets you coordinates of the char
    A within a string, coordinate pair.
    Args: data_pairs (list): string, coordinate pairs
    Returns: list: Coordinates of the "A" characters
    """
    string, coordinates = data_pairs
    results = [] # for later

    for i in range(len(string) - 2):  # Iterate string, 3 chars at a time.
        if string[i:i+3] in ['MAS', 'SAM']:  # slice notation matching
            results.append(coordinates[i + 1])  # Append coords for later

    return results

# Extract coordinates of all characters "A" that are in "SAM" or "MAS"
l_coords = []
for diagonal in l:
    l_coords += get_coordinates(diagonal)

# Extract coordinates of all characters "A" that are in "SAM" or "MAS"
r_coords = []
for diagonal in r:
    r_coords += get_coordinates(diagonal)


# Convert coordinates into set tuples
# so that we can calculate the intersections.
l_set = set(map(tuple, l_coords))
r_set = set(map(tuple, r_coords))

# Find the intersection and count the matches
matches = l_set & r_set
count = len(matches)

# print em out
print(count)
