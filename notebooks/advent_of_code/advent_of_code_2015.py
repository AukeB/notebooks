import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


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

    from collections import defaultdict

    from advent_of_code_utils import read_data
    return defaultdict, mo, read_data


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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
