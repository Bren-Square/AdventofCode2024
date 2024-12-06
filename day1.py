"""
    AoC Day 1
    Brendan Swigart
    This script assumes that you've pre-parsed your input
    I removed whitespace using vscode regex, replacing it
    with commas and then removed newline characters to make
    one really long string to read into this program.
"""

# get values
PATH = 'day1.txt'
with open(PATH, 'r', encoding="utf-8") as file:
    numbers = file.read()

# setup lists.
number_list = numbers.split(',')
left_numbers = number_list[0::2]
left_numbers = sorted(left_numbers, key=int)
right_numbers = number_list[1::2]
right_numbers = sorted(right_numbers, key=int)
total_distance = 0 # pylint: disable=invalid-name

# iterate and add
for i, _ in enumerate(left_numbers):
    delta = int(left_numbers[i]) - int(right_numbers[i])
    total_distance += abs(int(delta))
# print answer
print(total_distance)

# Part 2
similarity_sum = 0 # pylint: disable=invalid-name
for i, _ in enumerate(left_numbers):
    number_count = right_numbers.count(left_numbers[i])
    similarity_score = int(number_count) * int(left_numbers[i])
    similarity_sum += similarity_score

print(similarity_sum)
