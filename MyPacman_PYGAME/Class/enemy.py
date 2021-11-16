# from pygame.math import Vector2 as vec

from Class.entity import entity_mob


class Enemy(entity_mob):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        entity_mob.__init__(self, image, file_walls,
                            cell_width, cell_height,
                            walls)


class Blinky(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)


class Inky(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)


class Pinky(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)


class Clyde(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)
