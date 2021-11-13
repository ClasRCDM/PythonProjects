from pygame import sprite
from pygame.math import Vector2 as vec
from pygame import image as img
from random import randint

import vars as v


class enemy(sprite.Sprite):
    def __init__(self, image: str,
                 grid_pos: vec, number: int,
                 cell_height: int, cell_width: int,
                 walls: list) -> None:
        sprite.Sprite.__init__(self)

        #################################
        # /player's absolute variables\ #
        self.image = img.load(image).convert_alpha()

        self.cell_height, self.cell_width = cell_height, cell_width

        self.grid_pos: vec = grid_pos

        self.rect = self.image.get_rect()
        self.pix_pos = self.get_pix_pos()

        self.number: int = number

        self.direction: vec = vec(0, 0)

        self.walls: list[int] = walls

        self.personality: str = self.set_personality()
        self.target = None

        self.speed: int = self.set_speed()
        # \player's absolute variables/ #
        #################################

    def update(self):
        if self.target != self.grid_pos:
            self.pix_pos += self.direction * self.speed
            if self.time_to_move():
                self.move()

        # Setting grid position in reference to pix position
        self.grid_pos[0] = (self.pix_pos[0] - v.TOP_BOTTOM_BUFFER +
                            self.cell_width // 2) // self.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - v.TOP_BOTTOM_BUFFER +
                            self.cell_height // 2) // self.cell_height + 1

        # Set position global enemy
        self.rect[0] = self.pix_pos.x - int(v.TOP_BOTTOM_BUFFER / 5.5)
        self.rect[1] = self.pix_pos.y - int(v.TOP_BOTTOM_BUFFER / 6)

    def move(self):
        if self.personality == "random":
            self.direction = self.get_random_direction()

    def time_to_move(self):
        if int(self.pix_pos.x + v.TOP_BOTTOM_BUFFER // 2) %\
                self.cell_width == 0:
            if self.direction == vec(1, 0) or\
                    self.direction == vec(-1, 0) or\
                    self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y + v.TOP_BOTTOM_BUFFER // 2) %\
                self.cell_height == 0:
            if self.direction == vec(0, 1) or\
                    self.direction == vec(0, -1) or\
                    self.direction == vec(0, 0):
                return True
        return False

    def set_speed(self) -> int:
        if self.personality in ["speedy", "scared"]:
            speed = 2
        else:
            speed = 1
        return speed

    def get_random_direction(self) -> vec:
        while True:
            number = randint(-2, 1)
            if number == -2:
                x_dir, y_dir = 1, 0
            elif number == -1:
                x_dir, y_dir = 0, 1
            elif number == 0:
                x_dir, y_dir = -1, 0
            else:
                x_dir, y_dir = 0, -1
            next_pos = vec(self.grid_pos.x + x_dir, self.grid_pos.y + y_dir)
            if next_pos not in self.walls:
                break
        return vec(x_dir, y_dir)

    def get_pix_pos(self) -> vec:
        return vec((self.grid_pos.x * self.cell_width)
                   + v.TOP_BOTTOM_BUFFER // 2 + self.cell_width // 2,
                   (self.grid_pos.y * self.cell_height)
                   + v.TOP_BOTTOM_BUFFER // 2 +
                   self.cell_height // 2)

    def set_personality(self) -> str:
        if self.number == 0:
            return "random"
        elif self.number == 1:
            return "random"
        elif self.number == 2:
            return "random"
        else:
            return "random"
