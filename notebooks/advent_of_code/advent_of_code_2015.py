import marimo

__generated_with = "0.23.14"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Advent of Code 2015
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
    import numpy as np

    from itertools import permutations
    from collections import defaultdict, namedtuple

    from advent_of_code_utils import read_data

    return defaultdict, mo, namedtuple, np, permutations, read_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants
    """)
    return


@app.cell
def _():
    DATA_DIRECTORY_PATH = "data/advent_of_code"
    # DATA_DIRECTORY_PATH = "../" + DATA_DIRECTORY_PATH
    return (DATA_DIRECTORY_PATH,)


@app.cell
def _(namedtuple):
    Point = namedtuple("Point", ["x", "y"])
    return (Point,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 1 - Not Quite Lisp
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
    Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

    Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    Here's an easy puzzle to warm you up.

    Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

    The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

    For example:

    - (()) and ()() both result in floor 0.
    - ((( and (()(()( both result in floor 3.
    - ))((((( also results in floor 3.
    - ()) and ))( both result in floor -1 (the first basement level).
    - ))) and )())()) both result in floor -3.

    To what floor do the instructions take Santa?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(defaultdict):
    def exercise_1_1_find_the_final_floor_number(
        floor_instructions: str,
        starting_floor_number: int = 0
    ) -> int:
        """
        Calculate the final floor Santa ends up on based on floor instructions.

        Santa starts on `starting_floor_number` (defaults to 0) and follows a sequence 
        of instructions where '(' means going up one floor and ')' means going 
        down one floor. This function counts the ups and downs to determine the 
        final floor.

        Args:
            floor_instructions (str): A string containing '(' and ')' characters 
                representing Santa's floor movements.
            starting_floor_number (int, optional): The floor Santa starts on. 
                Defaults to 0.

        Returns:
            int: The final floor number after following all instructions.
        """
        direction_count = defaultdict(int)

        for character in floor_instructions:
            if character == "(":
                direction_count["up"] += 1
            elif character == ")":
                direction_count["down"] += 1

        final_floor_number = starting_floor_number + direction_count["up"] - direction_count["down"]

        return final_floor_number

    return (exercise_1_1_find_the_final_floor_number,)


@app.cell
def _(
    DATA_DIRECTORY_PATH,
    exercise_1_1_find_the_final_floor_number,
    read_data,
):
    floor_instructions = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_01.txt", separator="\n")

    print(exercise_1_1_find_the_final_floor_number(floor_instructions=floor_instructions))
    return (floor_instructions,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

    For example:

    - ) causes him to enter the basement at character position 1.
    - ()()) causes him to enter the basement at character position 5.

    What is the position of the character that causes Santa to first enter the basement?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_1_2_find_position_first_character_basement_entry(
    floor_instructions: str,
    starting_floor_number: int = 0,
) -> int:
    """
    Determine the position of the first instruction that causes Santa to enter
    the basement.

    Santa starts on `starting_floor_number` (defaults to 0) and follows a sequence
    of instructions where '(' increases the floor by one and ')' decreases it
    by one. The function returns the 1-based position of the first character
    that brings Santa to floor -1 (the basement).

    Args:
        floor_instructions (str): A string of '(' and ')' characters representing
            Santa's floor movements.
        starting_floor_number (int, optional): The floor Santa starts on.
            Defaults to 0.

    Returns:
        int: The 1-based position of the first character that causes entry into
            the basement.
    """
    starting_index = 1
    current_floor_number = starting_floor_number

    for index, character in enumerate(floor_instructions, start=starting_index):
        current_floor_number += 1 if character == "(" else - 1

        if current_floor_number == -1:
            return index


@app.cell
def _(floor_instructions):
    print(exercise_1_2_find_position_first_character_basement_entry(
        floor_instructions=floor_instructions)
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 2 - I Was Told There Would Be No Math
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
    The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

    Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

    For example:

    - A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    - A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

    All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_2_1_find_total_square_feet_wrapping_paper(
    present_dimensions: list[str]
) -> int:
    """
    Calculate total wrapping paper needed for a list of box dimensions.

    Each dimension string is formatted as "LxWxH". For every present, the
    required paper equals its surface area plus the area of its smallest
    side. Surface area is computed as 2*l*w + 2*w*h + 2*h*l.

    Args:
        present_dimensions (list[str]): List of box dimensions.

    Returns:
        int: Total square feet of wrapping paper needed.
    """
    total_square_feet = 0

    for present_dim in present_dimensions:
        length, width, height = [int(dim) for dim in present_dim.split("x")]
        smallest_side_area = min(length*width, width*height, height*length)
        total_square_feet += 2*length*width + 2*width*height + 2*height*length + smallest_side_area

    return total_square_feet


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    present_dimensions = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_02.txt", separator="\n")

    print(exercise_2_1_find_total_square_feet_wrapping_paper(present_dimensions=present_dimensions))
    return (present_dimensions,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

    For example:

    - A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    - A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

    How many total feet of ribbon should they order?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_2_1_find_total_feet_of_ribbon(
    present_dimensions: list[str]
) -> int:
    """
    Calculate total ribbon needed for a list of box dimensions.

    Each dimension string is formatted as "LxWxH". Ribbon needed equals
    the smallest perimeter of any face plus the volume of the box for
    the bow.

    Args:
        present_dimensions (list[str]): List of box dimensions.

    Returns:
        int: Total feet of ribbon required.
    """
    total_feet_of_ribbon = 0

    for present_dim in present_dimensions:
        length, width, height = [int(dim) for dim in present_dim.split("x")]
        smallest_perimeter = (
            2 * ((length + width + height) - max(length, width, height))
        )
        volume = length * width * height
        total_feet_of_ribbon += smallest_perimeter + volume

    return total_feet_of_ribbon


@app.cell
def _(present_dimensions):
    print(exercise_2_1_find_total_feet_of_ribbon(present_dimensions=present_dimensions))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 3 - Perfectly Spherical Houses in a Vacuum
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
    Santa is delivering presents to an infinite two-dimensional grid of houses.

    He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

    However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

    For example:

    - \> delivers presents to 2 houses: one at the starting location, and one to the east.
    - ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    - ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_3_1_find_unique_houses(
    directional_data: str,
    starting_position: list[int] = [0, 0]
) -> int:
    """
    Count how many unique houses receive at least one present.

    Santa starts at the given starting position on an infinite 2D grid.
    He follows a sequence of movement instructions and delivers a present
    at each visited house. Houses visited multiple times are only counted
    once.

    Args:
        directional_data (str): A string of movement instructions. Each
            character must be one of '^', 'v', '<', or '>', representing
            north, south, west, and east respectively.
        starting_position (list[int]): The (x, y) coordinates where Santa
            starts.

    Returns:
        int: The number of unique houses that receive at least one present.
    """
    current_position = starting_position.copy()
    visited_houses = {tuple(starting_position)}
    directional_mapping = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for move in directional_data:
        dx, dy = directional_mapping[move]

        current_position[0] += dx
        current_position[1] += dy

        visited_houses.add(tuple(current_position))

    return len(visited_houses)


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    directional_data = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_03.txt", separator="\n")

    number_of_unique_visited_houses = exercise_3_1_find_unique_houses(directional_data=directional_data)

    print(f"{number_of_unique_visited_houses=}")
    return (directional_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

    Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

    This year, how many houses receive at least one present?

    For example:

    - ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_3_2_find_unique_houses(
    directional_data: str,
    starting_position: list[int] = [0, 0]
) -> int:
    """
    Count how many unique houses receive at least one present when Santa
    and Robo-Santa deliver presents alternately.

    Santa and Robo-Santa start at the given starting position on an infinite
    2D grid, delivering a present at the starting house. They then take turns
    moving according to the sequence of movement instructions. Houses visited
    multiple times are only counted once.

    Args:
        directional_data (str): A string of movement instructions. Each
            character must be one of '^', 'v', '<', or '>', representing
            north, south, west, and east respectively.
        starting_position (list[int]): The (x, y) coordinates where both
            Santa and Robo-Santa start.

    Returns:
        int: The number of unique houses that receive at least one present.
    """
    santa_current_position = starting_position.copy()
    robo_santa_current_position = starting_position.copy()

    visited_houses = {tuple(starting_position)}
    directional_mapping = {
        "^": (0, 1),
        "v": (0, -1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for index, move in enumerate(directional_data):
        dx, dy = directional_mapping[move]

        if index % 2 == 0:
            santa_current_position[0] += dx
            santa_current_position[1] += dy
            visited_houses.add(tuple(santa_current_position))
        else:
            robo_santa_current_position[0] += dx
            robo_santa_current_position[1] += dy
            visited_houses.add(tuple(robo_santa_current_position))

    return len(visited_houses)


@app.cell
def _(directional_data):
    santa_and_robo_santa_unique_visited_houses = exercise_3_2_find_unique_houses(directional_data=directional_data)

    print(f"{santa_and_robo_santa_unique_visited_houses=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 4 - The Ideal Stocking Suffer
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
    Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

    For example:

    - If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    - If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_4_find_lowest_number(
    secret_key: str,
    number_of_leading_zeros: int
) -> int:
    """
    Find the lowest positive number that produces an MD5 hash with a
    specified number of leading zeroes when appended to the secret key.

    The MD5 hash is computed for the concatenation of the secret key and
    successive positive integers (starting at 0) until a hash is found that
    starts with the specified number of zeroes.

    Args:
        secret_key (str): The secret key string to use as the base of the hash.
        number_of_leading_zeros (int): The required number of leading zeroes
            in the hash. Default is 5.

    Returns:
        int: The lowest positive integer that, when appended to the secret key,
            produces an MD5 hash starting with the specified number of zeroes.
    """
    from hashlib import md5

    hash_prefix = "0" * number_of_leading_zeros
    number = 0

    while True:
        hash_input = secret_key + str(number)
        md5_hash = md5(hash_input.encode()).hexdigest()

        if md5_hash.startswith(hash_prefix):
            return number

        number += 1


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    secret_key = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_04.txt", separator="\n")

    lowest_integer_to_mine_advent_coins = exercise_4_find_lowest_number(
        secret_key=secret_key,
        number_of_leading_zeros=5
    )

    print(f"{lowest_integer_to_mine_advent_coins=}")
    return (secret_key,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now find one that starts with six zeroes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(secret_key):
    lowest_integer_to_mine_advent_coins_part_2 = exercise_4_find_lowest_number(
        secret_key=secret_key,
        number_of_leading_zeros=6
    )

    print(f"{lowest_integer_to_mine_advent_coins_part_2=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 5 - Doesn't He Have Intern-Elves For this?
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
    Santa needs help figuring out which strings in his text file are naughty or nice.

    A nice string is one with all of the following properties:

    - It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    - It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    - It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

    For example:
    - ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    - aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    - jchzalrnumimnmhp is naughty because it has no double letter.
    - haegwjzuvuyypxyu is naughty because it contains the string xy.
    - dvszwmarrgswjxmb is naughty because it contains only one vowel.

    How many strings are nice?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_5_1_find_number_of_nice_strings(
    list_of_strings: list[str],
    vowels: set[str] = set("aeiou"),
    disallowed_substrings: set[str] = {"ab", "cd", "pq", "xy"}
) -> int:
    """
    Count how many strings in a list are considered "nice" according to
    Santa's rules.

    A string is classified as nice if all of the following conditions are met:
    - It contains at least three vowels from the specified vowel set.
    - It contains at least one instance of the same character appearing
      twice in a row.
    - It does not contain any of the specified disallowed substrings.

    Each string is evaluated independently by scanning its characters and
    adjacent character pairs.

    Args:
        list_of_strings (list[str]): The collection of strings to evaluate.
        vowels (set[str]): The set of characters considered vowels when
            counting vowel occurrences. Default is {"a", "e", "i", "o", "u"}.
        disallowed_substrings (set[str]): Substrings that immediately
            disqualify a string if present. Default is {"ab", "cd", "pq", "xy"}.

    Returns:
        int: The number of strings in the input list that satisfy all
            "nice string" conditions.
    """
    number_of_nice_strings: int = 0

    for naughty_or_nice_string in list_of_strings:
        vowel_count: int = 0
        twice_in_a_row: bool = False
        disallowed_substring_detected = False

        # Pythonic way for iterating over consecutive elements.
        for previous_character, current_character in zip(naughty_or_nice_string, naughty_or_nice_string[1:]): 
            adjacent_characters = previous_character + current_character

            # Check for vowels.
            if previous_character in vowels:
                vowel_count += 1

            # Check if there is a character that appears twice in a row.
            if previous_character == current_character:
                twice_in_a_row = True

            # Check for disallowed substrings.
            if adjacent_characters in disallowed_substrings:                
                disallowed_substring_detected = True
                break

        # Check final character of string because we missed that in the loop.
        if naughty_or_nice_string[-1] in vowels:
            vowel_count += 1

        # Final check for naughty or nice string.
        if vowel_count >= 3 and twice_in_a_row and not disallowed_substring_detected:
            number_of_nice_strings += 1

    return number_of_nice_strings


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    naughty_or_nice_strings: list[str] = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_05.txt", separator="\n")

    number_of_nice_strings_5_1 = exercise_5_1_find_number_of_nice_strings(
        list_of_strings=naughty_or_nice_strings,
    )

    print(f"{number_of_nice_strings_5_1=}")
    return (naughty_or_nice_strings,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:
    - It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    - It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

    For example:

    - qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    - xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    - uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    - ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

    How many strings are nice under these new rules?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(defaultdict):
    def exercise_5_2_find_number_of_nice_strings(
        list_of_strings: list[str],
    ) -> int:
        """
        Count how many strings in a list are considered "nice" according to
        Santa's updated rules for Part 2.

        A string is classified as nice if both of the following conditions are met:
        - It contains a pair of any two letters that appears at least twice in the
          string without overlapping.
        - It contains at least one letter which repeats with exactly one letter
          between them.

        Each string is evaluated independently by scanning its characters and
        adjacent character pairs, storing the indices of each pair to detect
        non-overlapping repetitions.

        Args:
            list_of_strings (list[str]): The collection of strings to evaluate.

        Returns:
            int: The number of strings in the input list that satisfy all
                "nice string" conditions according to the updated rules.
        """
        number_of_nice_strings: int = 0

        for naughty_or_nice_string in list_of_strings:
            unique_adjacent_pairs = defaultdict(list)
            pair_appearing_twice_detected: bool = False
            repeating_character_detected: bool = False

            # Check for pairs of any two letter that appear at leat twice in string without overlapping.
            for index, adjacent_characters in enumerate(zip(naughty_or_nice_string, naughty_or_nice_string[1:])):
                adjacent_characters = "".join(adjacent_characters)
                unique_adjacent_pairs[adjacent_characters].append(index)

            for index_value in unique_adjacent_pairs.values():
                if len(index_value) > 1 and max(index_value) - min(index_value) > 1:
                    pair_appearing_twice_detected = True
                    break

            # Check for a letter which repeats with exactly one letter between them.
            for character_index in range(len(naughty_or_nice_string) - 2):
                first_character = naughty_or_nice_string[character_index]
                third_character = naughty_or_nice_string[character_index + 2]

                if first_character == third_character:
                    repeating_character_detected = True
                    break

            if pair_appearing_twice_detected and repeating_character_detected:
                number_of_nice_strings += 1

        return number_of_nice_strings

    return (exercise_5_2_find_number_of_nice_strings,)


@app.cell
def _(
    exercise_5_2_find_number_of_nice_strings,
    naughty_or_nice_strings: list[str],
):
    number_of_nice_strings_5_2 = exercise_5_2_find_number_of_nice_strings(
        list_of_strings=naughty_or_nice_strings,
    )

    print(f"{number_of_nice_strings_5_2=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 6: Probably a Fire Hazard
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
    Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

    Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

    Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

    To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

    For example:

    - turn on 0,0 through 999,999 would turn on (or leave on) every light.
    - toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    - turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

    After following the instructions, how many lights are lit?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(Point, np):
    def exercise_6_1_find_number_of_lit_lights(
        instruction_data: list[str],
    ) -> int:
        """
        Count how many lights are lit in a 1000x1000 grid after following Santa's instructions.

        Each instruction either turns on, turns off, or toggles a rectangular
        region of lights defined by two corner coordinates. The grid starts with
        all lights off and is updated for each instruction using NumPy array slicing.

        Args:
            instruction_data (list[str]): A list of instructions, each describing
                an action and two corner coordinates of a rectangle.

        Returns:
            int: The total number of lights that are lit after all instructions
                have been applied.
        """
        grid_size: int = 1000
        grid_of_lights = np.zeros((grid_size, grid_size), dtype=int)

        for instruction in instruction_data:
            instruction = instruction.split(" ")

            # Determine action based on instruction length.
            if len(instruction) == 4:
                action = instruction[0]
            elif len(instruction) == 5:
                action = "_".join(instruction[:2])

            # Determine coordinates backwards.
            c1 = Point(*[int(x) for x in instruction[-1].split(",")])
            c2 = Point(*[int(x) for x in instruction[-3].split(",")])

            # Apply actions to the grid of lights.
            rectangle = (slice(min(c1.x, c2.x), max(c1.x, c2.x) + 1), slice(min(c1.y, c2.y), max(c1.y, c2.y) + 1))

            if action == "turn_on":
                grid_of_lights[rectangle] = 1
            elif action == "turn_off":
                grid_of_lights[rectangle] = 0
            elif action == "toggle":
                grid_of_lights[rectangle] ^= 1 

        number_of_lit_lights = int(grid_of_lights.sum())

        return number_of_lit_lights

    return (exercise_6_1_find_number_of_lit_lights,)


@app.cell
def _(DATA_DIRECTORY_PATH, exercise_6_1_find_number_of_lit_lights, read_data):
    instruction_data: list[str] = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_06.txt", separator="\n")

    number_of_lit_lights_6_1 = exercise_6_1_find_number_of_lit_lights(instruction_data=instruction_data)

    print(f"{number_of_lit_lights_6_1=}")
    return (instruction_data,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish. The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero. The phrase turn on actually means that you should increase the brightness of those lights by 1. The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero. The phrase toggle actually means that you should increase the brightness of those lights by 2.

    What is the total brightness of all lights combined after following Santa's instructions?

    For example:
    - turn on 0,0 through 0,0 would increase the total brightness by 1.
    - toggle 0,0 through 999,999 would increase the total brightness by 2000000.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(Point, np):
    def exercise_6_2_find_number_of_lit_lights(
        instruction_data: list[str],
    ) -> int:
        """
        Calculate the total brightness of all lights in a 1000x1000 grid after
        following Santa's updated brightness instructions.

        Each instruction adjusts the brightness of a rectangular region of lights
        defined by two corner coordinates. The grid starts with all lights at zero
        brightness and is updated for each instruction using NumPy array slicing.

        The brightness rules are as follows:
        - "turn on" increases the brightness of each light in the rectangle by 1.
        - "turn off" decreases the brightness of each light by 1, with a minimum of 0.
        - "toggle" increases the brightness of each light in the rectangle by 2.

        Args:
            instruction_data (list[str]): A list of instructions, each describing
                an action and two corner coordinates of a rectangle.

        Returns:
            int: The total brightness of all lights after all instructions
                have been applied.
        """
        grid_size: int = 1000
        grid_of_lights = np.zeros((grid_size, grid_size), dtype=int)

        for instruction in instruction_data:
            instruction = instruction.split(" ")

            # Determine action based on instruction length.
            if len(instruction) == 4:
                action = instruction[0]
            elif len(instruction) == 5:
                action = "_".join(instruction[:2])

            # Determine coordinates backwards.
            c1 = Point(*[int(x) for x in instruction[-1].split(",")])
            c2 = Point(*[int(x) for x in instruction[-3].split(",")])

            # Apply actions to the grid of lights.
            rectangle = (slice(min(c1.x, c2.x), max(c1.x, c2.x) + 1), slice(min(c1.y, c2.y), max(c1.y, c2.y) + 1))

            if action == "turn_on":
                grid_of_lights[rectangle] += 1
            elif action == "turn_off":
                grid_of_lights[rectangle] = np.maximum(grid_of_lights[rectangle] - 1, 0)
            elif action == "toggle":
                grid_of_lights[rectangle] += 2 

        number_of_lit_lights = int(grid_of_lights.sum())

        return number_of_lit_lights

    return (exercise_6_2_find_number_of_lit_lights,)


@app.cell
def _(exercise_6_2_find_number_of_lit_lights, instruction_data: list[str]):
    number_of_lit_lights_6_2 = exercise_6_2_find_number_of_lit_lights(instruction_data=instruction_data)

    print(f"{number_of_lit_lights_6_2=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 7: Probably a Fire Hazard
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
    This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

    Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

    The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

    For example:

    - 123 -> x means that the signal 123 is provided to wire x.
    - x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    - p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    - NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

    Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

    For example, here is a simple circuit:

    ```
    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i
    ```

    After it is run, these are the signals on the wires:

    ```
    d: 72
    e: 507
    f: 492
    g: 114
    h: 65412
    i: 65079
    x: 123
    y: 456
    ```

    In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _():
    def _get_wire_value(element: str, wire_signal_values: dict[str, int | None]) -> int:
        """
        Resolve an element to its integer value.

        Accepts either a numeric literal or a wire name. Raises ValueError if
        the wire has not yet been assigned a value, signalling the caller to
        skip this instruction and retry on the next iteration.

        Args:
            element (str): A wire name or numeric literal.
            wire_signal_values (dict[str, int | None]): Current known wire values.

        Returns:
            value (int): The resolved integer value.

        Raises:
            ValueError: If the wire has no value yet.
        """
        value = int(element) if element.isdigit() else wire_signal_values.get(element)

        if value is None:
            raise ValueError

        return value


    def exercise_7_1_find_signal_value(
        instruction_booklet: list[str],
        number_of_bits_max_signal: int = 16,
    ) -> dict[str, int]:
        """
        Find the signal value of each wire after processing all instructions.

        Iterates over instructions repeatedly until all wires have been assigned
        a value. Instructions that depend on wires not yet resolved are skipped
        and retried in the next iteration.

        Args:
            instruction_booklet (list[str]): The puzzle input lines.
            number_of_bits_max_signal (int): Bit width of wire signals, defaults to 16.

        Returns:
            wire_signal_values (dict[str, int]): Mapping of wire name to its final signal.
        """
        arrow_definition = "->"
        max_signal_value = 2**number_of_bits_max_signal - 1
        all_output_wires = {line.split()[-1] for line in instruction_booklet}
        wire_signal_values: dict[str, int | None] = {}

        while any(wire not in wire_signal_values for wire in all_output_wires):
            for instruction_line in instruction_booklet:
                instruction_elements = instruction_line.split()
                index_arrow = instruction_elements.index(arrow_definition)
                instruction_input = instruction_elements[:index_arrow]
                output_wire = instruction_elements[-1]

                try:
                    if len(instruction_input) == 1:
                        wire_signal_values[output_wire] = _get_wire_value(instruction_input[0], wire_signal_values)

                    elif len(instruction_input) == 2:
                        wire_signal_values[output_wire] = ~_get_wire_value(instruction_input[1], wire_signal_values) & max_signal_value

                    elif len(instruction_input) == 3:
                        first_element, operator, second_element = instruction_input

                        if operator == "AND":
                            wire_signal_values[output_wire] = _get_wire_value(first_element, wire_signal_values) & _get_wire_value(second_element, wire_signal_values)
                        elif operator == "OR":
                            wire_signal_values[output_wire] = _get_wire_value(first_element, wire_signal_values) | _get_wire_value(second_element, wire_signal_values)
                        elif operator == "LSHIFT":
                            wire_signal_values[output_wire] = _get_wire_value(first_element, wire_signal_values) << int(second_element) & max_signal_value
                        elif operator == "RSHIFT":
                            wire_signal_values[output_wire] = _get_wire_value(first_element, wire_signal_values) >> int(second_element)

                except ValueError:
                    continue

        result = dict(sorted(wire_signal_values.items()))

        return result

    return (exercise_7_1_find_signal_value,)


@app.cell
def _(exercise_7_1_find_signal_value):
    example_data_7_1 = [
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
        "NOT x -> h",
        "NOT y -> i"
    ]

    example_wire_signal_values = exercise_7_1_find_signal_value(instruction_booklet=example_data_7_1)
    print(example_wire_signal_values)
    return


@app.cell
def _(DATA_DIRECTORY_PATH, exercise_7_1_find_signal_value, read_data):
    instruction_booklet: list[str] = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_07.txt", separator="\n")

    wire_signal_values = exercise_7_1_find_signal_value(instruction_booklet=instruction_booklet)

    print(f"{wire_signal_values['a']=}")
    return (instruction_booklet,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(exercise_7_1_find_signal_value, instruction_booklet: list[str]):
    instruction_booklet_2 = instruction_booklet.copy()
    index_b = [line.split()[-1] for line in instruction_booklet_2].index('b')
    instruction_booklet_2[index_b] = "956 -> b"

    wire_signal_values_2 = exercise_7_1_find_signal_value(instruction_booklet=instruction_booklet_2)

    print(f"{wire_signal_values_2['a']=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 8: Matchsticks
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _exercise_8_1_special_character_analysis(mo):
    mo.md(r"""
    Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.

    It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

    However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.

    For example:

    - "\" is 2 characters of code (the two double quotes), but the string contains zero characters.
    - "abc" is 5 characters of code, but 3 characters in the string data.
    - "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
    - "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

    Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

    Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

    For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _():
    import string

    def exercise_8_1_special_character_analysis(santas_list: list[str]) -> int:
        """
        Calculate the total number of characters of code for string literals minus
        the total number of characters in memory for the values of the strings.
        Handles three escape sequences: \\\\ (single backslash), \\" (lone double-quote),
        and \\x followed by two hexadecimal characters (single ASCII character).

        1. Initialise the difference counter with 2 per line to account for the
           surrounding double-quote characters.
        2. For each line, walk character by character; when a backslash is found,
           identify the escape sequence and increment the difference counter by the
           number of code characters that collapse into one in-memory character.

        Args:
            santas_list (list[str]): The double-quoted string literals from Santa's
                digital list, one per line.

        Returns:
            difference_counter (int): Total characters of code minus total characters
                in memory across all string literals.
        """
        difference_counter = 2 * len(santas_list)

        for line in santas_list:
            char_index: int = 0

            while char_index < len(line):
                if line[char_index] == "\\":
                    next_char = line[char_index + 1]

                    if next_char == "\\" or next_char == "\"":
                        difference_counter += 1
                        char_index += 2
                    elif next_char == "x" and all(digit in string.hexdigits for digit in line[char_index + 2: char_index + 4]):
                        difference_counter += 3
                        char_index += 4
                    else:
                        char_index += 1
                else:
                    char_index += 1

        return difference_counter

    return (exercise_8_1_special_character_analysis,)


@app.cell
def _(DATA_DIRECTORY_PATH, exercise_8_1_special_character_analysis, read_data):
    santas_list: list[str] = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_08.txt", separator="\n")

    difference_special_characters = exercise_8_1_special_character_analysis(santas_list=santas_list)

    print(f"{difference_special_characters=}")
    return (santas_list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the new encoded representation, including the surrounding double quotes.

    For example:

    - "\" encodes to "\"\"\", an increase from 2 characters to 6.
    - "abc" encodes to "\"abc\"\", an increase from 5 characters to 9.
    - "aaa\"aaa" encodes to "\"aaa\\\"aaa\"\", an increase from 10 characters to 16.
    - "\x27" encodes to "\"\\x27\"\", an increase from 6 characters to 11.

    Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.function
def exercise_8_2_special_character_analysis(santas_list: list[str]) -> int:
    """
    Calculate the total number of characters in the re-encoded string literals
    minus the total number of characters in the original code representation.

    Re-encoding wraps each string in a new pair of double-quotes and escapes
    every backslash and double-quote character with an additional backslash.

    Args:
        santas_list (list[str]): The double-quoted string literals from Santa's
            digital list, one per line.

    Returns:
        difference_counter (int): Total characters of re-encoded strings minus
            total characters of the original string literals across all lines.
    """
    difference_counter = 2 * len(santas_list) + sum(
        line.count("\\") + line.count('"') for line in santas_list
    )

    return difference_counter


@app.cell
def _(santas_list: list[str]):
    difference_special_characters_reverse = exercise_8_2_special_character_analysis(santas_list=santas_list)

    print(f"{difference_special_characters_reverse=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 9: All in a Single Night
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
    Every year, Santa manages to deliver all of his presents in a single night.

    This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

    For example, given the following distances:

    ```
    London to Dublin = 464
    London to Belfast = 518
    Dublin to Belfast = 141
    ```

    The possible routes are therefore:

    ```
    Dublin -> London -> Belfast = 982
    London -> Dublin -> Belfast = 605
    London -> Belfast -> Dublin = 659
    Dublin -> Belfast -> London = 659
    Belfast -> Dublin -> London = 605
    Belfast -> London -> Dublin = 982
    ```

    The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

    What is the distance of the shortest route?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _(np, permutations):
    def exercise_9_1_find_shortest_route(distances: list[str]) -> int:
        """
        Find the shortest route that visits every location exactly once using brute force.

        1. Extract all unique locations and map them to matrix indices.
        2. Build a symmetric distance matrix from the parsed input.
        3. Enumerate all possible routes via permutations and track the shortest.

        Args:
            distances (list[str]): Each line describes a distance in the format
                'A to B = N', where A and B are location names and N is the distance.

        Returns:
            shortest_route (int): The total distance of the shortest route that
                visits every location exactly once.
        """
        unique_locations = list({x.split()[i] for x in distances for i in (0, 2)})
        number_of_unique_locations = len(unique_locations)
        location_mapping = {
            location: unique_locations.index(location)
            for location in unique_locations
        }
        distance_matrix = np.zeros(
            [number_of_unique_locations, number_of_unique_locations], dtype=int
        )

        for line in distances:
            line_split = line.split()

            node_start: str = line_split[0]
            node_end: str = line_split[2]
            distance: int = int(line_split[4])

            distance_matrix[location_mapping[node_start]][
                location_mapping[node_end]
            ] = distance
            distance_matrix[location_mapping[node_end]][
                location_mapping[node_start]
            ] = distance

        all_possible_routes = permutations(range(number_of_unique_locations))
        shortest_route = float("inf")

        for route in all_possible_routes:
            distance_current_route = 0

            for cur_loc, next_loc in zip(route, route[1:]):
                distance_current_route += distance_matrix[cur_loc][next_loc]

            if distance_current_route < shortest_route:
                shortest_route = distance_current_route

        return int(shortest_route)

    return (exercise_9_1_find_shortest_route,)


@app.cell
def _(DATA_DIRECTORY_PATH, exercise_9_1_find_shortest_route, read_data):
    distances: list[str] = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_09.txt", separator="\n")

    shortest_route = exercise_9_1_find_shortest_route(distances=distances)

    print(f"{shortest_route=}")
    return (distances,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The next year, just to show off, Santa decides to take the route with the longest distance instead.

    He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

    For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

    What is the distance of the longest route?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _(np, permutations):
    def exercise_9_2_find_longest_route(distances: list[str]) -> int:
        """
        Find the longest route that visits every location exactly once using brute force.

        1. Extract all unique locations and map them to matrix indices.
        2. Build a symmetric distance matrix from the parsed input.
        3. Enumerate all possible routes via permutations and track the longest.

        Args:
            distances (list[str]): Each line describes a distance in the format
                'A to B = N', where A and B are location names and N is the distance.

        Returns:
            longest_route (int): The total distance of the longest route that
                visits every location exactly once.
        """
        unique_locations = list({x.split()[i] for x in distances for i in (0, 2)})
        number_of_unique_locations = len(unique_locations)
        location_mapping = {
            location: unique_locations.index(location)
            for location in unique_locations
        }
        distance_matrix = np.zeros(
            [number_of_unique_locations, number_of_unique_locations], dtype=int
        )

        for line in distances:
            line_split = line.split()

            node_start: str = line_split[0]
            node_end: str = line_split[2]
            distance: int = int(line_split[4])

            distance_matrix[location_mapping[node_start]][
                location_mapping[node_end]
            ] = distance
            distance_matrix[location_mapping[node_end]][
                location_mapping[node_start]
            ] = distance

        all_possible_routes = permutations(range(number_of_unique_locations))
        longest_route = 0

        for route in all_possible_routes:
            distance_current_route = 0

            for cur_loc, next_loc in zip(route, route[1:]):
                distance_current_route += distance_matrix[cur_loc][next_loc]

            if distance_current_route > longest_route:
                longest_route = distance_current_route

        return int(longest_route)

    return (exercise_9_2_find_longest_route,)


@app.cell
def _(distances: list[str], exercise_9_2_find_longest_route):
    longest_route = exercise_9_2_find_longest_route(distances=distances)

    print(f"{longest_route=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 10: Elves Look, Elves Say
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
    Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

    Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

    For example:

    - 1 becomes 11 (1 copy of digit 1).
    - 11 becomes 21 (2 copies of digit 1).
    - 21 becomes 1211 (one 2 followed by one 1).
    - 1211 becomes 111221 (one 1, one 2, and two 1s).
    - 111221 becomes 312211 (three 1s, two 2s, and one 1).

    Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

    Your puzzle input is 1113222113
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_10_1_compute_look_and_say_sequence(
    start_value: str, number_of_iterations: int
) -> list[str]:
    """
    Apply the look-and-say transformation iteratively, returning the full sequence.

    Each step reads the current value as runs of identical digits and encodes
    each run as its length followed by the digit. The returned list includes
    the original start_value as the first element.

    Args:
        start_value (str): The initial digit string to begin the sequence from.
        number_of_iterations (int): The number of look-and-say steps to apply.

    Returns:
        look_and_say_sequence (list[str]): All values in the sequence, from
            start_value through the final transformed value.
    """
    look_and_say_sequence = [start_value]
    current_value = start_value

    for _ in range(number_of_iterations):
        next_value = ""
        char_index = 0

        while char_index < len(current_value):
            cur_char = current_value[char_index]
            char_counter = 1

            while (
                char_index + char_counter < len(current_value)
                and current_value[char_index + char_counter] == cur_char
            ):
                char_counter += 1

            next_value += f"{char_counter}{cur_char}"
            char_index += char_counter

        look_and_say_sequence.append(next_value)
        current_value = next_value

    return look_and_say_sequence


@app.cell
def _():
    solution_10_1_length_result = exercise_10_1_compute_look_and_say_sequence(
        start_value="1113222113", number_of_iterations=40
    )

    print(f"{len(solution_10_1_length_result[-1])=}")
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
    Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

    Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _():
    solution_10_2_length_result = exercise_10_1_compute_look_and_say_sequence(
        start_value="1113222113", number_of_iterations=50
    )

    print(f"{len(solution_10_2_length_result[-1])=}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 11: Corporate Policy
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
    Santa's previous password expired, and he needs help choosing a new one.

    To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

    Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

    - Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    - Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    - Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

    For example:

    ```
    - hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
    - abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
    - abbcegjk fails the third requirement, because it only has one double letter (bb).
    - The next password after abcdefgh is abcdffaa.
    - The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
    ```

    Given Santa's current password (your puzzle input), what should his next password be?

    Your puzzle input is `cqjxjnds`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.function
def exercise_11_1_find_next_password(input_password: str) -> str:
    """ """
    num_iter = 50

    next_password = input_password

    for _ in range(num_iter):
        print(next_password)
        final_character = next_password[-1]

        if final_character == "z":
            new_password = []
            z_detected = False

            for character in next_password[::-1]:
                if character == "z":
                    z_detected = True
                    new_password.insert(0, "a")
                else:
                    if z_detected:
                        new_password.insert(0, chr(ord(character) + 1))
                        z_detected = False
                    else:
                        new_password.insert(0, character)

            next_password = "".join(new_password)
        else:
            next_password = next_password[0:-1] + chr(ord(next_password[-1]) + 1)


@app.cell
def _():
    input_password = "cqjxjzzs"

    next_password = exercise_11_1_find_next_password(input_password=input_password)

    print(f"{next_password=}")
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 12: JSAbacusFramework.io
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 13: Knights of the Dinner Table
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Instructions
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 1 - Solution
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Instructions
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Part 2 - Solution
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Day 14: Reindeer Olympics
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
    This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

    Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

    For example, suppose you have the following Reindeer:

    - Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    - Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

    After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

    In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

    Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
    """)
    return


@app.function
def exercise_14_1_find_fastest_reinder(
    reindeer_descriptions: list[str],
    total_time: int = 2503
) -> int:
    """
    Simulate each reindeer's flight and rest cycles to find the winning distance.

    1. Parse each reindeer description into its speed, move duration, rest
       duration, and combined cycle duration.
    2. Step through every second up to total_time, tracking each reindeer's
       cumulative distance based on whether it is flying or resting.
    3. Return the distance traveled by the reindeer that is furthest ahead.

    Args:
        reindeer_descriptions (list[str]): Raw puzzle input lines, one per
            reindeer.
        total_time (int): Number of seconds the race runs for.

    Returns:
        winning_reindeer_distance_traveled (int): Distance traveled by the
            leading reindeer once the race ends.
    """
    reindeers = {}
    
    for reindeer_description in reindeer_descriptions:
        reindeer_data = reindeer_description.split()

        reindeers[reindeer_data[0]] = {
            "move_speed": int(reindeer_data[3]),
            "move_duration": int(reindeer_data[6]),
            "rest_speed": 0,
            "rest_duration": int(reindeer_data[13]),
            "cycle_duration": int(reindeer_data[6]) + int(reindeer_data[13]),
            "traveled": [[0, 0]]
        }

    for i in range(total_time + 1):
        for reindeer_name, reindeer_stats in reindeers.items():
            j = i % reindeer_stats["cycle_duration"]
            
            if j > 0 and j <= reindeer_stats["move_duration"]:
                reindeers[reindeer_name]["traveled"].append(
                    [i, reindeer_stats["traveled"][-1][1] + reindeer_stats["move_speed"]]
                )
            else:
                reindeers[reindeer_name]["traveled"].append(
                    [i, reindeer_stats["traveled"][-1][1] + reindeer_stats["rest_speed"]]
                )

    winning_reindeer_distance_traveled = max([reinder_stats["traveled"][-1][1] for reinder_name, reinder_stats in reindeers.items()])
                                              
    return winning_reindeer_distance_traveled


@app.cell
def _(DATA_DIRECTORY_PATH, read_data):
    reindeer_descriptions: list[str] = read_data(file_path=f"{DATA_DIRECTORY_PATH}/2015_day_14.txt", separator="\n")

    winning_reindeer_distance_traveled = exercise_14_1_find_fastest_reinder(
        reindeer_descriptions=reindeer_descriptions
    )

    print(f"{winning_reindeer_distance_traveled=}")
    return


if __name__ == "__main__":
    app.run()
