import pygame
import game_elements

COLORS = game_elements.COLORS
SETTINGS = game_elements.SETTINGS
# {
#     "screen_width": 800,
#     "screen_height": 600,
#     "board_width": 800,
#     "board_height": 600,
#     "board_color": "white",
#     "board_grid_lines_color": "black",
#     "board_grid_lines_thickness": 1,
#     "cell_per_row": 20,
#     "cell_color_dead": "white",
#     "cell_color_alive": "yellow"
# }


class Painter:
    def __init__(self, board: game_elements.Board):
        self.draw_grid_lines = True
        self.board = board

    def _draw_lines(self, surface: pygame.Surface):
        cell_width = self.board.width // self.board.cell_count_per_row
        for i in range(self.board.cell_count_per_row):
            # horizontal lines
            start = (0, i * cell_width)
            end = (self.board.width, i * cell_width)
            pygame.draw.line(
                surface,
                COLORS[SETTINGS["board_grid_lines_color"]],
                start,
                end,
                SETTINGS["board_grid_lines_thickness"],
            )

            # vertical lines
            start = (i * cell_width, 0)
            end = (i * cell_width, self.board.height)
            pygame.draw.line(
                surface,
                COLORS[SETTINGS["board_grid_lines_color"]],
                start,
                end,
                SETTINGS["board_grid_lines_thickness"],
            )

    def draw_elements(self, main_surface: pygame.Surface):
        # drawing board
        main_surface.blit(self.board.surface)
        # drawing cells
        for row in self.board.cells:
            for cell in row:
                pygame.draw.rect(
                    main_surface,
                    cell.current_color,
                    cell.rect,
                )
        if self.draw_grid_lines:
            self._draw_lines(main_surface)
