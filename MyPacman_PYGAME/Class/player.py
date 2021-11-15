from pygame import Surface, sprite, event
from pygame.math import Vector2 as vec
from pygame import KEYDOWN, K_a, K_d, K_w, K_s
from pygame import image as img

import vars as v


class pacman(sprite.Sprite):
    def __init__(self, image: str, walls: list,
                 coins: list, big_coins: list,
                 cell_width: int, cell_height: int,
                 file_wall: str) -> None:

        sprite.Sprite.__init__(self)
        event.set_allowed([KEYDOWN, K_a, K_d, K_w, K_s])

        #################################
        # /player's absolute variables\ #
        self.pacman = img.load(image)

        self.image = img.load(image)
        self.set_sprite(0)

        self.rect = self.image.get_rect()
        self.togle_to_move: bool = True

        # $ Movement cell size $ #
        self.cell_width, self.cell_height = cell_width, cell_height

        # $ Location/ Start and End$ #
        self.grid_pos: vec = self.get_location(file_wall)
        self.pix_pos: vec = self.get_pix_pos()

        self.direction_mov: vec = vec(0, 0)
        self.direction_pos = None

        # $ Get location walls and coins $ #
        self.walls, self.coins, self.big_coins = walls, coins, big_coins

        # $ Wall variables $ #
        self.stored_direction, self.able_to_move = None, True
        self.capsule_mov = list[int]()
        self.capsule_mov = self.get_capsule_move(file_wall)

        # $ Lives, velocity and Points $ #
        self.speed, self.lives = 2, 1
        # \player's absolute variables/ #
        #################################

        # self.get_capsule_move(file_wall)

    def update(self):
        if self.able_to_move:  # Add movement player
            self.pix_pos += self.direction_mov * self.speed

        self.set_driving_state()  # Say you can go forward or backward

        if self.check_capsule():  # Check if you can move
            if self.stored_direction is not None:
                self.direction_mov = self.stored_direction
            self.able_to_move = self.break_move()

        # Setting grid position in reference to pix pos
        self.grid_pos[0] = (self.pix_pos[0] - v.TOP_BOTTOM_BUFFER +
                            self.cell_width // 2) // self.cell_width + 1
        self.grid_pos[1] = (self.pix_pos[1] - v.TOP_BOTTOM_BUFFER +
                            self.cell_height // 2) // self.cell_height + 1

        if self.on_coin():  # Eat coins
            self.eat_coin(self.coins)
        elif self.on_big_coin():  # Eat big coins
            self.eat_big_coin(self.big_coins)

        # Set position global player
        self.rect[0] = self.pix_pos.x - int(v.TOP_BOTTOM_BUFFER / 5.5)
        self.rect[1] = self.pix_pos.y - int(v.TOP_BOTTOM_BUFFER / 6)

    def get_location(self, file):  # Set loocation player
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in 'P':
                        return vec(xidx, yidx)

    def get_capsule_move(self, file):  # Set loocation player
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char in 'D':
                        self.capsule_mov.append(vec(xidx, yidx))
        return self.capsule_mov

    def get_sprite(self, frame: int):
        surface = Surface(
            (v.WIDHT_PACMAN, v.HEIGHT_PACMAN)).convert_alpha()
        surface.blit(self.pacman,
                     (0, 0),
                     ((frame * v.WIDHT_PACMAN), 0,
                      v.WIDHT_PACMAN, v.HEIGHT_PACMAN))
        surface.set_colorkey(v.BLACK)
        return surface

    def set_sprite(self, direction):
        self.image = self.get_sprite(direction)

    def eat_coin(self, coins):  # Check and eat the coins
        coins.remove(self.grid_pos)

    def eat_big_coin(self, big_coins):  # Check and eat the big coins
        big_coins.remove(self.grid_pos)

    def on_coin(self) -> bool:  # Check if it collided with a coin
        # if self.grid_pos in self.coins:
        return self.check_capsule() if self.grid_pos in self.coins else False

    def on_big_coin(self) -> bool:  # Check if it collided with a coin
        return self.check_capsule() if self.grid_pos in self.big_coins else False

    def move(self, direction_mov, sprite):  # move! k
        self.stored_direction: vec = direction_mov
        self.set_sprite(sprite)

    def inputs(self, ev, input):
        if ev.key is input:
            return True

    def break_move(self) -> bool:  # Check if it collided with the wall
        return self.get_objects(self.walls, vec(self.grid_pos + self.direction_mov))

    def can_move(self) -> bool:  # Check if it collided with the wall
        return self.get_objects(self.capsule_mov, self.grid_pos)

    def get_objects(self, object, another_object):
        for item in object:
            if another_object == item:
                return False
        return True

    def check_capsule(self):
        return self.get_capsule(self.pix_pos.x, self.cell_width, (vec(1, 0), vec(-1, 0))) or \
            self.get_capsule(self.pix_pos.y, self.cell_height, (vec(0, 1), vec(0, -1)))

    def get_capsule(self, direction, cell_size, mov):
        if int(direction + v.TOP_BOTTOM_BUFFER // 2) % cell_size == 0:
            return self.get_direction(mov)

    def get_direction(self, mov):
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
