import marimo

__generated_with = "0.18.4"
app = marimo.App(width="columns")


@app.cell(column=0, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Display
    """)
    return


@app.cell
def _(
    Dimensions,
    InventoryDrawer,
    Position,
    horizontal_slots,
    vertical_position,
    vertical_slots,
):
    item_slot_grid_dimensions = Dimensions(horizontal_slots.value, vertical_slots.value)
    item_slot_grid_position = Position(5, vertical_position.value)

    draw_inventory = InventoryDrawer(
        item_slot_grid_position=item_slot_grid_position,
        item_slot_grid_dimensions=item_slot_grid_dimensions
    )

    draw_inventory.draw()
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(column=1, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Parameters
    """)
    return


@app.cell
def _(mo):
    horizontal_slots = mo.ui.slider(1, 8, full_width=True)
    vertical_slots = mo.ui.slider(1, 3, full_width=True)
    vertical_position = mo.ui.slider(2, 9, full_width=True)
    return horizontal_slots, vertical_position, vertical_slots


@app.cell
def _(horizontal_slots):
    horizontal_slots
    return


@app.cell
def _(vertical_slots):
    vertical_slots
    return


@app.cell
def _(vertical_position):
    vertical_position
    return


@app.cell(hide_code=True)
def _():
    return


@app.cell(column=2, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Code
    """)
    return


@app.cell
def _():
    import marimo as mo

    from collections import namedtuple
    return mo, namedtuple


@app.cell
def _(
    CHAR_SET_DOUBLE_LINES,
    CHAR_SET_SINGLE_LIGHT_LINES,
    Dimensions,
    Position,
):
    class InventoryDrawer():
        """ """

        def __init__(
            self,
            item_slot_grid_position: Position,
            item_slot_grid_dimensions: Dimensions,
        ) -> None:
            """ """
            self.inventory_width, self.inventory_height = 80, 20
            self.char_set_inventory = CHAR_SET_DOUBLE_LINES
            self.char_set_item_slot = CHAR_SET_SINGLE_LIGHT_LINES

            self.item_slot_grid_position = item_slot_grid_position
            self.item_slot_grid_dimensions = item_slot_grid_dimensions

            self._validate_input_data()

            self.item_slot_layout = self._get_item_slot_layout()
            self.item_slot_width = sum([count for _, count in self.item_slot_layout["top"]])

            self.rows = self._construct_rows()
            self.rows_rendered = self._convert_rows_to_strings()

            self.inventory_layout = self._construct_inventory()

        def _validate_input_data(
            self
        ) -> None:
            """ """
            assert self.item_slot_grid_position.x > 1 and self.item_slot_grid_position.y > 1

        def _get_item_slot_layout(
            self
        ) -> dict[str, list[tuple[str, int]]]:
            """ """
            item_slot_layout = {
                "top": [
                    (self.char_set_item_slot["top_left_corner"], 1),
                    (self.char_set_item_slot["horizontal_line"], 4),
                    (self.char_set_item_slot["top_right_corner"], 1),
                ],
                "mid": [
                    (self.char_set_item_slot["vertical_line"], 1),
                    (" ", 1),
                    ("‡", 2),
                    (" ", 1),
                    (self.char_set_item_slot["vertical_line"], 1),
                ],
                "bot": [
                    (self.char_set_item_slot["bot_left_corner"], 1),
                    (self.char_set_item_slot["horizontal_line"], 4),
                    (self.char_set_item_slot["bot_right_corner"], 1),
                ],
            }

            return item_slot_layout

        def _construct_rows_with_item_slots(
            self,
        ) -> dict[str, list[tuple[str, int]]]:
            """ """
            row_start = [
                (self.char_set_inventory["vertical_line"], 1),
                (self.char_set_inventory["empty"], self.item_slot_grid_position.x - 1)
            ]

            row_end_width: int = self.item_slot_grid_position.x + self.item_slot_grid_dimensions.width * self.item_slot_width + 1

            row_end = [
                (self.char_set_inventory["empty"], self.inventory_width - row_end_width),
                (self.char_set_inventory["vertical_line"], 1)
            ]

            row_top = row_start.copy()
            row_mid = row_start.copy()
            row_bot = row_start.copy()

            for _ in range(self.item_slot_grid_dimensions.width):
                row_top.extend(self.item_slot_layout["top"])
                row_mid.extend(self.item_slot_layout["mid"])
                row_bot.extend(self.item_slot_layout["bot"])

            row_top.extend(row_end)
            row_mid.extend(row_end)
            row_bot.extend(row_end)

            rows_with_item_slots = {
                "item_slot_top": row_top,
                "item_slot_mid": row_mid,
                "item_slot_bot": row_bot,
            }

            return rows_with_item_slots

        def _construct_rows(
            self,
        ) -> dict[str, list[tuple[str, int]]]:
            """ """
            rows = {
                "top": [
                    (self.char_set_inventory["top_left_corner"], 1),
                    (self.char_set_inventory["horizontal_line"], self.inventory_width - 2),
                    (self.char_set_inventory["top_right_corner"], 1),
                ],
                "mid_empty": [
                    (self.char_set_inventory["vertical_line"], 1),
                    (self.char_set_inventory["empty"], self.inventory_width - 2),
                    (self.char_set_inventory["vertical_line"], 1),
                ],
                "bot": [
                    (self.char_set_inventory["bot_left_corner"], 1),
                    (self.char_set_inventory["horizontal_line"], self.inventory_width - 2),
                    (self.char_set_inventory["bot_right_corner"], 1),
                ],
            }

            rows.update(self._construct_rows_with_item_slots())

            return rows

        def _convert_rows_to_strings(
            self
        ) -> dict[str, str]:
            """ """
            rows_rendered = {
                f"{k}_str": "".join(key * value for key, value in v)
                for k, v in self.rows.items()
            }

            return rows_rendered

        def _construct_inventory(
            self
        ) -> list[str]:
            """ """
            inventory_layout = []

            inventory_layout.append(self.rows_rendered["top_str"])
            inventory_layout.extend([self.rows_rendered["mid_empty_str"]] * (self.item_slot_grid_position.y - 1))

            inventory_layout.extend(self.item_slot_grid_dimensions.height * [
                self.rows_rendered["item_slot_top_str"],
                self.rows_rendered["item_slot_mid_str"],
                self.rows_rendered["item_slot_bot_str"],
            ])

            remaining_rows = self.inventory_height - (self.item_slot_grid_position.y + 3 * self.item_slot_grid_dimensions.height + 1)

            inventory_layout.extend([self.rows_rendered["mid_empty_str"]] * remaining_rows)
            inventory_layout.append(self.rows_rendered["bot_str"])

            return inventory_layout

        def draw(
            self,
        ) -> None:
            """ """
            for inventory_row in self.inventory_layout:
                print(inventory_row)



    return (InventoryDrawer,)


@app.cell(hide_code=True)
def _():
    return


@app.cell(column=3, hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants
    """)
    return


@app.cell
def _(namedtuple):
    Dimensions = namedtuple("Dimensions", "width height")
    Position = namedtuple("Position", "x y")

    CHAR_SET_SINGLE_LIGHT_LINES = {
        "top_left_corner": "\u250C",
        "top_right_corner": "\u2510",
        "bot_left_corner": "\u2514",
        "bot_right_corner": "\u2518",
        "horizontal_line": "\u2500",
        "vertical_line": "\u2502",
        "empty": " ",
    }

    CHAR_SET_SINGLE_BOLD_LINES = {
        "top_left_corner": "\u250F",
        "top_right_corner": "\u2513",
        "bot_left_corner": "\u2517",
        "bot_right_corner": "\u251B",
        "horizontal_line": "\u2501",
        "vertical_line": "\u2503",
        "empty": " ",
    }

    CHAR_SET_SINGLE_LIGHT_LINES_ROUNDED_CORNERS = {
        "top_left_corner": "\u256D",
        "top_right_corner": "\u256E",
        "bot_left_corner": "\u2570",
        "bot_right_corner": "\u256F",
        "horizontal_line": "\u2500",
        "vertical_line": "\u2502",
        "empty": " ",
    }

    CHAR_SET_DOUBLE_LINES = {
        "top_left_corner": "\u2554",
        "top_right_corner": "\u2557",
        "bot_left_corner": "\u255A",
        "bot_right_corner": "\u255D",
        "horizontal_line": "\u2550",
        "vertical_line": "\u2551",
        "empty": " ",
    }
    return (
        CHAR_SET_DOUBLE_LINES,
        CHAR_SET_SINGLE_LIGHT_LINES,
        Dimensions,
        Position,
    )


@app.cell(hide_code=True)
def _():
    return


if __name__ == "__main__":
    app.run()
