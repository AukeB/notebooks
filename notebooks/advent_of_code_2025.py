import marimo

__generated_with = "0.18.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Imports
    """)
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Helper functions
    """)
    return


@app.function
def read_data(file_path: str, separator: str) -> list[str]:
    """
    Reads a file and returns the content of the file as a list of str objects.
    The separator determines how the file content is split: by commas or new lines.

    Args:
        file_path (str): The path to the file.
        separator (str): The separator for splitting the file content.

    Returns:
        list[str]: A list of strings split based on the separator.
    """
    with open(file_path, "r") as file:
        content = file.read().strip()
        if separator == ",":
            rotation_data = content.split(",")
        elif separator == "\n":
            rotation_data = content.split("\n")
    return rotation_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 1: Secret Entrance
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Elves have good news and bad news.

    The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time. The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole! To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

    Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

    "Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

    The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.

    The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

    So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0. Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0. So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

    The dial starts by pointing at 50.

    You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

    For example, suppose the attached document contained the following rotations:

    ```
    L68
    L30
    R48
    L5
    R60
    L55
    L1
    L99
    R14
    L82
    ```

    Following these rotations would cause the dial to move as follows:

    ```
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.
    Because the dial points at 0 a total of three times during this process, the password in this example is 3.
    ```

    Analyze the rotations in your attached document. What's the actual password to open the door?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_1_1_find_exact_zeros(
    rotation_data: list[str],
    start_position: int = 50,
) -> int:
    """
    Calculates the number of times the dial points at 0 after processing a sequence of rotations.

    This function simulates the movement of a circular dial, which starts at a given position (default is 50), 
    and is rotated based on a list of rotation instructions. Each rotation instruction specifies a direction 
    ('L' for left, 'R' for right) and a distance (number of clicks). The dial wraps around if it exceeds 
    the range of 0 to 99. The function counts how many times the dial points at 0 during the sequence of rotations.

    Args:
        rotation_data (list[str]): A list of rotation instructions in the format 'L<number>' or 'R<number>'.
        start_position (int, optional): The starting position of the dial. Defaults to 50.

    Returns:
        int: The number of times the dial points at 0 after processing all rotations.
    """
    end_position = start_position
    zero_counter = 0

    for i in range(len(rotation_data)):
        rotation_value = int(rotation_data[i][1:])

        if rotation_data[i].startswith("L"):
            end_position -= rotation_value
        elif rotation_data[i].startswith("R"):
            end_position += rotation_value

        while end_position > 99:
            end_position -= 100
        while end_position < 0:
            end_position += 100

        if end_position == 0:
            zero_counter += 1

    return zero_counter


@app.cell
def _():
    example_rotation_data = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    solution_example_1_1 = exercise_1_1_find_exact_zeros(rotation_data=example_rotation_data)

    assert(solution_example_1_1 == 3)
    return (example_rotation_data,)


@app.cell
def _():
    rotation_data = read_data(file_path="data/aoc_2025/day_1.txt", separator="\n")

    print(exercise_1_1_find_exact_zeros(rotation_data=rotation_data))
    return (rotation_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

    As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

    "Due to newer security protocols, please use password method 0x434C49434B until further notice."

    You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

    Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    ```
    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
    ```

    In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

    Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

    Using password method 0x434C49434B, what is the password to open the door?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_2_1_find_zero_pointings(
    rotation_data: list[str],
    start_position: int = 50
) -> int:
    """
    Calculates the total number of times the dial points at 0 during and after rotations.

    This function simulates the movement of a circular dial, which starts at a given position 
    (default is 50), and is rotated based on a list of rotation instructions. Each rotation 
    instruction specifies a direction ('L' for left, 'R' for right) and a distance (number of clicks). 
    The dial wraps around if it exceeds the range of 0 to 99. The function counts how many times the 
    dial points at 0 either during a rotation or at the end of a rotation.

    Args:
        rotation_data (list[str]): A list of rotation instructions in the format 'L<number>' or 'R<number>'.
        start_position (int, optional): The starting position of the dial. Defaults to 50.

    Returns:
        int: The total number of times the dial points at 0 during and after processing all rotations.
    """
    end_position = start_position
    zero_counter = 0

    for i in range(len(rotation_data)):
        rotation_value = int(rotation_data[i][1:])

        if rotation_data[i].startswith("L"):
            for _ in range(rotation_value):
                end_position -= 1

                if end_position < 0:
                    end_position += 100
                if end_position == 0:
                    zero_counter += 1

        elif rotation_data[i].startswith("R"):
            for _ in range(rotation_value):
                end_position += 1

                if end_position > 99:
                    end_position -= 100
                if end_position == 0:
                    zero_counter += 1

    return zero_counter


@app.cell
def _(example_rotation_data):
    solution_example_1_2 = (exercise_2_1_find_zero_pointings(rotation_data=example_rotation_data))

    assert(solution_example_1_2 == 6)
    return


@app.cell
def _(rotation_data):
    print(exercise_2_1_find_zero_pointings(rotation_data=rotation_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 2: Gift Shop
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

    As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

    As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?

    They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:

    ```
    11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124
    ```
    (The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)

    The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

    Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

    None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)

    Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

    ```
    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.
    ```

    Adding up all the invalid IDs in this example produces 1227775554.

    What do you get if you add up all of the invalid IDs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_2_1_find_invalid_ids(product_id_ranges: list[str]) -> int:
    """
    Identifies invalid product IDs within given ranges and returns their sum.

    This function processes a list of product ID ranges to identify invalid IDs. 
    An invalid ID is defined as a number that consists of a sequence of digits repeated twice (e.g., 55, 6464, 123123). 
    Each range is specified in the format 'start-end', where both start and end are inclusive. 
    The function checks each ID within the range, determines if it is invalid based on the repeated digit pattern, 
    and sums all the invalid IDs.

    Args:
        product_id_ranges (list[str]): A list of product ID ranges in the format 'start-end'.

    Returns:
        int: The sum of all invalid IDs found within the given ranges.
    """
    invalid_ids = []

    for product_range in product_id_ranges:
        separated_ids = product_range.split("-")
        first_id = int(separated_ids[0])
        last_id = int(separated_ids[1])

        for id in range(first_id, last_id+1):
            id = str(id)
            num_digits = len(id)

            for i in range(1, num_digits):
                is_divisible = (num_digits % i == 0)

                if is_divisible:
                    num_digits_to_check = i
                    num_repeats = int(num_digits / i)

                    id_parts = []

                    for j in range(num_repeats):
                        if num_repeats == 2:
                            id_parts.append(id[j*i:(j+1)*i])

                    if id_parts:
                        if id_parts[0] == id_parts[1]:
                            invalid_ids.append(int(id))

    return sum(invalid_ids)


@app.cell
def _():
    example_product_id_ranges = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124"
    ]

    solution_example_2_1 = (exercise_2_1_find_invalid_ids(product_id_ranges=example_product_id_ranges))

    assert(solution_example_2_1, 1227775554)
    return (example_product_id_ranges,)


@app.cell
def _():
    product_id_ranges = read_data(file_path="data/aoc_2025/day_2.txt", separator=",")

    print(exercise_2_1_find_invalid_ids(product_id_ranges=product_id_ranges))
    return (product_id_ranges,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

    Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

    From the same example as before:

    ```
    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.
    Adding up all the invalid IDs in this example produces 4174379265.
    ```

    What do you get if you add up all of the invalid IDs using these new rules?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_2_2_find_invalid_ids(product_id_ranges: list[str]) -> int:
    """
    Identifies invalid product IDs within given ranges and returns their sum using updated rules.

    This function processes a list of product ID ranges to identify invalid IDs based on new rules. 
    An invalid ID is defined as a number that consists of a sequence of digits repeated at least twice 
    (e.g., 12341234, 123123123, 1111111). Each range is specified in the format 'start-end', where both 
    start and end are inclusive. The function checks each ID within the range, determines if it is invalid 
    based on the repeated digit pattern, and sums all the invalid IDs.

    Args:
        product_id_ranges (list[str]): A list of product ID ranges in the format 'start-end'.

    Returns:
        int: The sum of all invalid IDs found within the given ranges based on the updated rules.
    """
    invalid_ids = []

    for product_range in product_id_ranges:
        separated_ids = product_range.split("-")
        first_id = int(separated_ids[0])
        last_id = int(separated_ids[1])

        for id in range(first_id, last_id+1):
            id = str(id)
            num_digits = len(id)

            for i in range(1, num_digits):
                is_divisible = (num_digits % i == 0)

                if is_divisible:
                    num_digits_to_check = i
                    num_repeats = int(num_digits / i)

                    id_parts = []

                    for j in range(num_repeats):
                        if num_digits_to_check >= 1:
                            id_parts.append(id[j*i:(j+1)*i])

                    if id_parts:
                        are_id_parts_equal = True

                        for id_part in id_parts:
                            if id_part != id_parts[0]:
                                are_id_parts_equal = False

                        if are_id_parts_equal and int(id) not in invalid_ids:
                            invalid_ids.append(int(id))

    return sum(invalid_ids)


@app.cell
def _(example_product_id_ranges):
    solution_example_2_2 = (exercise_2_2_find_invalid_ids(product_id_ranges=example_product_id_ranges))

    assert(solution_example_2_2, 4174379265)
    return


@app.cell
def _(product_id_ranges):
    print(exercise_2_2_find_invalid_ids(product_id_ranges=product_id_ranges))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 3 - Lobby
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all offline.

    "Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."
    |
    You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also offline."

    "But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."

    There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their joltage rating, a value from 1 to 9. You make a note of their joltage ratings (your puzzle input). For example:

    ```
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    ```

    The batteries are arranged into banks; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

    You'll need to find the largest possible joltage each bank can produce. In the above example:

    - In 987654321111111, you can make the largest joltage possible, 98, by turning on the first two batteries.
    - In 811111111111119, you can make the largest joltage possible by turning on the batteries labeled 8 and 9, producing 89 jolts.
    - In 234234234234278, you can make 78 by turning on the last two batteries (marked 7 and 8).
    - In 818181911112111, the largest joltage you can produce is 92.

    The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is 98 + 89 + 78 + 92 = 357.

    There are many batteries in front of you. Find the maximum joltage possible from each bank; what is the total output joltage?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_3_1_find_largest_joltage(
    joltage_ratings: list[str],
    num_batteries: int = 2,
) -> int:
    """
    Calculates the total maximum joltage that can be produced across all banks of batteries.

    This function processes a list of battery banks, where each bank contains battery joltage ratings 
    as a string of digits. For each bank, it identifies the largest possible joltage that can be produced 
    by turning on a specified number of batteries (default is 2). The joltage for a bank is determined by 
    forming a number using the digits of the selected batteries in the order they appear. The function 
    sums the maximum joltage from all banks to calculate the total output.

    Args:
        joltage_ratings (list[str]): A list of strings, where each string represents the joltage ratings 
            of batteries in a single bank.
        num_batteries (int, optional): The number of batteries to turn on in each bank to maximize 
            the joltage. Defaults to 2.

    Returns:
        int: The total maximum joltage produced across all banks.
    """
    total_joltage_over_all_banks = 0

    for bank_index, bank in enumerate(joltage_ratings):
        largest_battery_ratings = []
        largest_battery_index = -1

        for i in range(num_batteries):
            largest_battery_rating = 0

            for battery_index in range(len(bank) - num_batteries + i, largest_battery_index, -1):

                battery_joltage_rating = int(bank[battery_index])
                if battery_joltage_rating >= largest_battery_rating:
                    largest_battery_rating = battery_joltage_rating
                    largest_battery_index = battery_index

            largest_battery_ratings.append(largest_battery_rating)

        total_per_bank = 0

        for i in range(len(largest_battery_ratings) -1, -1, -1):
            total_per_bank += largest_battery_ratings[i] * 10**(len(largest_battery_ratings) - 1 - i)

        total_joltage_over_all_banks += total_per_bank

    return total_joltage_over_all_banks


@app.cell
def _():
    example_joltage_ratings = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]

    solution_example_3_1 = exercise_3_1_find_largest_joltage(
        joltage_ratings=example_joltage_ratings
    )

    assert(solution_example_3_1, 357)
    return (example_joltage_ratings,)


@app.cell
def _():
    joltage_ratings = read_data(file_path="data/aoc_2025/day_3.txt", separator="\n")

    print(exercise_3_1_find_largest_joltage(
       joltage_ratings=joltage_ratings
    ))
    return (joltage_ratings,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

    Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

    The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

    Consider again the example from before:

    ```
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    ```

    Now, the joltages are much larger:

    - In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    - In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    - In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    - In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

    The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

    What is the new total output joltage?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_3_2_find_largest_joltage(
    joltage_ratings: list[str],
    num_batteries: int = 12,
) -> int:
    """
    Calculates the total maximum joltage that can be produced across all banks of batteries using a larger number of batteries.

    This function processes a list of battery banks, where each bank contains battery joltage ratings 
    as a string of digits. For each bank, it identifies the largest possible joltage that can be produced 
    by turning on a specified number of batteries (default is 12). The joltage for a bank is determined by 
    forming a number using the digits of the selected batteries in the order they appear. The function 
    sums the maximum joltage from all banks to calculate the total output.

    Args:
        joltage_ratings (list[str]): A list of strings, where each string represents the joltage ratings 
            of batteries in a single bank.
        num_batteries (int, optional): The number of batteries to turn on in each bank to maximize 
            the joltage. Defaults to 12.

    Returns:
        int: The total maximum joltage produced across all banks using the specified number of batteries.
    """
    total_joltage_over_all_banks = 0

    for bank_index, bank in enumerate(joltage_ratings):
        largest_battery_ratings = []
        largest_battery_index = -1

        for i in range(num_batteries):
            largest_battery_rating = 0

            for battery_index in range(len(bank) - num_batteries + i, largest_battery_index, -1):

                battery_joltage_rating = int(bank[battery_index])
                if battery_joltage_rating >= largest_battery_rating:
                    largest_battery_rating = battery_joltage_rating
                    largest_battery_index = battery_index

            largest_battery_ratings.append(largest_battery_rating)

        total_per_bank = 0

        for i in range(len(largest_battery_ratings) -1, -1, -1):
            total_per_bank += largest_battery_ratings[i] * 10**(len(largest_battery_ratings) - 1 - i)

        total_joltage_over_all_banks += total_per_bank

    return total_joltage_over_all_banks


@app.cell
def _(example_joltage_ratings):
    solution_example_3_2 = exercise_3_2_find_largest_joltage(
        joltage_ratings=example_joltage_ratings
    )

    assert(solution_example_3_2, 3121910778619)
    return


@app.cell
def _(joltage_ratings):
    print(exercise_3_2_find_largest_joltage(
        joltage_ratings=joltage_ratings
    ))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Day 4 - Printing Department
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

    Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

    "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

    If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

    The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

    For example:

    ```
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.
    ```

    The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

    In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

    ```
    ..xx.xx@x.
    x@@.@.@.@@
    @@@@@.x.@@
    @.@@@@..@.
    x@.@@@@.@x
    .@@@@@@@.@
    .@.@.@.@@@
    x.@@@.@@@@
    .@@@@@@@@.
    x.x.@@@.x.
    ```

    Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_4_1_find_accessible_paper_rolls(
    paper_roll_data: list[str],
    max_neighbours: int = 3
) -> int:
    """
    Determines the number of paper rolls that can be accessed by forklifts.

    The function evaluates each paper roll in a grid (provided as input) to check
    if it has fewer than or equal to a specified number of adjacent paper rolls.
    Forklifts can access a roll of paper if there are fewer than `max_neighbours`
    paper rolls in the eight adjacent positions.

    Args:
        paper_roll_data (list[str]): A list of strings representing the grid of paper rolls.
            Each string corresponds to a row in the grid, where '@' represents a paper roll
            and '.' represents an empty space.
        max_neighbours (int): The maximum number of allowable adjacent paper rolls for a forklift
            to access a roll. Defaults to 3.

    Returns:
        int: The count of paper rolls that can be accessed by forklifts.
    """
    paper_roll_matrix = []

    for paper_roll_row in paper_roll_data:
        paper_roll_row_list: list[str] = []

        for element in paper_roll_row:
            paper_roll_row_list.append(element)

        paper_roll_matrix.append(paper_roll_row_list)

    paper_roll_count = 0

    for i in range(len(paper_roll_matrix)):
        for j in range(len(paper_roll_matrix[i])):
            if paper_roll_matrix[i][j] == "@":
                num_neighbours = 0

                all_neighbour_coordinates = [
                    (i-1, j-1),
                    (i-1, j),
                    (i-1, j+1),
                    (i, j-1),
                    (i, j+1),
                    (i+1, j-1),
                    (i+1, j),
                    (i+1, j+1),
                ]

                for neighbour_coordinates in all_neighbour_coordinates:
                    if (
                        neighbour_coordinates[0] >= 0 and 
                        neighbour_coordinates[0] < len(paper_roll_matrix) and
                        neighbour_coordinates[1] >= 0 and 
                        neighbour_coordinates[1] < len(paper_roll_matrix[i])
                    ):
                        if paper_roll_matrix[neighbour_coordinates[0]][neighbour_coordinates[1]] == "@":
                            num_neighbours += 1

                if num_neighbours <= max_neighbours:
                    paper_roll_count += 1

    return paper_roll_count


@app.cell
def _():
    example_paper_roll_data = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    example_solution_4_1 = exercise_4_1_find_accessible_paper_rolls(
        paper_roll_data=example_paper_roll_data
    )

    assert example_solution_4_1 == 13
    return (example_paper_roll_data,)


@app.cell
def _():
    paper_roll_data = read_data(file_path="data/aoc_2025/day_4.txt", separator="\n")

    print(exercise_4_1_find_accessible_paper_rolls(
        paper_roll_data=paper_roll_data
    ))
    return (paper_roll_data,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Now, the Elves just need help accessing as much of the paper as they can.

    Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

    Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

    ```
    Initial state:
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.

    Remove 13 rolls of paper:
    ..xx.xx@x.
    x@@.@.@.@@
    @@@@@.x.@@
    @.@@@@..@.
    x@.@@@@.@x
    .@@@@@@@.@
    .@.@.@.@@@
    x.@@@.@@@@
    .@@@@@@@@.
    x.x.@@@.x.

    Remove 12 rolls of paper:
    .......x..
    .@@.x.x.@x
    x@@@@...@@
    x.@@@@..x.
    .@.@@@@.x.
    .x@@@@@@.x
    .x.@.@.@@@
    ..@@@.@@@@
    .x@@@@@@@.
    ....@@@...

    Remove 7 rolls of paper:
    ..........
    .x@.....x.
    .@@@@...xx
    ..@@@@....
    .x.@@@@...
    ..@@@@@@..
    ...@.@.@@x
    ..@@@.@@@@
    ..x@@@@@@.
    ....@@@...

    Remove 5 rolls of paper:
    ..........
    ..x.......
    .x@@@.....
    ..@@@@....
    ...@@@@...
    ..x@@@@@..
    ...@.@.@@.
    ..x@@.@@@x
    ...@@@@@@.
    ....@@@...

    Remove 2 rolls of paper:
    ..........
    ..........
    ..x@@.....
    ..@@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@x.
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ...@@.....
    ..x@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ...x@.....
    ...@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ....x.....
    ...@@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...

    Remove 1 roll of paper:
    ..........
    ..........
    ..........
    ...x@@....
    ...@@@@...
    ...@@@@@..
    ...@.@.@@.
    ...@@.@@@.
    ...@@@@@..
    ....@@@...
    ```

    Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

    Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_4_2_iteratively_remove_paper_rolls(
    paper_roll_data: list[str],
    max_neighbours: int = 3
) -> int:
    """
    Determines the total number of paper rolls that can be iteratively removed by forklifts.

    Forklifts can remove a roll of paper if there are fewer than or equal to `max_neighbours`
    rolls of paper in the eight adjacent positions. Removing a roll may make other rolls accessible,
    and the process continues until no more rolls can be removed.

    Args:
        paper_roll_data (list[str]): A list of strings representing the grid of paper rolls.
            Each string corresponds to a row in the grid, where '@' represents a paper roll
            and '.' represents an empty space.
        max_neighbours (int): The maximum number of allowable adjacent paper rolls for a forklift
            to access and remove a roll. Defaults to 3.

    Returns:
        int: The total number of paper rolls removed.
    """
    paper_roll_matrix = []

    for paper_roll_row in paper_roll_data:
        paper_roll_row_list: list[str] = []

        for element in paper_roll_row:
            paper_roll_row_list.append(element)

        paper_roll_matrix.append(paper_roll_row_list)

    total_paper_roll_count = 0
    iterate = True

    while iterate:
        new_matrix = []
        paper_roll_count = 0

        for i in range(len(paper_roll_matrix)):
            new_row = []

            for j in range(len(paper_roll_matrix[i])):
                if paper_roll_matrix[i][j] == "@":
                    num_neighbours = 0

                    all_neighbour_coordinates = [
                        (i-1, j-1),
                        (i-1, j),
                        (i-1, j+1),
                        (i, j-1),
                        (i, j+1),
                        (i+1, j-1),
                        (i+1, j),
                        (i+1, j+1),
                    ]

                    for neighbour_coordinates in all_neighbour_coordinates:
                        if (
                            neighbour_coordinates[0] >= 0 and 
                            neighbour_coordinates[0] < len(paper_roll_matrix) and
                            neighbour_coordinates[1] >= 0 and 
                            neighbour_coordinates[1] < len(paper_roll_matrix[i])
                        ):
                            if paper_roll_matrix[neighbour_coordinates[0]][neighbour_coordinates[1]] == "@":
                                num_neighbours += 1

                    if num_neighbours <= max_neighbours:
                        paper_roll_count += 1
                        new_row.append(".")
                    else:
                        new_row.append("@")
                else:
                    new_row.append(".")

            new_matrix.append(new_row)

        if paper_roll_count > 0:
            total_paper_roll_count += paper_roll_count
            paper_roll_matrix = new_matrix.copy()
        elif paper_roll_count == 0:
            iterate = False

    return total_paper_roll_count


@app.cell
def _(example_paper_roll_data):
    example_solution_4_2 = exercise_4_2_iteratively_remove_paper_rolls(
        paper_roll_data=example_paper_roll_data
    )

    assert(example_solution_4_2, 43)
    return


@app.cell
def _(paper_roll_data):
    print(exercise_4_2_iteratively_remove_paper_rolls(
        paper_roll_data=paper_roll_data
    ))
    return


if __name__ == "__main__":
    app.run()
