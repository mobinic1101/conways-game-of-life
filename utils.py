import json


def create_settings_file():
    with open("./settings.json", "+w") as settings_file:
        settings_file.write("""
{
    "screen_width": 800,
    "screen_height": 600,
    "board_width": 800,
    "board_height": 600,
    "board_color": "white",
    "board_grid_lines_color": "black",
    "board_grid_lines_thickness": 1,
    "cell_per_row": 20,
    "cell_color_dead": "white",
    "cell_color_alive": "yellow",
    "update_speed": 2000
}
""")


def load_settings() -> dict:
    try:
        with open("./settings.json", "r") as file_:
            settings = json.load(file_)
    except FileNotFoundError as err:
        print(err)
        create_settings_file()
        return load_settings()
    return settings
