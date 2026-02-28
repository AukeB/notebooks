import marimo

__generated_with = "0.18.4"
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

    from collections import defaultdict, namedtuple

    from advent_of_code_utils import read_data
    return defaultdict, mo, namedtuple, np, read_data


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


if __name__ == "__main__":
    app.run()
