"""
    Advent of Code Day 11
    Brendan Swigart
"""

from collections import defaultdict

# finally, a test input that can fit on one line
test_input = "3279 998884 1832781 517 8 18864 28 0" # pylint: disable=invalid-name

# cast to list
test_list = test_input.split()

# do it again, this time with compression
def process_digit(digit: int, count: int, new_counts: dict):
    # process single digit keeping track of its frequency.

    # first rule
    if digit == 0:
        new_counts[1] += count
    # FINALLY FOUND A REASON TO USE A WALRUS OPERATOR
    elif len(num_string := str(digit)) % 2 == 0:
        mid = len(num_string) // 2
        l, r = map(int, (num_string[:mid], num_string[mid:]))
        new_counts[l] += count
        new_counts[r] += count
    # third rule
    else:
        eleventh_power = digit * 2024
        new_counts[eleventh_power] += count


def recursive_process(digit_list: list, iterations: int) -> dict:
    # process list with frequency compression.

    # init counts with input list
    # counts frequency of each entry in the list.
    counts = defaultdict(int)
    for item in digit_list:
        counts[int(item)] += 1

    # iterate x number of times
    for _ in range(iterations):
        # placeholder count dictionary
        new_counts = defaultdict(int)
        # go through each entry and run process_digit
        for digit, count in counts.items():
            process_digit(digit, count, new_counts)
        # update original counts with new counts
        counts = new_counts

    return counts


# get compressed values for part 1 and 2
part_one_count = recursive_process(test_list, 25)
part_two_count = recursive_process(test_list, 75)

# output totals
print(sum(part_one_count.values()))
print(sum(part_two_count.values()))
