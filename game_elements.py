import pygame
import utils

COLORTYPE = tuple[int, int, int, int]
COLORS = pygame.colordict.THECOLORS
SETTINGS = utils.load_settings()


class Cell:
    def __init__(
        self,
        width_height: int,
        row,
        col,
        pos_x,
        pos_y,
        color_alive: COLORTYPE,  # RGBA
        color_dead: COLORTYPE,  # RGBA
    ):
        self.width_height = width_height
        self.row = row
        self.col = col
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color_dead = color_dead
        self.color_alive = color_alive
        self.current_color = color_dead
        self.rect = pygame.Rect(pos_x, pos_y, width_height, width_height)
        self.is_alive = False

    def kill(self):
        self.is_alive = False
        self.current_color = self.color_dead

    def revive(self):
        self.is_alive = True
        self.current_color = self.color_alive


class Board:
    def __init__(
        self, width: int | float, height: int | float, cell_count_per_row: int
    ):
        self.width = width
        self.height = height
        self.cell_count_per_row = cell_count_per_row
        self.surface = pygame.Surface(size=(width, height))
        self.cells = self._make_cells()

    def _make_cells(self) -> list[list[Cell]]:
        cell_width = self.width // self.cell_count_per_row
        cells = []
        for y in range(self.cell_count_per_row):
            row = []
            for x in range(self.cell_count_per_row):
                cell_x, cell_y = x * cell_width, y * cell_width
                new_cell = Cell(
                    cell_width,
                    x,
                    y,
                    cell_x,
                    cell_y,
                    COLORS[SETTINGS["cell_color_alive"]],
                    COLORS[SETTINGS["cell_color_dead"]],
                )
                row.append(new_cell)
            cells.append(row)
        return cells

    def find_cells_by_coordinate(self, x, y):
        # # finding y
        # current_up = 0
        # current_down = len(self.cells)
        # current_center_row = len(self.cells) // 2
        # while True:
        #     current_cell = self.cells[current_center_row][0]
        #     if (current_cell.pos_y >= y > current_cell.pos_y + current_cell.width_height):
        #         break

        #     if y < current_cell.pos_y:
        #         current_down -= (abs(current_up - current_down) // 2)
        #         current_center_row = (abs(current_up - current_down) // 2)
        #     if y > current_cell.pos_y:
        #         current_down -= current_center_row

        #     current_center_row = abs(current_up - current_down) // 2

        # # finding x
        # current_left = 0
        # current_right = len(self.cells[0])
        # current_center_col = abs(current_right - current_left) // 2
        # while True:
        #     current_cell = self.cells[0][current_center_col]
        #     if current_cell.pos_x >= x > current_cell.pos_x + current_cell.width_height:
        #         break

        #     if x < current_cell.pos_x:
        #         current_right -= current_center_col
        #     if x > current_cell.pos_x:
        #         current_left += current_center_col

        #     current_center_col = abs(current_right - current_left) // 2
        target_cell = None
        for row in self.cells:
            for cell in row:
                if (cell.pos_x < x < cell.pos_x + cell.width_height) and (
                    cell.pos_y < y < cell.pos_y + cell.width_height
                ):
                    target_cell = cell
                    break

        return target_cell
