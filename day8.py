"""
    AoC Day 8
    Brendan Swigart
    There are a ton of issues with this script. I'm aware of them.
    I'm not going to fix them. My hope is to never look at this
    ever again. You shouldn't either.
"""


def parse_map(grid):
    """
        I started doing this the right way with this functions. But then
        I gave up in favor of doing this quickly so that I will never have
        to look at this crap ever again.
        Args: grid (list): list of strings representing the antenna grid.
        Returns: dict: contains frequency and tuple of coords {'freq': (x,y)}
    """
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell.isalnum():  # Check for valid antennas
                antennas.setdefault(cell, []).append((x, y))
    return antennas


# Rather than make a txt I just decided to use vscode and premap
# this piece of crap as a list ahead of time.
input_map = [
    ".....8............1r.....a....................O...", #0
    ".a..............4..q.........................0...9", #1
    "....a.........8...................................", #2
    ".................D.....................V0.........", #3
    ".....d............................................", #4
    ".r..........q....................................O", #5
    "..................q...........................9...", #6
    "..............D..............X..................V.", #7
    "........D................X.................0......", #8
    ".........8............X...........................", #9
    "....................J....................9..0.....", #10
    "..a..B............r..W........J...............R..Q", #11
    "......WD...q.....1..........Q..............R..V...", #12
    ".1W...................u...........................", #13
    "..............................u.............R.....", #14
    "....B..............d..c..................R........", #15
    ".............J..............X............V........", #16
    "......1...........................3...............", #17
    "......B...........d...................3...........", #18
    "............8..J.......u.....3....................", #19
    "...........4.............6........................", #20
    ".....4v.............d.......................O.....", #21
    "..........................v.2.....................", #22
    ".............................................s....", #23
    "..................4...M..W..................s.....", #24
    "......................m...........................", #25
    "...........M......................................", #26
    "..b..................c............................", #27
    "....................Co..........KQ.......O.s......", #28
    ".................C............................s...", #29
    ".......x............c............................3", #30
    "........o......A....U.....Q.........5.............", #31
    "...............U..................j...5...........", #32
    ".....K.......U................j..........2........", #33
    ".......A.v.....w.....................c...5........", #34
    "..K....................................j..........", #35
    "...............K.yk....B.............2............", #36
    "......C....b..............x...........Y...........", #37
    ".....mA..C......U.................................", #38
    "........M.....A.....................2..6...5......", #39
    ".............................7.......Y............", #40
    ".m.M......w..v....................................", #41
    "............m...........x.....Y...................", #42
    "....................k....w........................", #43
    "......b.....w..S....7.............................", #44
    "..............S..............x...........Y........", #45
    "....................S...6.........................", #46
    ".y...............S..........7.6.................9.", #47
    "o..........k...............b......................", #48
    "yo...........k....................................", #49
]

# get all coordinates
coordinate_map = parse_map(input_map)
antinode_locations = set()

# Is there a cleaner way to do this nasty triple loop? Most certainly, yes.
# Will I ever go back and refactor it and/or do I care? Not a chance in hell.
# Why not? Because this challenge is obnoxious af and serves no real value
# to me outside of a gold star on an advent calendar. That's why.
for frequency, coordinates in coordinate_map.items():
    for i, _ in enumerate(coordinates):
        for j in range(i + 1, len(coordinates)):

            # get tuples
            a, b = coordinates[i], coordinates[j]

            # unpack tuples
            ax, ay = a
            bx, by = b

            # 6th grade adage: "slope equals rise over run"
            dx = ax - bx
            dy = ay - by

            # Determine step direction for extending the line
            step_x = -1 if dx > 0 else 1 if dx < 0 else 0 # pylint: disable=invalid-name
            step_y = -1 if dy > 0 else 1 if dy < 0 else 0 # pylint: disable=invalid-name

            # Initial antinode coordinates
            anti_ax, anti_ay = ax + step_x * abs(dx), ay + step_y * abs(dy)
            anti_bx, anti_by = bx - step_x * abs(dx), by - step_y * abs(dy)

            # create the first two antinode tuples
            anti_coord_a = (anti_ax, anti_ay)
            anti_coord_b = (anti_bx, anti_by)

            # create maximum x/y values because line length
            x_len = len(input_map) # pylint: disable=invalid-name
            y_len = len(input_map[0]) # pylint: disable=invalid-name
            # check if the antinodes exist on valid coordinates
            if all(0 <= n < x_len and 0 <= n < y_len for n in anti_coord_a):
                antinode_locations.add(anti_coord_a)
            if all(0 <= n < x_len and 0 <= n < y_len for n in anti_coord_b):
                antinode_locations.add(anti_coord_b)

            # continue to place antinodes along a until it falls
            # off the grid via negative number or out of index range.
            while 0 <= anti_ax < y_len and 0 <= anti_ay < x_len:
                anti_ax += step_x * abs(dx)
                anti_ay += step_y * abs(dy)
                anti_coord_a = (anti_ax, anti_ay)
                if all(0 <= n < x_len and 0 <= n < y_len for n in anti_coord_a):
                    antinode_locations.add(anti_coord_a)
                else:
                    break

            # continue to place antinodes along a until it falls
            # off the grid via negative number or out of index range.
            while 0 <= anti_bx < y_len and 0 <= anti_by < x_len:
                anti_bx -= step_x * abs(dx)
                anti_by -= step_y * abs(dy)
                anti_coord_b = (anti_bx, anti_by)
                if all(0 <= n < x_len and 0 <= n < y_len for n in anti_coord_b):
                    antinode_locations.add(anti_coord_b)
                else:
                    break

print(len(antinode_locations))
