"""
    Advent of Code: Day 5
    Brendan Swigart
"""

# get rules in their own list object
RULES_PATH = 'day5a.txt'
with open(RULES_PATH, 'r', encoding="utf-8") as rules_file:
    rules = rules_file.read()
# get pages to check in their own list object
PAGES_PATH = 'day5b.txt'
with open(PAGES_PATH, 'r', encoding='utf-8') as pages_file:
    pages = pages_file.read()


# create lists and assign a counter for later
pages_list = pages.strip().split('\n')
rules_list = rules.strip().split('\n')
part_two_count = 0 # pylint: disable=invalid-name
part_one_count = 0 # pylint: disable=invalid-name

def correct_page_order(bad_pages: list) -> list:
    """
        Args: bad_pages (list): a list of pages that are out of order
        Returns: list: a list of pages that are in order
    """

    # Create set for rules providing fast/quick access
    rules_set = set(rules_list)

    # Most counterintuitive True/False setup you've ever seen.
    changes_made = True
    while changes_made:
        changes_made = False

        # Iterate through pairs of elements in bad_pages
        for i in range(len(bad_pages) - 1):
            a, b = bad_pages[i], bad_pages[i + 1] # unpack vars

            # When are you ever going to use bubble sort?
            if f"{a}|{b}" not in rules_set:
                # RIGHT HERE MOFO
                bad_pages[i], bad_pages[i + 1] = bad_pages[i + 1], bad_pages[i]
                changes_made = True

    return bad_pages


for page in pages_list:
    page_tokens = page.split(",")
    print_orders = [a + "|" + b for i, a in enumerate(page_tokens) for b in page_tokens[i+1:]]
    should_print = True # pylint: disable=invalid-name
    for order in print_orders:
        if order not in rules_list:
            should_print = False # pylint: disable=invalid-name
    if not should_print:
        print(page_tokens)
        correct_pages = correct_page_order(page_tokens)
        part_two_count += int(correct_pages[len(correct_pages) // 2])
    if should_print:
        part_one_count += int(page_tokens[len(page_tokens) // 2])


print(part_one_count)
print(part_two_count)
