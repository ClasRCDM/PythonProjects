from pygame import sprite
from pygame.math import Vector2 as vec
from os import path, getcwd

import Class.enemy as e
import vars as v


class spawn_enemies:
    def __init__(self, wall):
        self.enemies = sprite.Group()

        self.wall_dirc: str = wall

        self.pix_pos_enemies: list = []
        self.grid_pos_enemies: list = []

        self.value_sprite: int = 0
        self.directory = path.join(getcwd(), v.MAIN_FILE, v.FILES[0])

        self.get_location(self.wall_dirc)

        for value in self.grid_pos_enemies:
            self.pix_pos_enemies.append(self.get_pix_pos(value))

        self.set_enemies()

    def draw(self, screen):
        self.enemies.draw(screen)

    def get_location(self, file):
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in ['2', '3', '4', '5']:
                        self.grid_pos_enemies.append(vec(xidx, yidx))

    def get_pix_pos(self, value) -> vec:  # Grid pos enemies
        return vec(value.x * v.WIDTH_CELL + 2,
                   value.y * v.HEIGHT_CELL + 2)

    def set_enemies(self):
        for pos in self.pix_pos_enemies:
            self.sprite = path.join(self.directory, v.SPRITE_ENEMIES[self.value_sprite])
            self.value_sprite += 1
            self.enemies.add(e.enemy(self.sprite, pos.x, pos.y))
