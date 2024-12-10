"""
    Advent of Code Day 9
    Brendan Swigart
    Gonna forget this was a thing too.
    What a pain in the ass, this was.
"""

# baselines
forward_ranges, skip_ranges, position = [], [], 0

# same shit, different pile
with open('day9.txt', encoding='utf-8') as file:
    input_data = file.read().strip()

# loop input and alternate forward_ranges and skip_ranges
for index, char in enumerate(input_data):
    current_range = list(range(position, position + int(char)))
    position += int(char)
    if index % 2 == 0:
        forward_ranges.append(current_range)
    else:
        skip_ranges.append(current_range)

# flatten skip_ranges into a single list
skip_ranges_flat = sum(skip_ranges, [])

# loop through forward_ranges in reverse order
for forward in reversed(forward_ranges):
    for i in reversed(range(len(forward))):
        # Replace values in forward_ranges based on skip_ranges_flat
        if len(skip_ranges_flat) > 0 and forward[i] > skip_ranges_flat[0]:
            forward[i] = skip_ranges_flat[0]  # Replace with smallest value in skip_ranges_flat
            skip_ranges_flat = skip_ranges_flat[1:]  # Remove used value

# Compute the final result
part1_result = sum(i * j for i, forward in enumerate(forward_ranges) for j in forward)
print("Part 1 Result:", part1_result)


# Part 2

# reinit lists and position tracker
forward_ranges, skip_ranges, position = [], [], 0

# loop input and alternate forward_ranges and skip_ranges
for index, char in enumerate(input_data):
    current_range = list(range(position, position + int(char)))  # Create a range

    # Update position pointer
    position += int(char)
    if index % 2 == 0:
        # add to forward ranges
        forward_ranges.append(current_range)
    else:
        # add to skip ranges
        skip_ranges.append(current_range)

# process forward_ranges and skip_ranges
for y in reversed(range(len(forward_ranges))):
    for x, skip in enumerate(skip_ranges):
        # replace forward range if skip range is larger and conditions are met
        if len(skip) >= len(forward_ranges[y]) and forward_ranges[y][0] > skip[0]:
            forward_ranges[y] = skip[:len(forward_ranges[y])]
            # trim used parts
            skip_ranges[x] = skip[len(forward_ranges[y]):]

# compute the final result
part2_result = sum(i * j for i, forward in enumerate(forward_ranges) for j in forward)
print("Part 2 Result:", part2_result)
