from pygame import sprite, image, draw
from pygame.math import Vector2 as vec

import vars as v


class background(sprite.Sprite):
    def __init__(self, images: str,
                 wall_dirc: str, screen,
                 cell_width: int, cell_height: int) -> None:

        sprite.Sprite.__init__(self)

        ###################################
        # /​​absolute background variables\ #
        self.image = image.load(images).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = (v.WIDTH / 2, v.HEIGHT / 2)

        self.screen = screen

        self.cell_height, self.cell_width = cell_height, cell_width

        self.wall_collision: list[int] = []
        self.wall_dirc: str = wall_dirc

        self.coins: list[int] = []
        self.big_coins: list[int] = []
        # \​​absolute background variables/ #
        ###################################

        self.wall(self.wall_dirc)

    def update(self):  # Update elements
        self.grid()
        self.draw_coins(self.screen)

    def grid(self):  # General grid
        for x in range(v.WIDTH // self.cell_width):
            draw.line(self.image, v.GREY,
                      (x * self.cell_width, 0),
                      (x * self.cell_width, v.HEIGHT))
        for x in range(v.HEIGHT // self.cell_height):
            draw.line(self.image, v.GREY,
                      (0, x * self.cell_height),
                      (v.WIDTH, x * self.cell_height))

    def wall(self, file):
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == '1':  # Create the walls
                        self.wall_collision.append(vec(xidx, yidx))
                    elif char in ['c', 'D']:  # creates the spawn path for the coins
                        self.coins.append(vec(xidx, yidx))
                    elif char == 'C':  # creates the spawn path for the big coins
                        self.big_coins.append(vec(xidx, yidx))

    def draw_coins(self, screen):  # Create the coins
        for coin in self.coins:
            self.coin(screen, 2, coin)
        for coin in self.big_coins:
            self.coin(screen, 4, coin)

    def coin(self, screen, size, coin):
        draw.circle(screen, v.YELLOW_DARK,
                    (int(coin.x * self.cell_width)
                     + self.cell_width // 2
                     + v.TOP_BOTTOM_BUFFER // 2,
                     int(coin.y * self.cell_height)
                     + self.cell_height // 2
                     + v.TOP_BOTTOM_BUFFER // 2), size)
