from pygame.math import Vector2 as vec

#####################################
# /absolute variables of the world\ #

WIDTH: int = 560
HEIGHT: int = 620

FUllSCREEN: tuple = (WIDTH, HEIGHT)

MAIN_FILE: str = 'MyPacman'
FILES = ('images', 'sounds', 'fonts')

TITLE_GAME: str = 'Oh, PACman'

ICON: str = 'iconPac.png'

BACKGROUND: tuple = (0, 0, 0)
WALL_BACKGROUND: str = 'walls.txt'

FPS: int | float = 60

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

# $ Collisions $ #
WIDTH_CELL: int | float = WIDTH // 28
HEIGHT_CELL: int | float = HEIGHT // 30

# $ Player $ #
PLAYER_START_POS = vec(1, 1)

# $$ Sprites Player $$ #
SPRITE_PACMAN: dict = {'PACMAN_ATTACK': 'pacman_attack.png',
                       'PACMAN_RUN': 'pacman_run.png'}

# $ Texts Wold $ #
text_START: str = '-Pressione uma tecla para jogar'
text_DEV: str = 'ClasRCDM'
text_FOR: str = 'João Tinti'

# \global variables/ #
#####################################
