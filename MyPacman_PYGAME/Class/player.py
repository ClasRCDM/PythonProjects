from pygame import sprite
from pygame.math import Vector2 as vec
from pygame import KEYDOWN,\
    K_LEFT, K_a, K_RIGHT, K_d, K_UP, K_w, K_DOWN, K_s
from pygame import image as img, transform as tfm

import vars as v


class pacman(sprite.Sprite):
    def __init__(self, image: str,
                 walls: list, coins: list, big_coins: list,
                 cell_width: int | float, cell_height: int | float,
                 file_wall: str) -> None:

        sprite.Sprite.__init__(self)

        #################################
        # /player's absolute variables\ #
        self.image = img.load(image).convert_alpha()
        self.image = tfm.scale(self.image, (16, 16))

        self.rect = self.image.get_rect()
        self.togle_to_move = True

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
        self.current_score, self.speed, self.lives = 0, 2, 1

        self.direction: list[str] = ['right', 'None']
        self.direction_y_current: int = 90
        self.direction_y: list[int] = [90, -90, 180, -180]
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

    def movement(self, ev):  # Check movement inputs
        if ev.type == KEYDOWN:
            if ev.key == K_LEFT or ev.key == K_a:
                self.move(vec(-1, 0), self.direction)
            if ev.key == K_RIGHT or ev.key == K_d:
                self.move(vec(1, 0), self.direction)
            if ev.key == K_UP or ev.key == K_w:
                self.move(vec(0, -1), self.direction)
            if ev.key == K_DOWN or ev.key == K_s:
                self.move(vec(0, 1), self.direction)

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

    def move(self, direction_mov, direction):  # move! k
        self.stored_direction: vec = direction_mov
        print(f'Antes[{self.direction_y_current}]')

        if direction_mov == vec(-1, 0) and direction[0] != 'left':
            self.image = tfm.flip(self.image, True, False)

            if self.direction_y_current == 180 and direction[1] == 'up':
                self.image = tfm.rotate(self.image, self.direction_y[0])
                self.direction_y_current = 90
            elif self.direction_y_current == -180 and direction[1] == 'up':
                self.image = tfm.rotate(self.image, self.direction_y[0])
                self.direction_y_current = 90
            elif self.direction_y_current == 90 and direction[1] == 'up':
                self.image = tfm.rotate(self.image, self.direction_y[0])
                self.direction_y_current = 90
            if self.direction_y_current == 180 and direction[1] == 'down':
                self.image = tfm.rotate(self.image, self.direction_y[1])
                self.direction_y_current = -90
            elif self.direction_y_current == 90:
                self.direction_y_current = -90

            direction[1] = 'None'
            self.direction[0] = 'left'
        elif direction_mov == vec(1, 0) and direction[0] != 'right':
            self.image = tfm.flip(self.image, True, False)

            if self.direction_y_current == 180 and direction[1] == 'up':
                self.image = tfm.rotate(self.image, self.direction_y[1])
                self.direction_y_current = -90
            elif self.direction_y_current == -180 and direction[1] == 'up':
                self.image = tfm.rotate(self.image, self.direction_y[1])
                self.direction_y_current = -90
            elif self.direction_y_current == 90 and direction[1] == 'up':
                self.image = tfm.rotate(self.image, self.direction_y[1])
                self.direction_y_current = -90
            if self.direction_y_current == 180 and direction[1] == 'down':
                self.image = tfm.rotate(self.image, self.direction_y[0])
                self.direction_y_current = 90
            elif self.direction_y_current == 90:
                self.direction_y_current = -90

            direction[1] = 'None'
            self.direction[0] = 'right'

        if direction_mov == vec(0, -1) and direction[1] != 'up':
            if self.direction[0] == 'right' and self.direction_y_current == 90:
                self.image = tfm.rotate(self.image, self.direction_y[0])
                self.direction_y_current = 180
            elif self.direction[0] == 'right' and self.direction_y_current == 180:
                self.image = tfm.rotate(self.image, self.direction_y[2])
                self.direction_y_current = 180
            elif self.direction[0] == 'right' and self.direction_y_current == -90:
                self.image = tfm.rotate(self.image, self.direction_y[0])
                self.direction_y_current = 90

            if self.direction[0] == 'left' and self.direction_y_current == -90:
                self.image = tfm.rotate(self.image, self.direction_y[1])
                self.direction_y_current = -180
            elif self.direction[0] == 'left' and self.direction_y_current == -180:
                self.image = tfm.rotate(self.image, self.direction_y[3])
                self.direction_y_current = -180
            elif self.direction[0] == 'left' and self.direction_y_current == 90:
                self.image = tfm.rotate(self.image, self.direction_y[1])
                self.direction_y_current = -90

            self.direction[0] = 'None'
            self.direction[1] = 'up'

        elif direction_mov == vec(0, 1) and direction[1] != 'down':
            if self.direction[0] == 'right' and self.direction_y_current == 90:
                self.image = tfm.rotate(self.image, self.direction_y[1])
                self.direction_y_current = 180
            elif self.direction[0] == 'right' and self.direction_y_current == 180:
                self.image = tfm.rotate(self.image, self.direction_y[3])
                self.direction_y_current = 180

            if self.direction[0] == 'left' and self.direction_y_current == -90:
                self.image = tfm.rotate(self.image, self.direction_y[0])
                self.direction_y_current = -180
            elif self.direction[0] == 'left' and self.direction_y_current == -180:
                self.image = tfm.rotate(self.image, self.direction_y[2])
                self.direction_y_current = -180

            self.direction[0] = 'None'
            self.direction[1] = 'down'

        print(f'Depois[{self.direction_y_current}]')

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
