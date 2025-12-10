import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", auto_download=["ipynb"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2025
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Generic imports
    """)
    return


@app.cell
def _():
    import marimo as mo

    from collections import defaultdict
    return defaultdict, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants
    """)
    return


@app.cell
def _():
    DATA_DIRECTORY_PATH = "data/aoc_2025"
    # DATA_DIRECTORY_PATH = "../" + DATA_DIRECTORY_PATH
    return (DATA_DIRECTORY_PATH,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Helper functions
    """)
    return


@app.cell
def _():
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

    def convert_string_to_list_of_tuples(str_data: str) -> list[tuple[int]]:
        """
        Convert a string representation of tuples into a list of integer tuples.
    
        Each tuple in the string should be enclosed in parentheses and separated
        by spaces. Elements within a tuple should be comma-separated integers.

        Args:
            str_data (str): The str data representing one or more tuples.

        Returns:
            list[tuple[int]]: The same data but now with the correct variable
                types.
        """
        list_of_tuples = []
        data_split = str_data.split(" ")

        for element in data_split:
            sub_list_elements = element[1:-1].split(",")
            sub_list_elements = [int(number) for number in sub_list_elements]
            list_of_tuples.append(tuple(sub_list_elements))

        return list_of_tuples
    return convert_string_to_list_of_tuples, read_data


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
    Simulate safe dial rotations and count how many times the dial lands on zero.

    The dial is rotated one click at a time. It wraps around from 99 to 0 and
    from 0 to 99. The count increases each time the dial ends a rotation
    pointing at zero.

    Args:
        rotation_data (list[str]): List of rotation instructions, each starting with 'L'
            or 'R' followed by an integer number of clicks.
        start_position (int): Starting value on the dial, between 0 and 99. Defaults
            to 50.

    Returns:
        int: The number of times the dial ends a rotation pointing at zero.
    """
    current_position = start_position
    zero_counter = 0

    for rotation in rotation_data:
        step = 1 if rotation[0] == "R" else -1
        number_of_steps = int(rotation[1:])

        for _ in range(number_of_steps):
            current_position = (current_position + step) % 100

        if not current_position:
            zero_counter += 1

    return zero_counter


@app.cell
def _():
    example_rotation_data = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    solution_example_1_1 = exercise_1_1_find_exact_zeros(rotation_data=example_rotation_data)

    assert solution_example_1_1 == 3
    return (example_rotation_data,)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    rotation_data = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_1.txt", separator="\n")

    print(exercise_1_1_find_exact_zeros(rotation_data=rotation_data))
    return (rotation_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
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
def exercise_1_2_count_zero_clicks(
    rotation_data: list[str],
    start_position: int = 50,
) -> int:
    """
    Count how many times the dial points at zero during the given rotations.

    The dial moves one click at a time. Each instruction starts with 'L' or 'R'
    followed by an integer indicating how many clicks to rotate. The dial wraps
    from 99 to 0 and from 0 to 99. The counter increases every time a single
    click causes the dial to land on zero.

    Args:
        rotation_data (list[str]): List of rotation instructions as strings. Each has a
            direction character ('L' or 'R') followed by an integer number of
            clicks.
        start_position (int): Starting value on the dial, between 0 and 99. Defaults
            to 50.

    Returns:
        int: The total number of times any click causes the dial to land on zero.
    """
    current_position = start_position
    zero_counter = 0

    for rotation in rotation_data:
        step = 1 if rotation[0] == "R" else -1
        number_of_steps = int(rotation[1:])

        for _ in range(number_of_steps):
            current_position = (current_position + step) % 100

            if not current_position:
                zero_counter += 1

    return zero_counter


@app.cell
def _(example_rotation_data):
    solution_example_1_2 = (exercise_1_2_count_zero_clicks(rotation_data=example_rotation_data))

    assert solution_example_1_2 == 6
    return


@app.cell
def _(rotation_data):
    print(exercise_1_2_count_zero_clicks(rotation_data=rotation_data))
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

    assert solution_example_2_1 == 1227775554
    return (example_product_id_ranges,)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    product_id_ranges = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_2.txt", separator=",")

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

    assert solution_example_2_2 == 4174379265
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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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

    assert solution_example_3_1 == 357
    return (example_joltage_ratings,)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    joltage_ratings = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_3.txt", separator="\n")

    print(exercise_3_1_find_largest_joltage(
       joltage_ratings=joltage_ratings
    ))
    return (joltage_ratings,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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

    assert solution_example_3_2 == 3121910778619
    return


@app.cell
def _(joltage_ratings):
    print(exercise_3_2_find_largest_joltage(
        joltage_ratings=joltage_ratings
    ))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 4 - Printing Department
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


@app.cell(hide_code=True)
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

    solution_example_4_1 = exercise_4_1_find_accessible_paper_rolls(
        paper_roll_data=example_paper_roll_data
    )

    assert solution_example_4_1 == 13
    return (example_paper_roll_data,)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    paper_roll_data = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_4.txt", separator="\n")

    print(exercise_4_1_find_accessible_paper_rolls(
        paper_roll_data=paper_roll_data
    ))
    return (paper_roll_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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
    solution_example_4_2 = exercise_4_2_iteratively_remove_paper_rolls(
        paper_roll_data=example_paper_roll_data
    )

    assert solution_example_4_2 == 43
    return


@app.cell
def _(paper_roll_data):
    print(exercise_4_2_iteratively_remove_paper_rolls(
        paper_roll_data=paper_roll_data
    ))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 5 - Cafetaria
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
    As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

    You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

    "If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

    The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

    The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

    ```
    3-5
    10-14
    16-20
    12-18
    ```

    ```
    1
    5
    8
    11
    17
    32
    ```

    The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

    The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

    - Ingredient ID 1 is spoiled because it does not fall into any range.
    - Ingredient ID 5 is fresh because it falls into range 3-5.
    - Ingredient ID 8 is spoiled.
    - Ingredient ID 11 is fresh because it falls into range 10-14.
    - Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
    - Ingredient ID 32 is spoiled.

    So, in this example, 3 of the available ingredient IDs are fresh.

    Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_5_1_identify_fresh_ingredients(
    ingredient_data: list[str],
) -> int:
    """
    Count how many available ingredient IDs are within any fresh ID range.

    The input consists of lines describing inclusive fresh ingredient ID ranges
    (each formatted as two integers separated by a hyphen, e.g. ``"3-5"``),
    followed by a blank line, and then lines containing individual ingredient
    IDs. An ingredient ID is considered fresh if it falls within at least one
    of the provided ranges.

    Args:
        ingredient_data (list[str]): The raw lines from the inventory database.
            These should include fresh ID ranges (two integers separated by a
            hyphen), a blank separator line, and available ingredient IDs.

    Returns:
        int: The number of available ingredient IDs that fall within any
            fresh ID range.
    """
    ingredient_id_ranges = []
    available_ingredient_ids = []

    for ingredient_data_row in ingredient_data:
        ingredient_data_row = ingredient_data_row.strip()

        if "-" in ingredient_data_row:
            separated_ids = ingredient_data_row.split("-")
            first_id = int(separated_ids[0])
            last_id = int(separated_ids[1])
            ingredient_id_ranges.append((first_id, last_id))
        elif ingredient_data_row == "":
            pass
        else:
            available_ingredient_ids.append(int(ingredient_data_row))

    counter = 0

    for ingredient_id in available_ingredient_ids:
        for lb, ub in ingredient_id_ranges:
            if ingredient_id >= lb and ingredient_id <= ub:
                counter += 1
                break

    return counter


@app.cell
def _():
    example_ingredient_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32"
    ]

    solution_example_5_1 = exercise_5_1_identify_fresh_ingredients(
        ingredient_data=example_ingredient_data
    )

    assert solution_example_5_1 == 3
    return (example_ingredient_data,)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    ingredient_data = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_5.txt", separator="\n")

    print(exercise_5_1_identify_fresh_ingredients(
        ingredient_data=ingredient_data
    ))
    return (ingredient_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

    So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

    Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

    ```
    3-5
    10-14
    16-20
    12-18
    ```

    The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

    Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_5_2_find_total_number_of_fresh_ingredients(
    ingredient_data: list[str],
) -> int:
    """
    Calculate the total number of distinct fresh ingredient IDs from a list of ranges.

    This function processes a list of ingredient ID ranges (ignoring individual
    available ingredient IDs) and counts how many unique IDs are considered fresh.
    The key challenge is that ranges can overlap, so a naive count could
    double-count IDs. To handle this, the function iteratively breaks ranges
    into subranges and resolves overlaps until all ranges are non-overlapping.

    High-level approach:
        1. Parse the input to extract all ingredient ID ranges as (start, end) tuples.
        2. Maintain a list of "non-overlapping" ranges and iteratively process each
           initial range against this list:
              - If a range overlaps with existing ranges, split it into subranges
                to isolate the non-overlapping portions.
              - If a range is entirely contained in an existing range, it is ignored.
        3. Repeat this process until no further changes occur, i.e., until the
           set of ranges reaches a stable state (a fixpoint).
        4. Sum the lengths of all non-overlapping ranges to get the total count
           of unique fresh ingredient IDs.

    Args:
        ingredient_data (list[str]): A list of strings representing the ingredient
            database. Each string is either a fresh ID range formatted as
            two integers separated by a hyphen (e.g., "3-5") or a blank line
            separating sections. Individual ingredient IDs are ignored.

    Returns:
        int: The total number of distinct ingredient IDs that are considered
            fresh according to the provided ranges.
    """
    intial_ingredient_id_ranges = []
    non_overlapping_ingredient_id_ranges = []

    for ingredient_data_row in ingredient_data:
        ingredient_data_row = ingredient_data_row.strip()

        if "-" in ingredient_data_row:
            separated_ids = ingredient_data_row.split("-")
            first_id = int(separated_ids[0])
            last_id = int(separated_ids[1])
            intial_ingredient_id_ranges.append((first_id, last_id))
        else:
            pass

    iterate = True

    while iterate:        
        for (first_id, last_id) in intial_ingredient_id_ranges:            
            updated_range = []
            entirely_covered = False

            for lb, ub in non_overlapping_ingredient_id_ranges:
                if first_id < lb:
                    if last_id < lb:
                        pass
                    elif last_id >= lb and last_id <= ub:
                        updated_range.append((first_id, lb - 1))
                        break
                    elif last_id > ub:
                        updated_range.append((first_id, lb - 1))
                        updated_range.append((ub + 1, last_id))
                        break
                elif first_id >= lb and first_id <= ub:
                    if last_id <= ub:
                        entirely_covered = True
                    elif last_id > ub:
                        updated_range.append((ub + 1, last_id))
                        break
                elif first_id > ub:
                    pass

            if not updated_range and entirely_covered == False:
                updated_range.append((first_id, last_id))

            if updated_range:
                for (first_id, last_id) in updated_range:
                    if (first_id, last_id) not in non_overlapping_ingredient_id_ranges:
                        non_overlapping_ingredient_id_ranges.append((first_id, last_id))

        if sorted(intial_ingredient_id_ranges) == sorted(non_overlapping_ingredient_id_ranges):
            iterate = False
        else:
            intial_ingredient_id_ranges = non_overlapping_ingredient_id_ranges.copy()
            non_overlapping_ingredient_id_ranges = []

    counter = 0

    for (first_id, last_id) in non_overlapping_ingredient_id_ranges:
        counter += len(range(first_id, last_id)) + 1

    return counter


@app.cell
def _(example_ingredient_data):
    solution_example_5_2 = exercise_5_2_find_total_number_of_fresh_ingredients(ingredient_data=example_ingredient_data)

    assert solution_example_5_2 == 14
    return


@app.cell
def _(ingredient_data):
    print(exercise_5_2_find_total_number_of_fresh_ingredients(ingredient_data=ingredient_data))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 6 - Trash Compactor
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
    After helping the Elves in the kitchen, you were taking a break and helping them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!

    A brief fall later, you find yourself in a garbage smasher. Unfortunately, the door's been magnetically sealed.

    As you try to find a way out, you are approached by a family of cephalopods! They're pretty sure they can get the door open, but it will take some time. While you wait, they're curious if you can help the youngest cephalopod with her math homework.

    Cephalopod math doesn't look that different from normal math. The math worksheet (your puzzle input) consists of a list of problems; each problem has a group of numbers that need to either be either added (+) or multiplied (*) together.

    However, the problems are arranged a little strangely; they seem to be presented next to each other in a very long horizontal list. For example:

    ```
    123 328  51 64
     45 64  387 23
      6 98  215 314
    *   +   *   +
    ```

    Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol for the operation that needs to be performed. Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.

    So, this worksheet contains four problems:

    - 123 * 45 * 6 = 33210
    - 328 + 64 + 98 = 490
    - 51 * 387 * 215 = 4243455
    - 64 + 23 + 314 = 401

    To check their work, cephalopod students are given the grand total of adding together all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.

    Of course, the actual worksheet is much wider. You'll need to make sure to unroll it completely so that you can read the problems clearly.

    Solve the problems on the math worksheet. What is the grand total found by adding together all of the answers to the individual problems?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_6_1_help_with_math_homework(
    math_homework: list[str]
) -> int:
    """
    Parses and solves a horizontally unrolled cephalopod math worksheet.

    Each column in the input represents one math problem. A problem consists of
    several numbers stacked vertically, with either '+' or '*' at the bottom
    indicating whether all numbers in that column should be added or multiplied.

    Columns are separated by whitespace, and the horizontal alignment of numbers
    is irrelevant. This function reconstructs the worksheet by splitting each
    row into meaningful tokens (integers or operators), then processes the grid
    column by column.

    For each column:
      - Read upward to collect all numbers.
      - Read the bottom cell to determine whether to sum or multiply them.
      - Compute the column’s result.

    The final answer is the sum of all individual column results.

    Args:
        math_homework (list[str]): The raw worksheet input, where each string is 
            one row of the printed cephalopod homework.

    Returns
        int: The grand total: the sum of the results of all column-wise problems.
    """
    mult_and_add_matrix = []

    for row in math_homework:
        split_row = row.split(" ")
        formatted_row = []

        for row_element in split_row:
            if row_element == "":
                pass
            elif row_element == "+":
                formatted_row.append(row_element)
            elif row_element == "*":
                formatted_row.append(row_element)
            else:
                formatted_row.append(int(row_element))

        mult_and_add_matrix.append(formatted_row)

    total_sum_of_additions_and_multiplications = 0

    for j in range(len(mult_and_add_matrix[0])):
        add_or_multiply = ""
        numbers_to_add_or_multiply = []

        for i in range(len(mult_and_add_matrix) -1, -1, -1):
            matrix_element = mult_and_add_matrix[i][j]

            if i == len(mult_and_add_matrix) - 1:
                if matrix_element == "+":
                    add_or_multiply = "add"
                elif matrix_element == "*":
                    add_or_multiply = "multiply"
            else:
                numbers_to_add_or_multiply.append(matrix_element)

        if add_or_multiply == "add":
            total_sum_of_additions_and_multiplications += sum(numbers_to_add_or_multiply)
        elif add_or_multiply == "multiply":
            product = 1
            for number in numbers_to_add_or_multiply:
                product *= number
            total_sum_of_additions_and_multiplications += product

    return total_sum_of_additions_and_multiplications


@app.cell
def _():
    example_math_homework = [
        "123 328  51 64",
        " 45 64  387 23",
        "  6 98  215 314",
        "*   +   *   +  "
    ]

    solution_example_6_1 = exercise_6_1_help_with_math_homework(math_homework=example_math_homework)

    assert solution_example_6_1 == 4277556
    return (example_math_homework,)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    math_homework = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_6.txt", separator="\n")

    print(exercise_6_1_help_with_math_homework(math_homework=math_homework))
    return (math_homework,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

    Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

    Here's the example worksheet again:

    ```
    123 328  51 64
     45 64  387 23
      6 98  215 314
    *   +   *   +
    ```

    Reading the problems right-to-left one column at a time, the problems are now quite different:

    - The rightmost problem is 4 + 431 + 623 = 1058
    - The second problem from the right is 175 * 581 * 32 = 3253600
    - The third problem from the right is 8 + 248 + 369 = 625
    - Finally, the leftmost problem is 356 * 24 * 1 = 8544

    Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

    Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_6_2_help_with_math_homework(
    math_homework: list[str]
) -> int:
    """
    Compute the grand total of all cephalopod math problems read right-to-left.

    Each puzzle row represents part of a very wide worksheet where multiple
    vertical math problems are arranged side-by-side. In cephalopod math,
    numbers are written top-to-bottom with the most significant digit first,
    and entire problems are read right-to-left, one column at a time.

    This function processes the worksheet by:

    1. Reversing each input row so that scanning left-to-right corresponds to
       the intended cephalopod right-to-left reading order.
    2. Padding all rows with leading spaces to equalize their width, ensuring
       each column accurately represents a digit column across all rows.
    3. Iterating through each column, reconstructing numbers by stacking digits
       from top to bottom.
    4. Detecting a problem boundary when an entire column contains only spaces.
       At that moment, the collected numbers are either summed or multiplied,
       depending on the operator at the bottom of the problem.
    5. Accumulating the results of all problems into a grand total.

    This approach effectively parses the worksheet as a column-wise stream,
    treating each contiguous column block as a single problem and using
    structural whitespace to separate them.

    Args:
        math_homework (list[str]): A list of strings representing the worksheet 
            rows, containing digits, spaces, and '+'/'*' operators.

    Returns:
        int: The grand total obtained by evaluating all parsed right-to-left
            cephalopod math problems.
    """
    character_matrix = []

    for row in math_homework:
        character_row = []
        for character in row[::-1]:
            character_row.append(character)
        character_matrix.append(character_row)

    max_row_length = 0

    for row in character_matrix:
        if len(row) > max_row_length:
            max_row_length = len(row)

    for i, row in enumerate(character_matrix):
        row_length_difference = max_row_length - len(row)
        for _ in range(row_length_difference):
            character_matrix[i].insert(0, " ")
        character_matrix[i].append(" ")

    total_sum_of_additions_and_multiplications = 0
    add_or_multiply = ""
    numbers_to_add_or_multiply = []

    for j in range(len(character_matrix[0])):
        only_spaces_in_column = True
        number: str = ""

        for i in range(len(character_matrix)):
            matrix_element = character_matrix[i][j]

            if matrix_element == " ":
                pass
            elif matrix_element == "+":
                add_or_multiply = "add"
                only_spaces_in_column = False
            elif matrix_element == "*":
                add_or_multiply = "multiply"
                only_spaces_in_column = False
            else:
                number += matrix_element
                only_spaces_in_column = False

        if number:
            numbers_to_add_or_multiply.append(int(number))

        if only_spaces_in_column:
            if add_or_multiply == "add":
                total_sum_of_additions_and_multiplications += sum(numbers_to_add_or_multiply)
            elif add_or_multiply == "multiply":
                product: int = 1
                for n in numbers_to_add_or_multiply:
                    product *= n
                total_sum_of_additions_and_multiplications += product

            add_or_multiply = ""
            numbers_to_add_or_multiply = []

    return total_sum_of_additions_and_multiplications


@app.cell
def _(example_math_homework):
    solution_example_6_2 = exercise_6_2_help_with_math_homework(math_homework=example_math_homework)

    assert solution_example_6_2 == 3263827
    return


@app.cell
def _(math_homework):
    print(exercise_6_2_help_with_math_homework(math_homework=math_homework))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 7 - Laboratories
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
    You thank the cephalopods for the help and exit the trash compactor, finding yourself in the familiar halls of a North Pole research wing.

    Based on the large sign that says "teleporter hub", they seem to be researching teleportation; you can't help but try it for yourself and step onto the large yellow teleporter pad.

    Suddenly, you find yourself in an unfamiliar room! The room has no doors; the only way out is the teleporter. Unfortunately, the teleporter seems to be leaking magic smoke.

    Since this is a teleporter lab, there are lots of spare parts, manuals, and diagnostic equipment lying around. After connecting one of the diagnostic tools, it helpfully displays error code 0H-N0, which apparently means that there's an issue with one of the tachyon manifolds.

    You quickly locate a diagram of the tachyon manifold (your puzzle input). A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward. Tachyon beams pass freely through empty space (.). However, if a tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate right of the splitter.

    For example:

    ```
    .......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    In this example, the incoming tachyon beam (|) extends downward from S until it reaches the first splitter:

    ```
    .......S.......
    .......|.......
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    At that point, the original beam stops, and two new beams are emitted from the splitter:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    Those beams continue downward until they reach more splitters:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ......|.|......
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    At this point, the two splitters create a total of only three tachyon beams, since they are both dumping tachyons into the same place between them:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ......|.|......
    .....|^|^|.....
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............
    ```

    This process continues until all of the tachyon beams reach a splitter or exit the manifold:

    ```
    .......S.......
    .......|.......
    ......|^|......
    ......|.|......
    .....|^|^|.....
    .....|.|.|.....
    ....|^|^|^|....
    ....|.|.|.|....
    ...|^|^|||^|...
    ...|.|.|||.|...
    ..|^|^|||^|^|..
    ..|.|.|||.|.|..
    .|^|||^||.||^|.
    .|.|||.||.||.|.
    |^|^|^|^|^|||^|
    |.|.|.|.|.|||.|
    ```

    To repair the teleporter, you first need to understand the beam-splitting properties of the tachyon manifold. In this example, a tachyon beam is split a total of 21 times.

    Analyze your manifold diagram. How many times will the beam be split?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_7_1_find_number_of_beam_splits(
    tachyon_manifold: list[str]
) -> int:
    """
    Count the total number of times tachyon beams are split in a manifold.

    A tachyon beam starts at the location marked 'S' in the top row and moves
    downward. Beams pass freely through empty spaces ('.') and are split when
    they encounter a splitter ('^'). When a splitter is hit, the beam stops
    and two new beams are emitted from the immediate left and right positions
    of the splitter. Overlapping beams in the same column are counted only
    once per row.

    Args:
        tachyon_manifold (list[str]): A list of strings representing the grid
            of the tachyon manifold. 'S' marks the starting point, '.' is empty
            space, and '^' is a splitter.

    Returns:
        int: The total number of beam splits that occur in the manifold.
    """
    beam_split_counter: int = 0
    beam_x_coordinates: set[int] = {tachyon_manifold[0].index("S")}

    for row_index in range(len(tachyon_manifold) - 1):
        new_beam_x_coordinates = set()

        for x in beam_x_coordinates:
            if tachyon_manifold[row_index+1][x] == "^":
                new_beam_x_coordinates.add(x-1)
                new_beam_x_coordinates.add(x+1)
                beam_split_counter += 1
            else:
                new_beam_x_coordinates.add(x)

        beam_x_coordinates = new_beam_x_coordinates

    return beam_split_counter


@app.cell
def _():
    example_tachyon_manifold = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]

    solution_example_7_1 = exercise_7_1_find_number_of_beam_splits(tachyon_manifold=example_tachyon_manifold)

    assert solution_example_7_1 == 21
    return (example_tachyon_manifold,)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    tachyon_manifold = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_7.txt", separator="\n")

    print(exercise_7_1_find_number_of_beam_splits(tachyon_manifold=tachyon_manifold))
    return (tachyon_manifold,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    With your analysis of the manifold complete, you begin fixing the teleporter. However, as you open the side of the teleporter to replace the broken manifold, you are surprised to discover that it isn't a classical tachyon manifold - it's a quantum tachyon manifold.

    With a quantum tachyon manifold, only a single tachyon particle is sent through the manifold. A tachyon particle takes both the left and right path of each splitter encountered.

    Since this is impossible, the manual recommends the many-worlds interpretation of quantum tachyon splitting: each time a particle reaches a splitter, it's actually time itself which splits. In one timeline, the particle went left, and in the other timeline, the particle went right.

    To fix the manifold, what you really need to know is the number of timelines active after a single particle completes all of its possible journeys through the manifold.

    In the above example, there are many timelines. For instance, there's the timeline where the particle always went left:

    ```
    .......S.......
    .......|.......
    ......|^.......
    ......|........
    .....|^.^......
    .....|.........
    ....|^.^.^.....
    ....|..........
    ...|^.^...^....
    ...|...........
    ..|^.^...^.^...
    ..|............
    .|^...^.....^..
    .|.............
    |^.^.^.^.^...^.
    |..............
    ```

    Or, there's the timeline where the particle alternated going left and right at each splitter:

    ```
    .......S.......
    .......|.......
    ......|^.......
    ......|........
    ......^|^......
    .......|.......
    .....^|^.^.....
    ......|........
    ....^.^|..^....
    .......|.......
    ...^.^.|.^.^...
    .......|.......
    ..^...^|....^..
    .......|.......
    .^.^.^|^.^...^.
    ......|........
    ```

    Or, there's the timeline where the particle ends up at the same point as the alternating timeline, but takes a totally different path to get there:

    ```
    .......S.......
    .......|.......
    ......|^.......
    ......|........
    .....|^.^......
    .....|.........
    ....|^.^.^.....
    ....|..........
    ....^|^...^....
    .....|.........
    ...^.^|..^.^...
    ......|........
    ..^..|^.....^..
    .....|.........
    .^.^.^|^.^...^.
    ......|........
    ```

    In this example, in total, the particle ends up on 40 different timelines.

    Apply the many-worlds interpretation of quantum tachyon splitting to your manifold diagram. In total, how many different timelines would a single tachyon particle end up on?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def exercise_7_2_find_number_of_timelines(defaultdict):
    def exercise_7_2_find_number_of_timelines(
        tachyon_manifold: list[str]
    ) -> int:
        """
        Count the total number of quantum timelines for a single tachyon particle
        traversing a quantum tachyon manifold using the many-worlds interpretation.

        Each splitter ('^') splits the current timeline into two: one going left
        and one going right. Timelines do not merge; every possible path is counted
        as a distinct timeline. The particle starts at the location marked 'S' in
        the top row and moves downward, creating new timelines at each splitter.

        Args:
            tachyon_manifold (list[str]): A list of strings representing the quantum
                tachyon manifold. 'S' marks the starting point, '.' is empty space,
                and '^' is a splitter.

        Returns:
            int: Total number of unique timelines after the particle traverses the manifold.
        """
        timeline_counter = {tachyon_manifold[0].index("S"): 1}

        for i in range(len(tachyon_manifold) - 1):            
            beam_counter_per_row = defaultdict(int)

            for x, count in timeline_counter.items():
                if tachyon_manifold[i+1][x] == "^":
                    beam_counter_per_row[x-1] += count
                    beam_counter_per_row[x+1] += count
                else:
                    beam_counter_per_row[x] += count

            timeline_counter = beam_counter_per_row

        total_number_of_timelines = sum(timeline_counter.values())
        return total_number_of_timelines
    return (exercise_7_2_find_number_of_timelines,)


@app.cell
def _(example_tachyon_manifold, exercise_7_2_find_number_of_timelines):
    solution_example_7_2 = exercise_7_2_find_number_of_timelines(tachyon_manifold=example_tachyon_manifold)

    assert solution_example_7_2 == 40
    return


@app.cell
def _(exercise_7_2_find_number_of_timelines, tachyon_manifold):
    print(exercise_7_2_find_number_of_timelines(tachyon_manifold=tachyon_manifold))
    return


@app.function
def exercise_7_2_find_number_of_timelines_iterative(
    tachyon_manifold: list[str]
) -> int:
    """
    Count the total number of quantum timelines for a single tachyon particle
    traversing a quantum tachyon manifold using an iterative DFS approach.

    A single tachyon particle starts at 'S' in the top row and moves downward.
    Each splitter ('^') creates two new timelines: one moving left and one
    moving right. Empty cells ('.') allow the particle to continue straight down.
    This function explores all possible paths iteratively, using backtracking
    to account for all splits.

    Args:
        tachyon_manifold (list[str]): A list of strings representing the quantum
            tachyon manifold. 'S' marks the starting point, '.' is empty space,
            and '^' is a splitter.

    Returns:
        int: Total number of unique timelines after the particle traverses the manifold.
    """

    def propagate_beam_downward(
        beam_x_coordinates: list[int],
        choices: list[str],
        tachyon_manifold: list[str],
    ) -> tuple[list[int], list[str]]:
        """
        Propagate the beam downward through the manifold until the bottom is reached.

        For each row below the current beam position:
        - If the cell is a splitter ('^'), a left branch is chosen and recorded in choices.
        - If the cell is empty ('.'), the beam continues straight down.

        Args:
            beam_x_coordinates (list[int]): Current x-coordinates of the beam path.
            choices (list[str]): List of choices taken so far ('L', 'R', '-').
            tachyon_manifold (list[str]): The full quantum tachyon manifold grid.

        Returns:
            tuple[list[int], list[str]]: Updated beam x-coordinates and choices after
                propagating to the bottom of the manifold.
        """
        while len(beam_x_coordinates) < len(tachyon_manifold):
            x = beam_x_coordinates[-1]
            char_below = tachyon_manifold[len(beam_x_coordinates)][x]

            # Always go left when encountering a splitter.
            if char_below == "^":
                choices.append("L")
                beam_x_coordinates.append(x - 1)
            elif char_below == ".":
                choices.append("-")
                beam_x_coordinates.append(x)

        return beam_x_coordinates, choices

    timeline_counter = 1
    choices = []
    beam_x_coordinates = [tachyon_manifold[0].index("S")]

    beam_x_coordinates, choices = propagate_beam_downward(
        beam_x_coordinates, choices, tachyon_manifold
    )

    while True:
        for i in range(len(beam_x_coordinates) - 1, -1, -1):
            if choices[i - 1] == "L":
                # Backtrack to the previous choice.
                beam_x_coordinates = beam_x_coordinates[:i].copy()
                choices = choices[:i - 1].copy()

                # Now take the right branch instead.
                choices.append("R")
                beam_x_coordinates.append(beam_x_coordinates[-1] + 1)

                beam_x_coordinates, choices = propagate_beam_downward(
                    beam_x_coordinates, choices, tachyon_manifold
                )

                timeline_counter += 1
                break
        else:
            break

    return timeline_counter


@app.cell
def _(example_tachyon_manifold):
    solution_example_7_2_v2 = exercise_7_2_find_number_of_timelines_iterative(tachyon_manifold=example_tachyon_manifold)

    assert solution_example_7_2_v2 == 40
    return


@app.cell
def _():
    # I think this code will give the correct answer, however because of the iterative approach,
    # and the scaling with 2 to the power of the number of rows in the Tachyon manifold diagram,
    # this will take way too much time. I don't know how long exactly, but it's not a feasible solution.

    # exercise_7_2_find_number_of_timelines_iterative(tachyon_manifold=tachyon_manifold)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 8 - Playground
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
    Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

    You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

    Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical junction boxes.

    Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

    The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

    For example:

    ```
    162,817,812
    57,618,57
    906,360,560
    592,479,940
    352,342,300
    466,668,158
    542,29,236
    431,825,988
    739,650,466
    52,470,668
    216,146,977
    819,987,18
    117,168,530
    805,96,715
    346,949,466
    970,615,88
    941,993,340
    862,61,35
    984,92,344
    425,690,689
    ```

    This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

    To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

    By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

    Now, the two junction boxes which are closest together but aren't already directly connected are 162,817,812 and 431,825,988. After connecting them, since 162,817,812 is already connected to another junction box, there is now a single circuit which contains three junction boxes and an additional 17 circuits which contain one junction box each.

    The next two junction boxes to connect are 906,360,560 and 805,96,715. After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

    The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!

    This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. They would like to know how big the circuits will be.

    After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.

    Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. Afterward, what do you get if you multiply together the sizes of the three largest circuits?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    return


@app.cell
def _():
    example_junction_positions = [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]
    return


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    junction_positions = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_8.txt", separator="\n")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

    Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

    Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 9 - Movie Theater
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
    You slide down the firepole in the corner of the playground and land in the North Pole base movie theater!

    The movie theater has a big tile floor with an interesting pattern. Elves here are redecorating the theater by switching out some of the square tiles in the big grid they form. Some of the tiles are red; the Elves would like to find the largest rectangle that uses red tiles for two of its opposite corners. They even have a list of where the red tiles are located in the grid (your puzzle input).

    For example:

    ```
    7,1
    11,1
    11,7
    9,7
    9,5
    2,5
    2,3
    7,3
    ```

    Showing red tiles as # and other tiles as ., the above arrangement of red tiles would look like this:

    ```
    ..............
    .......#...#..
    ..............
    ..#....#......
    ..............
    ..#......#....
    ..............
    .........#.#..
    ..............
    ```

    You can choose any two red tiles as the opposite corners of your rectangle; your goal is to find the largest rectangle possible.

    For example, you could make a rectangle (shown as O) with an area of 24 between 2,5 and 9,7:

    ```
    ..............
    .......#...#..
    ..............
    ..#....#......
    ..............
    ..OOOOOOOO....
    ..OOOOOOOO....
    ..OOOOOOOO.#..
    ..............
    ```

    Or, you could make a rectangle with area 35 between 7,1 and 11,7:

    ```
    ..............
    .......OOOOO..
    .......OOOOO..
    ..#....OOOOO..
    .......OOOOO..
    ..#....OOOOO..
    .......OOOOO..
    .......OOOOO..
    ..............
    ```

    You could even make a thin rectangle with an area of only 6 between 7,3 and 2,3:

    ```
    ..............
    .......#...#..
    ..............
    ..OOOOOO......
    ..............
    ..#......#....
    ..............
    .........#.#..
    ..............
    ```

    Ultimately, the largest rectangle you can make in this example has area 50. One way to do this is between 2,5 and 11,1:

    ```
    ..............
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..OOOOOOOOOO..
    ..............
    .........#.#..
    ..............
    ```

    Using two red tiles as opposite corners, what is the largest area of any rectangle you can make?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_9_1_find_largest_rectangle(
    red_tile_coordinates: list[str]
) -> int:
    """
    Find the largest possible rectangle area formed by any two red tiles as opposite corners.

    Each coordinate is given as a string "x,y". Two tiles define a rectangle whose area is
    computed as (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1). All unique tile pairs are evaluated,
    and the largest resulting rectangle area is returned.

    Args:
        red_tile_coordinates (list[str]): List of red tile positions as "x,y" strings.

    Returns:
        int: The largest rectangle area formed by any pair of red tiles.
    """
    red_tile_coordinates = [
        [int(num) for num in row.split(",")] for row in red_tile_coordinates
    ]

    largest_area = 0

    for i in range(len(red_tile_coordinates)):
        for j in range(i):
            c1 = red_tile_coordinates[i]
            c2 = red_tile_coordinates[j]

            rectangle_area = (1 + abs(c1[0]-c2[0])) * (1 + abs(c1[1]-c2[1]))

            if rectangle_area > largest_area:
                largest_area = rectangle_area

    return largest_area


@app.cell
def _():
    example_red_tile_coordinates = [
        "7,1",
        "11,1",
        "11,7",
        "9,7",
        "9,5",
        "2,5",
        "2,3",
        "7,3",
    ]

    solution_example_9_1 = exercise_9_1_find_largest_rectangle(red_tile_coordinates=example_red_tile_coordinates)

    assert solution_example_9_1 == 50
    return


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    red_tile_coordinates = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_9.txt", separator="\n")

    print(exercise_9_1_find_largest_rectangle(red_tile_coordinates=red_tile_coordinates))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Elves just remembered: they can only switch out tiles that are red or green. So, your rectangle can only include red or green tiles.

    In your list, every red tile is connected to the red tile before and after it by a straight line of green tiles. The list wraps, so the first red tile is also connected to the last red tile. Tiles that are adjacent in your list will always be on either the same row or the same column.

    Using the same example as before, the tiles marked X would be green:

    ```
    ..............
    .......#XXX#..
    .......X...X..
    ..#XXXX#...X..
    ..X........X..
    ..#XXXXXX#.X..
    .........X.X..
    .........#X#..
    ..............
    ```

    In addition, all of the tiles inside this loop of red and green tiles are also green. So, in this example, these are the green tiles:

    ```
    ..............
    .......#XXX#..
    .......XXXXX..
    ..#XXXX#XXXX..
    ..XXXXXXXXXX..
    ..#XXXXXX#XX..
    .........XXX..
    .........#X#..
    ..............
    ```

    The remaining tiles are never red nor green.

    The rectangle you choose still must have red tiles in opposite corners, but any other tiles it includes must now be red or green. This significantly limits your options.

    For example, you could make a rectangle out of red and green tiles with an area of 15 between 7,3 and 11,1:

    ```
    ..............
    .......OOOOO..
    .......OOOOO..
    ..#XXXXOOOOO..
    ..XXXXXXXXXX..
    ..#XXXXXX#XX..
    .........XXX..
    .........#X#..
    ..............
    ```

    Or, you could make a thin rectangle with an area of 3 between 9,7 and 9,5:

    ```
    ..............
    .......#XXX#..
    .......XXXXX..
    ..#XXXX#XXXX..
    ..XXXXXXXXXX..
    ..#XXXXXXOXX..
    .........OXX..
    .........OX#..
    ..............
    ```

    The largest rectangle you can make in this example using only red and green tiles has area 24. One way to do this is between 9,5 and 2,3:

    ```
    ..............
    .......#XXX#..
    .......XXXXX..
    ..OOOOOOOOXX..
    ..OOOOOOOOXX..
    ..OOOOOOOOXX..
    .........XXX..
    .........#X#..
    ..............
    ```

    Using two red tiles as opposite corners, what is the largest area of any rectangle you can make using only red and green tiles?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 10 - Factory
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
    Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.

    The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a Shiba Inu. All that remains of the manual are some indicator light diagrams, button wiring schematics, and joltage requirements for each machine.

    For example:

    ```
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    ```

    The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.

    To start a machine, its indicator lights must match those shown in the diagram, where . means off and # means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.

    So, an indicator light diagram like [.##.] means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.

    You can toggle the state of indicator lights by pushing any of the listed buttons. Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).

    So, a button wiring schematic like (0,3,4) means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were [#.....], pushing the button would change them to be [...##.] instead.

    Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.

    You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.

    There are a few ways to correctly configure the first machine:

    ```
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    ```

    - You could press the first three buttons once each, a total of 3 button presses.
    - You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
    - You could press all of the buttons except (1,3) once each, a total of 5 button presses.

    However, the fewest button presses required is 2. One way to do this is by pressing the last two buttons ((0,2) and (0,1)) once each.

    The second machine can be configured with as few as 3 button presses:

    ```
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    ```

    One way to achieve this is by pressing the last three buttons ((0,4), (0,1,2), and (1,2,3,4)) once each.

    The third machine has a total of six indicator lights that need to be configured correctly:

    ```
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    ```

    The fewest presses required to correctly configure it is 2; one way to do this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.

    So, the fewest button presses required to correctly configure the indicator lights on all of the machines is 2 + 3 + 2 = 7.

    Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(convert_string_to_list_of_tuples):
    def exercise_10_1_find_minimal_button_presses(
        manual: list[str]
    ) -> int:
        """
        Compute the minimal number of button presses required for a list of 
        machines described in a manual.

        Each machine description contains an indicator light diagram and a 
        button wiring schematic. The function tries all possible combinations 
        of button presses to find the minimal number that achieves the target 
        light configuration.

        Args:
            manual (list[str]): A list of strings, each representing a machine.
                Each string has the format "[lights] (buttons)" where lights 
                are '#' for on and '.' for off, and buttons are tuples of 
                light indices they toggle.

        Returns:
            int: The sum of the minimal number of button presses needed for 
                all machines in the manual.
        """
        total_button_press_counter: int = 0

        for machine_description in manual:
            # Get indices.
            index_square_bracket_closing: int = machine_description.index("]")
            index_parenthesis_closing: int = machine_description.rindex(")")

            # Separate machine properties.
            indicator_light_diagram: str = machine_description[1:index_square_bracket_closing]
            button_wiring_schematic: str = machine_description[index_square_bracket_closing + 2:index_parenthesis_closing + 1]

            # Additional setup variables.
            number_of_lights: int = len(indicator_light_diagram)
            target_state: list[int] = [index for index, indicator in enumerate(indicator_light_diagram) if indicator == "#"]
            buttons: list[tuple[int]] = convert_string_to_list_of_tuples(str_data=button_wiring_schematic)
            number_of_buttons: int = len(buttons)

            # Brute force approach.
            number_of_button_states: int = 2 ** number_of_buttons
            minimal_number_of_button_presses = float('inf')

            # Loop over all possible states.
            for state_integer in range(number_of_button_states):
                state_binary: str = bin(state_integer)[2:].zfill(number_of_buttons)
                current_state = [0 for _ in range(number_of_lights)]
                button_press_counter: int = 0

                # Loop over the binary representation of the current state.
                for button_index, button_state in enumerate(state_binary):
                    button_state = int(button_state)

                    # Press the button.
                    if button_state:
                        button = buttons[button_index]

                        # Loop over all the light elements present in the button that will be switched on and off.
                        for light_index in button:
                            if current_state[light_index] == 0:
                                current_state[light_index] = 1
                            elif current_state[light_index] == 1:
                                current_state[light_index] = 0

                        button_press_counter += 1

                final_state = [index for index, indicator in enumerate(current_state) if indicator]
            
                if target_state == final_state and button_press_counter < minimal_number_of_button_presses:
                    minimal_number_of_button_presses = button_press_counter

            total_button_press_counter += minimal_number_of_button_presses

        return total_button_press_counter
    return (exercise_10_1_find_minimal_button_presses,)


@app.cell
def _(convert_string_to_list_of_tuples):
    def exercise_10_1_find_minimal_button_presses_binary_approach(
        manual: list[str]
    ) -> int:
        """
        Compute the minimal number of button presses required for a list of 
        machines using a binary/bitmask approach.

        Each machine description contains an indicator light diagram and a 
        button wiring schematic. The function iterates over all possible 
        button press combinations using binary numbers to efficiently 
        determine the minimal number of presses that achieve the target 
        light configuration.

        Args:
            manual (list[str]): A list of strings, each representing a machine.
                Each string has the format "[lights] (buttons)" where lights 
                are '#' for on and '.' for off, and buttons are tuples of 
                light indices they toggle.

        Returns:
            int: The sum of the minimal number of button presses needed for 
                all machines in the manual.
        """
        total_button_press_counter: int = 0

        for machine_description in manual:
            # Get indices.
            index_square_bracket_closing: int = machine_description.index("]")
            index_parenthesis_closing: int = machine_description.rindex(")")

            # Separate machine properties.
            indicator_light_diagram: str = machine_description[1:index_square_bracket_closing]
            button_wiring_schematic: str = machine_description[index_square_bracket_closing + 2:index_parenthesis_closing + 1]

            # Additional setup variables.
            number_of_lights: int = len(indicator_light_diagram)
            target_state: list[int] = [index for index, indicator in enumerate(indicator_light_diagram) if indicator == "#"]
            buttons: list[tuple[int]] = convert_string_to_list_of_tuples(str_data=button_wiring_schematic)
            number_of_buttons: int = len(buttons)

            # Brute force approach.
            number_of_button_states: int = 2 ** number_of_buttons
            minimal_number_of_button_presses = float('inf')

            # Loop over all possible states
            for state_integer in range(1 << number_of_buttons):
                current_state = [0 for _ in range(number_of_lights)]
                button_press_counter: int = 0

                # Loop over all buttons.
                for button_index in range(number_of_buttons):
                    if state_integer & (1 << button_index):
                        button_press_counter += 1

                        # Loop over all the light elements present in the button that will be switched on and off.
                        for light_index in buttons[button_index]:
                            current_state[light_index] ^= 1

                final_state = [index for index, indicator in enumerate(current_state) if indicator]
                if target_state == final_state:
                    minimal_number_of_button_presses = min(button_press_counter, minimal_number_of_button_presses)
        
            total_button_press_counter += minimal_number_of_button_presses

        return total_button_press_counter
    return (exercise_10_1_find_minimal_button_presses_binary_approach,)


@app.cell
def _(
    exercise_10_1_find_minimal_button_presses,
    exercise_10_1_find_minimal_button_presses_binary_approach,
):
    example_manual = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    ]

    solution_example_10_1 = exercise_10_1_find_minimal_button_presses(manual=example_manual)
    solution_example_10_1_v2 = exercise_10_1_find_minimal_button_presses_binary_approach(manual=example_manual)

    assert solution_example_10_1 == 7
    assert solution_example_10_1_v2 == 7
    return (example_manual,)


@app.cell
def _(
    DATA_DIRECTORY_PATH,
    exercise_10_1_find_minimal_button_presses,
    exercise_10_1_find_minimal_button_presses_binary_approach,
    read_data,
):
    manual = read_data(file_path=f"{DATA_DIRECTORY_PATH}/day_10.txt", separator="\n")

    assert exercise_10_1_find_minimal_button_presses(manual=manual) == 578
    assert exercise_10_1_find_minimal_button_presses_binary_approach(manual=manual) == 578
    return (manual,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    All of the machines are starting to come online! Now, it's time to worry about the joltage requirements.

    Each machine needs to be configured to exactly the specified joltage levels to function properly. Below the buttons on each machine is a big lever that you can use to switch the buttons from configuring the indicator lights to increasing the joltage levels. (Ignore the indicator light diagrams.)

    The machines each have a set of numeric counters tracking its joltage levels, one counter per joltage requirement. The counters are all initially set to zero.

    So, joltage requirements like {3,5,4,7} mean that the machine has four counters which are initially 0 and that the goal is to simultaneously configure the first counter to be 3, the second counter to be 5, the third to be 4, and the fourth to be 7.

    The button wiring schematics are still relevant: in this new joltage configuration mode, each button now indicates which counters it affects, where 0 means the first counter, 1 means the second counter, and so on. When you push a button, each listed counter is increased by 1.

    So, a button wiring schematic like (1,3) means that each time you push that button, the second and fourth counters would each increase by 1. If the current joltage levels were {0,1,2,3}, pushing the button would change them to be {0,2,2,4}.

    You can push each button as many times as you like. However, your finger is getting sore from all the button pushing, and so you will need to determine the fewest total presses required to correctly configure each machine's joltage level counters to match the specified joltage requirements.

    Consider again the example from before:

    ```
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    ```

    Configuring the first machine's counters requires a minimum of 10 button presses. One way to do this is by pressing (3) once, (1,3) three times, (2,3) three times, (0,2) once, and (0,1) twice.

    Configuring the second machine's counters requires a minimum of 12 button presses. One way to do this is by pressing (0,2,3,4) twice, (2,3) five times, and (0,1,2) five times.

    Configuring the third machine's counters requires a minimum of 11 button presses. One way to do this is by pressing (0,1,2,3,4) five times, (0,1,2,4,5) five times, and (1,2) once.

    So, the fewest button presses required to correctly configure the joltage level counters on all of the machines is 10 + 12 + 11 = 33.

    Analyze each machine's joltage requirements and button wiring schematics. What is the fewest button presses required to correctly configure the joltage level counters on all of the machines?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(convert_string_to_list_of_tuples):
    import pulp

    def exercise_10_2_find_minimal_button_presses(
        manual: list[str]
    ) -> int:
        """
        Compute the minimal total number of button presses to reach target states for all 
        machines in the manual using integer linear programming.

        Each machine description must include:
        1. Indicator light diagram (e.g., '[#..#]') where '#' indicates a target light.
        2. Button wiring schematic (e.g., '(0,1) (2,3)') showing which lights each button 
           affects.
        3. Target joltage levels (e.g., '1,0,1,0') representing the desired state of each 
           light.

        The function uses PuLP's CBC solver to determine the minimal number of presses per 
        machine and sums them for all machines.

        For each machine:
          - Parse the description to extract lights, buttons, and target states.
          - Build a coefficient matrix where matrix[i][j] = 1 if button j affects light i.
          - Define integer variables for button presses.
          - Minimize the sum of button presses while satisfying the target state constraints.
          - Solve the ILP with CBC.
          - Accumulate the total minimal presses.

        Args:
            manual (list[str]): List of machine descriptions as strings.

        Returns:
            int: Total minimal number of button presses required across all machines.
        """

        total_button_press_counter: int = 0

        for machine_description in manual:
            # Get indices.
            index_square_bracket_closing: int = machine_description.index("]")
            index_parenthesis_closing: int = machine_description.rindex(")")

            # Separate machine properties.
            indicator_light_diagram: str = machine_description[1:index_square_bracket_closing]
            button_wiring_schematic: str = machine_description[index_square_bracket_closing + 2:index_parenthesis_closing + 1]
            joltage_requirements: str = machine_description[index_parenthesis_closing + 3:-1]

            # Additional setup variables.
            number_of_lights: int = len(indicator_light_diagram)
            buttons: list[tuple[int]] = convert_string_to_list_of_tuples(str_data=button_wiring_schematic)
            number_of_buttons: int = len(buttons)
            target_joltage_levels: tuple = tuple(int(level) for level in joltage_requirements.split(","))

            # Setup a coefficient matrix and fill it with the effect all the buttons have on the light indicators.
            coefficient_matrix = [[0] * number_of_buttons for _ in range(number_of_lights)]
            for col_index in range(len(coefficient_matrix[0])):
                for row_index in range(len(coefficient_matrix)):
                    coefficient_matrix[row_index][col_index] = 1 if row_index in buttons[col_index] else 0

            # Build the PuLP linear programming model.
            problem = pulp.LpProblem(
                name="MinimalButtonPresses",
                sense=pulp.LpMinimize # Minimization is objective.
            )

            # Setup up variables.
            variables = [
                pulp.LpVariable(name=f"x_{j}", lowBound=0, upBound=None, cat="Integer")
                for j in range(number_of_buttons)
            ]

            problem += pulp.lpSum(vector=variables) # Minimize the total number of presses

            # Setup constraints.
            for light_index in range(number_of_lights):
                problem += pulp.lpSum(
                    coefficient_matrix[light_index][button_index] * variables[button_index]
                    for button_index in range(number_of_buttons)
                ) == target_joltage_levels[light_index]

            # The problem is ready to be solved now.
            problem.solve(solver=pulp.PULP_CBC_CMD(msg=False))

            # Obtain results
            solution = [int(pulp.value(variable)) for variable in variables]
            total_button_press_counter += sum(solution)

        return total_button_press_counter
    return (exercise_10_2_find_minimal_button_presses,)


@app.cell
def _(example_manual, exercise_10_2_find_minimal_button_presses):
    solution_example_10_2 = exercise_10_2_find_minimal_button_presses(manual=example_manual)

    assert solution_example_10_2 == 33
    return


@app.cell
def _(exercise_10_2_find_minimal_button_presses, manual):
    print(exercise_10_2_find_minimal_button_presses(manual=manual))
    return


if __name__ == "__main__":
    app.run()
