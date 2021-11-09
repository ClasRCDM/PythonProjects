from pygame import sprite, mask
from pygame.math import Vector2 as vec
from pygame import KEYDOWN,\
    K_LEFT, K_a, K_RIGHT, K_d, K_UP, K_w, K_DOWN, K_s
from pygame import image as img, transform as tfm

import vars as v


class player_pacman(sprite.Sprite):
    def __init__(self, image) -> None:
        sprite.Sprite.__init__(self)

        #################################
        # /player's absolute variables\ #
        self.image = img.load(image).convert()
        self.image = tfm.scale(self.image, (17, 17))

        self.rect = self.image.get_rect()

        self.grid_pos: vec = v.PLAYER_START_POS
        self.pix_pos = self.get_pix_pos()

        self.direction: vec = vec(1, 0)

        self.Stored_direction = None
        self.able_to_move: bool = True
        self.togle_to_move = True
        # \player's absolute variables/ #
        #################################

    def update(self):
        # Player square
        self.grid_pos[0] = \
            (self.pix_pos[0] + v.WIDTH_CELL // 2) // v.WIDTH_CELL
        self.grid_pos[1] = \
            (self.pix_pos[1] + v.WIDTH_CELL // 2) // v.WIDTH_CELL

        # Add current player position
        self.move_update()
        self.rect[0] = self.pix_pos.x
        self.rect[1] = self.pix_pos.y

    def pacman_movement(self, ev):  # Check movement inputs
        if ev.type == KEYDOWN:
            if ev.key == K_LEFT or ev.key == K_a:
                self.move(vec(-1, 0))
            if ev.key == K_RIGHT or ev.key == K_d:
                self.move(vec(1, 0))
            if ev.key == K_UP or ev.key == K_w:
                self.move(vec(0, -1))
            if ev.key == K_DOWN or ev.key == K_s:
                self.move(vec(0, 1))

    def eat_coin(self, on_coin, coins):  # Check and eat the coins
        if on_coin:
            coins.remove(self.grid_pos)

    def move(self, direction):
        self.Stored_direction = direction

    def move_update(self):
        # Character direction
        if self.togle_to_move:
            self.pix_pos += self.direction
        else:
            self.move(vec(0, 1))

        self.time_to_move()

    def time_to_move(self):  # Check if the player can move
        if (self.pix_pos.x + 40 // 2) % v.WIDTH_CELL == 1:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                if self.Stored_direction is not None:
                    self.direction = self.Stored_direction
        if (self.pix_pos.y + 40 // 2) % v.HEIGHT_CELL == 1:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                if self.Stored_direction is not None:
                    self.direction = self.Stored_direction

    def get_pix_pos(self) -> vec:  # Grid pos player
        return vec(self.grid_pos.x * v.WIDTH_CELL + 2,
                   self.grid_pos.y * v.HEIGHT_CELL + 2)
        print(self.grid_pos, self.pix_pos)
