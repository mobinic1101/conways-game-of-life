import datetime
import random
import pygame
from game_elements import Board, Cell, COLORS, SETTINGS
from painter import Painter


pygame.init()
clock = pygame.Clock()
screen = pygame.display.set_mode((SETTINGS["screen_width"], SETTINGS["screen_height"]))


def random_revive_cells(board: Board, cell_revive_chance: str="1/5"):
    cell_revive_chance = cell_revive_chance.split("/")
    trues, falses = int(cell_revive_chance[0]), int(cell_revive_chance[1])
    chances = []
    for _ in range(trues):
        chances.append(True)
    for _ in range(falses):
        chances.append(False)
    for row in board.cells:
        for cell in row:
            if random.choice(chances):
                cell.revive()

def revive_all_cells(board: Board):
    for row in board.cells:
        for cell in row:
            cell.revive()

def kill_all_cells(board: Board):
    for row in board.cells:
        for cell in row:
            cell.kill()


def get_cell_neighbors(cell: Cell, board:Board):
    # neighbors: list[Cell] = []
    # if cell.row > 0:
    #     neighbors.append(board.cells[cell.row - 1][cell.col]) # up
    #     if cell.col > 0:
    #         neighbors.append(board.cells[cell.row - 1][cell.col - 1]) # up_left
    #     if cell.col < len(board.cells[0]) - 1:
    #         neighbors.append(board.cells[cell.row - 1][cell.col + 1]) # up_right
    # if cell.row < len(board.cells) - 1:
    #     neighbors.append(board.cells[cell.row + 1][cell.col]) # down
    #     if cell.col > 0:
    #         neighbors.append(board.cells[cell.row + 1][cell.col - 1]) # down_left
    #     if cell.col < len(board.cells[0]) - 1:
    #         neighbors.append(board.cells[cell.row + 1][cell.col + 1]) # down_right
    # if cell.col > 0:
    #     neighbors.append(board.cells[cell.row][cell.col - 1]) # left
    # if cell.col < len(board.cells[0]) - 1:
    #     neighbors.append(board.cells[cell.row][cell.col + 1]) # right
    neighbors: list[Cell] = []
    neighbor_directions = [(-1, -1), (-1, 0), (-1, +1),
                           (0, -1), (0, 0), (0, +1),
                           (+1, -1), (+1, 0), (+1, +1)]
    for direction in neighbor_directions:
        if direction == (0, 0): continue # exclude the cell itself.
        neighbor = cell.col + direction[1], cell.row + direction[0]
        if (len(board.cells) -1 >= neighbor[0] >= 0) and (len(board.cells[0]) - 1 >= neighbor[1] >= 0):
            neighbors.append(board.cells[neighbor[0]][neighbor[1]])

    return neighbors, sum(1 for neighbor in neighbors if neighbor.is_alive)


def apply_cells_logic(board: Board):
    cells_to_change: list[Cell, str] = []
    for row in board.cells:
        for cell in row:
            neighbors, neighbors_count = get_cell_neighbors(cell, board)
            
            if cell.is_alive:
                if neighbors_count <= 1: # dies
                    cells_to_change.append((cell, "kill"))
                elif neighbors_count >= 4: # dies
                    cells_to_change.append((cell, "kill"))
                elif 1 < neighbors_count < 4: # survives
                    pass
            else:
                if neighbors_count == 3:
                    cells_to_change.append((cell, "revive"))

    for cell, action in cells_to_change:
        if action == "kill":
            cell.kill()
        elif action == "revive":
            cell.revive()

def main():
    fps = 60
    game_running = True
    board = Board(SETTINGS["board_width"], SETTINGS["board_height"], SETTINGS["cell_per_row"])
    painter = Painter(board)
    random_revive_cells(board)
    update_cells = True
    cells_update_time = datetime.timedelta(milliseconds=SETTINGS["update_speed"])
    cells_next_update_time = datetime.datetime.now() + cells_update_time
    while game_running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    revive_all_cells(board)
                if event.key == pygame.K_r: # revive cells randomly
                    random_revive_cells(board)
                if event.key == pygame.K_c: # kills all cells (clears the board)
                    kill_all_cells(board)
                if event.key == pygame.K_l: # removes/shows grid lines
                    painter.draw_grid_lines = False if painter.draw_grid_lines else True
                if event.key == pygame.K_SPACE: # pause/resume
                    update_cells = True if not update_cells else False
                    if not update_cells:
                        print("update paused.")
                    else: print("update resumed.")

        buttons = pygame.mouse.get_pressed()
        if any(buttons):
            mouse_pos = pygame.mouse.get_pos()
            clicked_cell = board.find_cells_by_coordinate(*mouse_pos)

            if clicked_cell is not None:
                # print(f"cell count: {get_cell_neighbors(clicked_cell, board)[1]}")
                if buttons[0]: # left click
                    clicked_cell.revive()
                elif buttons[2]: # right click
                    clicked_cell.kill()

        current_time = datetime.datetime.now()
        if update_cells and current_time >= cells_next_update_time:
            apply_cells_logic(board)
            cells_next_update_time = current_time + cells_update_time
        
        painter.draw_elements(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()




