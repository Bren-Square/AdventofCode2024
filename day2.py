"""
    AoC Day 2
    Brendan Swigart
"""

# Part 1 functions
def is_sorted(nums):
    """
        checks if list of numbers is ascending or descending
        Args: nums (list): list of integers.
        Returns: bool: returns True if asc or desc, False otherwise
    """
    # Empty lists are technically sorted
    if not nums:
        return True
    # all function checks if all items in a list are True
    ascending = all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
    descending = all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))
    return ascending or descending


def check_diff(nums):
    """
        Checks if any two adjacent digits differ by between 1 and 3
    """
    for i in range(len(nums) - 1):
        abs_diff = abs(nums[i] - nums[i + 1])
        if abs_diff not in (1, 2, 3):
            return False
    return True


# part 2 function
def pop_and_check(nums):
    """
        Checks if removing a single element from the list
        will make it valid (sorted and check_diff).
    """
    for i in range(len(nums)):  # Loop indices
        popped_list = nums[:i] + nums[i+1:]  # Remove current element
        if is_sorted(popped_list) and check_diff(popped_list):
            return True
    return False


# Part 1 and 2 baseline logic
# get values from text file
PATH = 'day2.txt'
with open(PATH, 'r', encoding="utf-8") as file:
    reports = file.read()

# get list of reports
report_list = reports.strip().split('\n')
# declare report counts to zero
report_count = 0 # pylint: disable=invalid-name
popped_report_count = 0 # pylint: disable=invalid-name

# loop through reports
for report in report_list:
    # split report numbers into list of ints
    report_numbers = [int(x) for x in report.split()]
    if is_sorted(report_numbers) and check_diff(report_numbers):
        report_count += 1
    elif pop_and_check(report_numbers):
        popped_report_count += 1


print("initial report count: " + str(report_count))
print("corrected report count: " + str(popped_report_count))
print("total report count: " + str(report_count + popped_report_count))
