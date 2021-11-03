from pygame import sprite
from pygame.math import Vector2 as vec

import vars as v
import pygame


class player_pacman(sprite.Sprite):
    def __init__(self, image) -> None:
        sprite.Sprite.__init__(self)

        #################################
        # /player's absolute variables\ #
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (17, 17))

        self.rect = self.image.get_rect()

        self.grid_pos = v.PLAYER_START_POS
        self.direction = vec(1, 0)

        self.pix_pos = self.get_pix_pos()
        self.Stored_direction = None

        self.rect[0] = self.pix_pos.x
        self.rect[1] = self.pix_pos.y
        # \player's absolute variables/ #
        #################################

    def update(self):
        # Character direction
        self.pix_pos += self.direction
        if self.time_to_move('x'):
            if self.Stored_direction is not None:
                self.direction = self.Stored_direction
        if self.time_to_move('y'):
            if self.Stored_direction is not None:
                self.direction = self.Stored_direction

        # Player square
        self.grid_pos[0] = \
            (self.pix_pos[0] + v.WIDTH_CELL // 2) // v.WIDTH_CELL
        self.grid_pos[1] = \
            (self.pix_pos[1] + v.WIDTH_CELL // 2) // v.WIDTH_CELL

        # Add current player position
        self.rect[0] = self.pix_pos.x
        self.rect[1] = self.pix_pos.y

    def pacman_movement(self, ev):  # Check movement inputs
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT or ev.key == pygame.K_a:
                self.move(vec(-1, 0))
            if ev.key == pygame.K_RIGHT or ev.key == pygame.K_d:
                self.move(vec(1, 0))
            if ev.key == pygame.K_UP or ev.key == pygame.K_w:
                self.move(vec(0, -1))
            if ev.key == pygame.K_DOWN or ev.key == pygame.K_s:
                self.move(vec(0, 1))

    def move(self, direction):
        self.Stored_direction = direction

    def time_to_move(self, dirc: str):
        if (self.pix_pos.x // 2) % v.WIDTH_CELL == 1 and dirc == 'x':
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                return True
        if (self.pix_pos.y // 2) % v.HEIGHT_CELL == 1 and dirc == 'y':
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                return True

    def get_pix_pos(self) -> vec:  # Grid player
        return vec(self.grid_pos.x * v.WIDTH_CELL + 2,
                   self.grid_pos.y * v.HEIGHT_CELL + 2)
        print(self.grid_pos, self.pix_pos)
