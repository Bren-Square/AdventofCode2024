"""
    AoC Day 7
    Brendan Swigart
    Finally decided to do (mostly) everything in functions...
"""

from itertools import product

def generate_values(nums, target):
    """
        Generates values of all possible equations 
        returns True if any value matches the target.
    Args:
        nums - list
        target - int
    Returns:
        result - int
        bool - bool
    """
    if len(nums) < 2:
        return nums[0] == target

    operators = ['+', '*', '||']
    operator_slots = len(nums) - 1  # Number of slots between numbers

    # Generate ALL THE COMBINATIONS
    for ops in product(operators, repeat=operator_slots):
        result = nums[0]
        valid = True
        # Apply operators sequentially
        for i, op in enumerate(ops):
            if op == '+':
                result += nums[i + 1]
            elif op == '*':
                result *= nums[i + 1]
            elif op == '||':
                # Concatenate current result with the next number
                result = int(str(result) + str(nums[i + 1]))
            else:
                valid = False  # Catch invalid operators
                break
        # if it matches the target, return to be added
        if valid and result == target:
            return result, True
    return 0, False


def process_input(input_text):
    """
        Got tired of for loops outside functions.
        added the splitting/formatting of each line here.
    """
    results = []
    sum_val = 0
    for line in input_text.strip().split('\n'):
        target_str, nums_str = line.split(':')
        target = int(target_str.strip())
        nums = list(map(int, nums_str.strip().split()))
        # Check if any equation can evaluate to the target
        val, is_match = generate_values(nums, target)
        sum_val += val
        results.append(is_match)
    return sum_val, results


# get values
PATH = 'day7.txt'
with open(PATH, 'r', encoding="utf-8") as file:
    text = file.read()


# unpack value and results. Should refactor this to just give the total
# but I'm lazy and this challenge was annoying.
total, resultant_set = process_input(text)
print(total)
