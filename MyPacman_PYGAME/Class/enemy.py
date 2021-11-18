from pygame.math import Vector2 as vec
from pygame import draw

from Class.entity import entity_mob

from math import degrees, sin, atan2, radians, cos
from vars import GREY, TOP_BOTTOM_BUFFER


class Enemy(entity_mob):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        entity_mob.__init__(self, image, file_walls,
                            cell_width, cell_height,
                            walls)

    def way_traversed(self, screen,
                      lcolor, tricolor,
                      start: vec, end: vec, trirad):
        draw.line(screen, lcolor, start, end, 2)
        rotation = degrees(
            (atan2(start[1] - end[1], end[0] - start[0])) + 90)
        draw.polygon(screen, tricolor,
                     ((end[0] + trirad * sin(
                         radians(rotation)),
                       end[1] + trirad * cos(
                           radians(rotation))),
                      (end[0] + trirad * sin(
                          radians(rotation - 120)),
                       end[1] + trirad * cos(
                           radians(rotation - 120))),
                      (end[0] + trirad * sin(
                          radians(rotation + 120)),
                       end[1] + trirad * cos(
                           radians(rotation + 120)))))

    def get_pos(self) -> vec:  # Get and add enemy position
        return vec((self.arrow_pos[0] * self.cell_width)
                   + TOP_BOTTOM_BUFFER // 2
                   + self.cell_width // 2,
                   (self.arrow_pos[1] * self.cell_height)
                   + TOP_BOTTOM_BUFFER // 2
                   + self.cell_height // 2)


class Blinky(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str, screen) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)
        self.screen = screen

        self.arrow_pos = vec(1, 1)

    def update(self):
        self.update_moves()
        self.way_traversed(self.screen,
                           GREY, GREY,
                           self.pix_pos, self.get_pos(), 5)

    def set_spawn(self, spawn: str = '!'):
        return spawn


class Inky(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str, screen) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)
        self.screen = screen

    def set_spawn(self, spawn: str = '@'):
        return spawn


class Pinky(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)

    def update(self):
        self.update_moves()

    def set_spawn(self, spawn: str = '#'):
        return spawn


class Clyde(Enemy):
    def __init__(self, image: str, walls: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        Enemy.__init__(self, image, walls,
                       cell_width, cell_height,
                       file_walls)

    def update(self):
        self.update_moves()

    def set_spawn(self, spawn: str = '$'):
        return spawn
