from pygame import Surface, event
from pygame.math import Vector2 as vec
from pygame import KEYDOWN, K_a, K_d, K_w, K_s
from pygame import image as img

import vars as v

from Class.entity import entity_mob


class pacman(entity_mob):
    def __init__(self, image: str, walls: list[int],
                 coins: list[int], big_coins: list[int],
                 cell_width: int, cell_height: int,
                 file_walls: str) -> None:

        entity_mob.__init__(self, image, file_walls,
                            cell_width, cell_height,
                            walls)
        event.set_allowed([KEYDOWN, K_a, K_d, K_w, K_s])

        #################################
        # /player's absolute variables\ #
        self.pacman = img.load(image)

        self.set_sprite(0)

        # $ Location/ Start and End$ #
        self.direction_pos = None

        # $ Get location walls and coins $ #
        self.coins, self.big_coins = coins, big_coins

        # $ Wall variables $ #
        self.capsule_mov = list[int]()
        self.capsule_mov = self.get_capsule_move(file_walls)

        # \player's absolute variables/ #
        #################################

    def update(self):
        self.update_moves()

        self.set_driving_state()  # Say you can go forward or backward

        if self.on_coin():  # Eat coins
            self.eat_coin(self.coins)
        elif self.on_big_coin():  # Eat big coins
            self.eat_big_coin(self.big_coins)

    def move(self, direction_mov, sprite):  # move! k
        self.stored_direction: vec = direction_mov
        self.set_sprite(sprite)

    def get_capsule_move(self, file):  # Set loocation player
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in 'D':
                        self.capsule_mov.append(vec(xidx, yidx))
        return self.capsule_mov

    def get_sprite(self, frame: int):
        surface = Surface(
            (v.WIDTH_PACMAN, v.HEIGHT_PACMAN)).convert_alpha()
        surface.blit(self.pacman,
                     (0, 0),
                     ((frame * v.WIDTH_PACMAN), 0,
                      v.WIDTH_PACMAN, v.HEIGHT_PACMAN))
        surface.set_colorkey(v.BLACK)
        return surface

    def set_sprite(self, direction):
        self.image = self.get_sprite(direction)

    def set_spawn(self, spawn: str = 'P'):
        return spawn

    def eat_coin(self, coins):  # Check and eat the coins
        coins.remove(self.grid_pos)

    def eat_big_coin(self, big_coins):  # Check and eat the big coins
        big_coins.remove(self.grid_pos)

    def on_coin(self) -> bool:  # Check if it collided with a coin
        # if self.grid_pos in self.coins:
        return self.check_capsule() if self.grid_pos in self.coins else False

    def on_big_coin(self) -> bool:  # Check if it collided with a coin
        return self.check_capsule() if self.grid_pos in self.big_coins else False

    def inputs(self, ev, input):
        if ev.key is input:
            return True

    def can_move(self) -> bool:  # Check if it collided with the points move
        return self.get_objects(self.capsule_mov, self.grid_pos)

    def set_driving_state(self):
        if not self.break_move() or not self.can_move():
            self.move(self.direction_pos[0], self.direction_pos[1])
        else:
            if self.get_direction((vec(1, 0), vec(-1, 0))):
                self.current_x = True
                self.current_y = False
            elif self.get_direction((vec(0, 1), vec(0, -1))):
                self.current_y = True
                self.current_x = False

    def movement(self, ev):  # Check movement inputs
        if ev.type == KEYDOWN:
            if self.inputs(ev, K_a) and self.current_x:
                self.move(vec(-1, 0), 1)
            elif self.inputs(ev, K_d) and self.current_x:
                self.move(vec(1, 0), 0)
            if self.inputs(ev, K_w) and self.current_y:
                self.move(vec(0, -1), 3)
            elif self.inputs(ev, K_s) and self.current_y:
                self.move(vec(0, 1), 2)

            if self.inputs(ev, K_w):
                self.direction_pos = (vec(0, -1), 3)
            elif self.inputs(ev, K_s):
                self.direction_pos = (vec(0, 1), 2)
            if self.inputs(ev, K_a):
                self.direction_pos = (vec(-1, 0), 1)
            elif self.inputs(ev, K_d):
                self.direction_pos = (vec(1, 0), 0)
