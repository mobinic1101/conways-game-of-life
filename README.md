<img width="480" height="480" alt="gol" src="https://github.com/user-attachments/assets/fed38150-635a-431a-9e00-fa694806ffaa" />


## how to run
1. clone the repository
`git clone https://github.com/mobinic1101/conways-game-of-life.git`
2. cd into the game directory
`cd conways-game-of-life`
3. install pygame
`pip install pygame`
4. run the main.py file
`python main.py`

use the controls listed below, then pause the simulation and clear the board, then draw a symmetrical shape and then hit space...

## controls
- **space**      -> pause/resume the simulation.
- **R**          -> resets the board with random cells.
- **C**          -> clears the board (kills all the cells).
- **A**          -> fills the board (revives all the cells).
- **L**          -> shows/hides grid lines.
- **LeftClick**  -> press and hold to keep reviving cells under the cursor.
- **RightClick** -> press and hold to keep killing cells under the cursor.


## change game settings
settings.json is the file for game settings.
increase/decrease `update_speed` to increasae or decrease the simulation speed.
to see full list of available colors, checkout `pygame.colordict` module. 
other settings are self explanatory.

<hr/>
contributions are welcome!