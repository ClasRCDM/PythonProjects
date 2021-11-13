from pygame import Surface, sprite
from pygame.math import Vector2 as vec
from pygame import KEYDOWN,\
    K_LEFT, K_a, K_RIGHT, K_d, K_UP, K_w, K_DOWN, K_s
from pygame import image as img

import vars as v


class pacman(sprite.Sprite):
    def __init__(self, image: str,
                 walls: list, coins: list, big_coins: list,
                 cell_width: int | float, cell_height: int | float,
                 file_wall: str) -> None:

        sprite.Sprite.__init__(self)

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

        self.direction_mov: vec = vec(1, 0)

        # $ Get location walls and coins $ #
        self.walls, self.coins, self.big_coins = walls, coins, big_coins

        # $ Wall variables $ #
        self.stored_direction, self.able_to_move = None, True

        # $ Lives, velocity and Points $ #
        self.current_score, self.speed, self.lives = 0, 1, 1
        # \player's absolute variables/ #
        #################################

    def update(self):
        if self.able_to_move:  # Add movement player
            self.pix_pos += self.direction_mov * self.speed

        if self.time_to_move():  # Check if you can move
            if self.stored_direction is not None:
                self.direction_mov = self.stored_direction
            self.able_to_move = self.can_move()

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
                    if char == 'P':
                        return vec(xidx, yidx)
            print(set(enumerate(file)) & set(enumerate(file)))

    def get_sprite(self, frame: int):
        surface = Surface(
            (v.WIDHT_PACMAN, v.HEIGHT_PACMAN)).convert_alpha()
        surface.blit(self.pacman,
                     (0, 0),
                     ((frame * v.WIDHT_PACMAN), 0,
                      v.WIDHT_PACMAN, v.HEIGHT_PACMAN))
        surface.set_colorkey((0, 0, 0))
        return surface

    def set_sprite(self, direction):
        self.image = self.get_sprite(direction)

    def movement(self, ev):  # Check movement inputs
        if ev.type == KEYDOWN:
            if ev.key == K_LEFT or ev.key == K_a:
                self.move(vec(-1, 0))
                self.set_sprite(1)
            if ev.key == K_RIGHT or ev.key == K_d:
                self.move(vec(1, 0))
                self.set_sprite(0)
            if ev.key == K_UP or ev.key == K_w:
                self.move(vec(0, -1))
                self.set_sprite(3)
            if ev.key == K_DOWN or ev.key == K_s:
                self.move(vec(0, 1))
                self.set_sprite(2)

    def eat_coin(self, coins):  # Check and eat the coins
        coins.remove(self.grid_pos)

    def eat_big_coin(self, big_coins):  # Check and eat the big coins
        big_coins.remove(self.grid_pos)

    def on_coin(self) -> bool:  # Check if it collided with a coin
        if self.grid_pos in self.coins:
            if int(self.pix_pos.x + v.TOP_BOTTOM_BUFFER // 2) %\
                    self.cell_width == 0:
                if self.direction_mov == vec(1, 0) \
                        or self.direction_mov == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + v.TOP_BOTTOM_BUFFER // 2) %\
                    self.cell_height == 0:
                if self.direction_mov == vec(0, 1) \
                        or self.direction_mov == vec(0, -1):
                    return True
        return False

    def on_big_coin(self) -> bool:  # Check if it collided with a coin
        if self.grid_pos in self.big_coins:
            if int(self.pix_pos.x + v.TOP_BOTTOM_BUFFER // 2) %\
                    self.cell_width == 0:
                if self.direction_mov == vec(1, 0) \
                        or self.direction_mov == vec(-1, 0):
                    return True
            if int(self.pix_pos.y + v.TOP_BOTTOM_BUFFER // 2) %\
                    self.cell_height == 0:
                if self.direction_mov == vec(0, 1) \
                        or self.direction_mov == vec(0, -1):
                    return True
        return False

    def move(self, direction_mov):  # move! k
        self.stored_direction: vec = direction_mov

    def can_move(self) -> bool:  # Check if it collided with the wall
        for wall in self.walls:
            if vec(self.grid_pos + self.direction_mov) == wall:
                return False
        return True

    def time_to_move(self) -> bool:  # Check if it is able to move
        if int(self.pix_pos.x + v.TOP_BOTTOM_BUFFER // 2) %\
                self.cell_width == 0:
            if self.direction_mov == vec(1, 0) or\
                    self.direction_mov == vec(-1, 0) or\
                    self.direction_mov == vec(0, 0):
                return True
        if int(self.pix_pos.y + v.TOP_BOTTOM_BUFFER // 2) %\
                self.cell_height == 0:
            if self.direction_mov == vec(0, 1) or\
                    self.direction_mov == vec(0, -1) or\
                    self.direction_mov == vec(0, 0):
                return True

    def get_pix_pos(self) -> vec:  # Get and add player position
        return vec((self.grid_pos[0] * self.cell_width)
                   + v.TOP_BOTTOM_BUFFER // 2
                   + self.cell_width // 2,
                   (self.grid_pos[1] * self.cell_height)
                   + v.TOP_BOTTOM_BUFFER // 2
                   + self.cell_height // 2)
