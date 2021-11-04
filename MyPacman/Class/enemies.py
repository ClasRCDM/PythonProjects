import vars as v

from pygame import sprite, image
from pygame.math import Vector2 as vec


class enemies():
    def __init__(self, screen, wall) -> None:
        ###################################
        # /​​absolute background variables\ #
        self.grid_pos = v.PLAYER_START_POS
        self.pix_pos = self.get_pix_pos()

        self.enemies: list = []
        self.enemy_pos: list = []

        self.screen = screen
        # \​​absolute background variables/ #
        ###################################

        self.load_enemies(wall)

    def enemy(self):
        pass

    def make_enemies(self):
        for enemy_pos in self.enemy_pos:
            self.enemies.append(self.enemy(enemy_pos))

    def load_enemies(self, wall):
        with open(wall, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in ['2', '3', '4', '5']:
                        self.enemy_pos.append(vec(yidx, xidx))

    def get_pix_pos(self) -> vec:  # Grid pos enemy
        return vec(self.grid_pos.x * v.WIDTH_CELL + 2,
                   self.grid_pos.y * v.HEIGHT_CELL + 2)
        print(self.grid_pos, self.pix_pos)
