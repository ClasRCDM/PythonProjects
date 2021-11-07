from pygame.math import Vector2 as vec
from os import path, getcwd

import Class.enemy as e
import vars as v


class spawn_enemies:
    def __init__(self, wall, walls):
        self.enemies: list = []

        self.wall_dirc: str = wall
        self.walls = walls

        self.grid_pos_enemies: list = []

        self.value_sprite: int = 0
        self.directory = path.join(getcwd(), v.MAIN_FILE, v.FILES[0])

        self.get_location(self.wall_dirc)

        self.set_enemies()

    def draw(self, screen):
        self.enemies.draw(screen)

    def get_location(self, file):
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in ['2', '3', '4', '5']:
                        self.grid_pos_enemies.append(vec(xidx, yidx))

    def set_enemies(self):
        for pos in self.grid_pos_enemies:
            sprite = path.join(self.directory, v.SPRITE_ENEMIES[self.value_sprite])
            self.value_sprite += 1
            self.enemies.append(e.enemy(sprite, pos, 0, self.walls))

    def group(self):
        return self.enemies
