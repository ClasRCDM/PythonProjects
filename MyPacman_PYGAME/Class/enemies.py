from pygame.math import Vector2 as vec
from os import path, getcwd

import Class.enemy as e
import vars as v


class spawn_enemies:
    def __init__(self, pacman_loc, screen,
                 wall_dirc: str, walls: list,
                 cell_height: int, cell_width: int):
        self.enemies: list = []
        self.pacman_loc = pacman_loc

        self.screen = screen

        self.wall_dirc: str = wall_dirc
        self.walls: list = walls

        self.cell_height, self.cell_width = cell_height, cell_width

        self.grid_pos_enemies: list = []

        self.directory = path.join(getcwd(), v.MAIN_FILE, v.FILES[0])

        self.get_location(self.wall_dirc)

    def get_location(self, file):
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in ['2', '3', '4', '5']:
                        self.grid_pos_enemies.append(vec(xidx, yidx))

    def group(self):
        return self.enemies
