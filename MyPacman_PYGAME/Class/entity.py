from pygame import sprite
from pygame import image as img
from pygame.math import Vector2 as vec

import vars as v


class entity_mob(sprite.Sprite):
    def __init__(self, entity_sprite: str, file_wall: str,
                 cell_width: int, cell_height: int,
                 wall: list[int]) -> None:

        sprite.Sprite.__init__(self)

        ###############################
        # /Absolute entity variables\ #
        self.image = img.load(entity_sprite)

        self.rect = self.image.get_rect()

        # $ Movement cell size $ #
        self.cell_width, self.cell_height = cell_width, cell_height

        # $ Location/ Start and End$ #
        self.grid_pos: vec = self.get_location(file_wall)
        self.pix_pos: vec = self.get_pix_pos()

        self.direction_mov: vec = vec(0, 0)

        # $ Get location walls and coins $ #
        self.walls: list[int] = wall

        # $ Wall variables $ #
        self.stored_direction, self.able_to_move = None, True

        # $ Lives, velocity and Points $ #
        self.speed, self.lives = 2, 1
        # \Absolute entity variables/ #
        ###############################

    def update_moves(self):
        if self.able_to_move:  # Add movement player
            self.pix_pos += self.direction_mov * self.speed

        if self.check_capsule():  # Check if you can move
            if self.stored_direction is not None:
                self.direction_mov = self.stored_direction
            self.able_to_move = self.break_move()

        # Setting grid position in reference to pix pos
        self.grid_pos[0] = (self.pix_pos[0] - v.TOP_BOTTOM_BUFFER +
                            self.cell_width // 2) // self.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - v.TOP_BOTTOM_BUFFER +
                            self.cell_height // 2) // self.cell_height + 1

        # Set position global player
        self.rect[0] = self.pix_pos.x - int(v.TOP_BOTTOM_BUFFER / 5.5)
        self.rect[1] = self.pix_pos.y - int(v.TOP_BOTTOM_BUFFER / 6)

    def get_location(self, file):  # Set entity location
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in self.set_spawn():
                        return vec(xidx, yidx)

    def move(self, direction_mov):  # move! k
        self.stored_direction: vec = direction_mov

    def break_move(self) -> bool:  # Check if it collided with the wall
        return self.get_objects(self.walls, vec(self.grid_pos + self.direction_mov))

    def get_objects(self, object, another_object):
        for item in object:  # Returns false if pasted with object
            if another_object == item:
                return False
        return True

    def check_capsule(self):  # Check if it can move inside the capsules
        return self.get_capsule(self.pix_pos.x, self.cell_width, (vec(1, 0), vec(-1, 0))) or \
            self.get_capsule(self.pix_pos.y, self.cell_height, (vec(0, 1), vec(0, -1)))

    def get_capsule(self, direction, cell_size, mov):  # Calculates the entity's position in the capsules
        if int(direction + v.TOP_BOTTOM_BUFFER // 2) % cell_size == 0:
            return self.get_direction(mov)

    def get_direction(self, mov):  # Check entity direction
        if self.direction_mov == mov[0] or self.direction_mov == mov[1] or\
                self.direction_mov == vec(0, 0):
            return True

    def get_pix_pos(self) -> vec:  # Get and add player position
        return vec((self.grid_pos[0] * self.cell_width)
                   + v.TOP_BOTTOM_BUFFER // 2
                   + self.cell_width // 2,
                   (self.grid_pos[1] * self.cell_height)
                   + v.TOP_BOTTOM_BUFFER // 2
                   + self.cell_height // 2)
