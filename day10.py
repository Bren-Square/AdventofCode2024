"""
    Advent of Code Day 10
    Brendan Swigart
    This was somewhat easier than the previous ilk
"""

with open('day10.txt', encoding='utf-8') as file:
    input_data = file.read().strip()

line_length = input_data.find('\n') if '\n' in input_data else len(input_data)
single_line_data = input_data.replace('\n', '')

def is_trailhead(pos: int, trailmap: str, trailcount: int) -> int:
    """
        A recursive function that counts the number of valid
        trails in a trailmap. uses the index of a string to
        accomplish this.
    """
    # if the trailhead is at 9, this trailhead is complete
    # and there is nothing more to do but increment by
    if trailmap[pos] == '9':
        return trailcount + 1

    # empty lists for later
    trailhead_cardinals, filtered_cardinals = [], []

    # get cardinal positions relative to the current position
    # modulo is used here to detect if the current pos is on an edge
    if pos - line_length >= 0:
        trailhead_cardinals.append([pos - line_length, trailmap[pos - line_length]])
    if pos + line_length < len(trailmap):
        trailhead_cardinals.append([pos + line_length, trailmap[pos + line_length]])
    if pos % line_length != 0:
        trailhead_cardinals.append([pos - 1, trailmap[pos - 1]])
    if (pos + 1) % line_length != 0:
        trailhead_cardinals.append([pos + 1, trailmap[pos + 1]])

    # filter valid next locations by next value we want
    filtered_cardinals = [cardinal for cardinal in trailhead_cardinals
        if int(cardinal[1]) == int(trailmap[pos]) + 1]

    # now with more RECURSION!
    for valid_cardinal in filtered_cardinals:
        trailcount = is_trailhead(int(valid_cardinal[0]), trailmap, trailcount)

    return trailcount


# Initialize trail count
trail_sum = 0 # pylint: disable=invalid-name

# Process input data
for position, _ in enumerate(single_line_data):
    trail_count = 0
    if single_line_data[position] == '0':
        trail_count = is_trailhead(position, single_line_data, trail_count)
    trail_sum += trail_count

print(trail_sum)
