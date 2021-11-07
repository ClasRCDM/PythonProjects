from pygame import sprite
from pygame.math import Vector2 as vec
from pygame import image as img, transform as tfm

import vars as v
import random


class enemy(sprite.Sprite):
    def __init__(self, image, grid_pos, number, wall) -> None:
        sprite.Sprite.__init__(self)

        #################################
        # /player's absolute variables\ #
        self.image = img.load(image).convert_alpha()
        self.image = tfm.scale(self.image, (17, 17))

        self.grid_pos = grid_pos

        self.rect = self.image.get_rect()
        self.pix_pos = self.get_pix_pos()

        self.rect[0] = self.pix_pos.x
        self.rect[1] = self.pix_pos.y
        # \player's absolute variables/ #
        #################################

    def update(self):
        # Add current player position
        self.rect[0] = self.pix_pos.x
        self.rect[1] = self.pix_pos.y

    def get_pix_pos(self) -> vec:  # Grid pos enemy
        return vec(self.grid_pos.x * v.WIDTH_CELL + 2,
                   self.grid_pos.y * v.HEIGHT_CELL + 2)
