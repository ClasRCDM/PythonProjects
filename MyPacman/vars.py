from pygame.math import Vector2 as vec
from os import path, getcwd  # Get files

#####################################
# /absolute variables of the world\ #

WIDTH: int = 610
HEIGHT: int = 670

FUllSCREEN: tuple = (WIDTH, HEIGHT)

MAIN_FILE: str = 'MyPacman'
FILES = ('images', 'sounds', 'fonts')

TITLE_GAME: str = 'Oh, PACman'

ICON: str = 'iconPac.png'

BACKGROUND: tuple = (0, 0, 0)

FPS: int | float = 60

TOP_BOTTOM_BUFFER = 50
MAZE_WIDTH, MAZE_HEIGHT = WIDTH-TOP_BOTTOM_BUFFER, HEIGHT-TOP_BOTTOM_BUFFER

FONT: str = 'PressStart2P.ttf'

# \absolute variables of the world/ #
#####################################
# /global variables\ #

# Scenes #
game_start: bool = True
game: bool = False

MUSICS: str = 'StartGame_music'

# $ Images $ #
LOGO_PACMAN: str = 'PACMANLOGO.png'
MAZE_BACKGROUND: str = 'maze.png'

# $ TXT $ #
WALL_BACKGROUND: str = 'walls.txt'

# $ Sounds $ #
music_START: str = 'intermission.wav'
music_PLAY: str = 'munch_1.wav'
music_BACKGROUND: str = 'songs/ManThemeRemix_arsenic1987.mp3'

# $ Colors $ #
YELLOW: tuple = (244, 233, 51)
WHITE: tuple = (255, 255, 255)
GREY: tuple = (72, 72, 72)
RED: tuple = (255, 0, 0)
PURPLE: tuple = (218, 112, 214)
BLUE: tuple = (30, 144, 255)

# $ Collisions $ #
WIDTH_CELL: int | float = WIDTH // 28
HEIGHT_CELL: int | float = HEIGHT // 30

# $$ Sprites Player $$ #
SPRITE_PACMAN: dict = {'PACMAN_ATTACK': 'pacman_attack.png',
                       'PACMAN_RUN': 'pacman_run.png'}

# $ Enemies $ #
SPRITE_ENEMIES: list = ['enemy_0.png',
                        'enemy_1.png',
                        'enemy_2.png',
                        'enemy_3.png']

# $ Texts Wold $ #
text_START: str = '-Pressione espaço para jogar'
text_DEV: str = 'ClasRCDM'
text_FOR: str = 'João Tinti'

# \global variables/ #
#####################################

ROWS = 30
COLS = 28
