from pygame import sprite
from pygame.math import Vector2 as vec
from os import path, getcwd

import Class.enemy as e
import vars as v


class spawn_enemies:
    def __init__(self, wall):
        self.enemies = sprite.Group()
        self.grid_pos: list = []
        self.wall_dirc: str = wall

        self.directory = path.join(getcwd(), v.MAIN_FILE, v.FILES[0])
        self.sprite = path.join(self.directory, v.SPRITE_ENEMIES['Enemy_1'])

        self.get_location(self.wall_dirc)
        self.set_enemies()

    def draw(self, screen):
        self.enemies.draw(screen)

    def get_location(self, file):
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in ['2', '3', '4', '5']:
                        self.grid_pos.append(vec(xidx, yidx))

    def set_enemies(self):
        for enemy in self.grid_pos:
            print(enemy)
            self.enemies.add(e.enemy(self.sprite, enemy.x, enemy.y))
