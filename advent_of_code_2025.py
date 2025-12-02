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
    """ """
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

    print(exercise_1_1_find_exact_zeros(rotation_data=example_rotation_data))
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
def exercise_2_1_find_zero_pointings(
    rotation_data: list[str],
    start_position: int = 50
) -> int:
    """ """
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
    print(exercise_2_1_find_zero_pointings(rotation_data=example_rotation_data))
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
    """ """
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

    print(exercise_2_1_find_invalid_ids(product_id_ranges=example_product_id_ranges))
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
    """ """
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
                            #print(id, is_divisible, num_digits_to_check, num_repeats, id_parts, True)
                        else:
                            #print(id, is_divisible, num_digits_to_check, num_repeats, id_parts)
                            pass

        #print()
    
    return sum(invalid_ids)


@app.cell
def _(example_product_id_ranges):
    print(exercise_2_2_find_invalid_ids(product_id_ranges=example_product_id_ranges))
    return


@app.cell
def _(product_id_ranges):
    print(exercise_2_2_find_invalid_ids(product_id_ranges=product_id_ranges))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
