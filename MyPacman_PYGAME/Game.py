from Oh_Pacman import World
from vars import TITLE_GAME


def init_game():
    MyWorld = World(TITLE_GAME)
    MyWorld.World_init()


if __name__ == '__main__':
    init_game()
