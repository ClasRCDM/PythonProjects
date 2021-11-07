from pygame import sprite, image, draw, mask
from pygame.math import Vector2 as vec

import vars as v


class background(sprite.Sprite):
    def __init__(self, images, wall, screen, grid_pos) -> None:
        sprite.Sprite.__init__(self)

        ###################################
        # /​​absolute background variables\ #
        self.image = image.load(images).convert_alpha()

        self.mask = mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = (v.WIDTH / 2, v.HEIGHT / 2)

        self.screen = screen
        self.grid_pos: vec = grid_pos

        self.wall_collision: list = []
        self.wall_visibility: bool = False
        self.wall_dirc: str = wall

        self.coins: list = []
        self.coins_visibility: bool = False
        # \​​absolute background variables/ #
        ###################################

        self.wall(self.wall_dirc)

    def update(self):  # Update elements
        self.grid(self.screen)
        self.grid_check(self.grid_pos)
        self.draw_coins(self.screen)

    def grid(self, screen):  # General grid
        for x in range(v.WIDTH // v.WIDTH_CELL):
            draw.line(screen, v.GREY,
                      (x * v.WIDTH_CELL, 0),
                      (x * v.WIDTH_CELL, v.HEIGHT))
        for x in range(v.HEIGHT // v.HEIGHT_CELL):
            draw.line(screen, v.GREY,
                      (0, x * v.HEIGHT_CELL),
                      (v.WIDTH, x * v.HEIGHT_CELL))

        if self.wall_visibility:
            for wall in self.wall_collision:  # Draw the walls
                draw.rect(
                    screen, v.PURPLE, (
                        wall.x * v.WIDTH_CELL, wall.y * v.HEIGHT_CELL,
                        v.WIDTH_CELL, v.HEIGHT_CELL))
        if self.coins_visibility:
            for coins in self.coins:  # Draw the coins
                draw.rect(
                    screen, v.BLUE, (
                        coins.x * v.WIDTH_CELL, coins.y * v.HEIGHT_CELL,
                        v.WIDTH_CELL, v.HEIGHT_CELL))

    def grid_check(self, grid_pos):  # Grid where is the player
        draw.rect(self.screen, v.RED,
                  (grid_pos[0] * v.WIDTH_CELL,
                   grid_pos[1] * v.HEIGHT_CELL,
                   v.WIDTH_CELL, v.HEIGHT_CELL), 1)

    def wall(self, file):
        with open(file, mode='r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == '1':  # Create the walls
                        self.wall_collision.append(vec(xidx, yidx))
                    elif char == 'C':  # creates the spawn path for the coins
                        self.coins.append(vec(xidx, yidx))

    def draw_coins(self, screen):  # Create the coins
        for coin in self.coins:
            draw.circle(screen, v.YELLOW,
                        (int(coin.x * v.WIDTH_CELL) + v.WIDTH_CELL // 2,
                         int(coin.y * v.HEIGHT_CELL) + v.HEIGHT_CELL // 2), 5)

    def on_coin(self, pix_pos, direction) -> bool:  # Create the coins on the grid
        if self.grid_pos in self.coins:
            if (pix_pos.x + 40 // 2) % v.WIDTH_CELL == 1:
                if direction == vec(1, 0) or direction == vec(-1, 0):
                    return True
            if (pix_pos.y + 40 // 2) % v.HEIGHT_CELL == 1:
                if direction == vec(0, 1) or direction == vec(0, -1):
                    return True
        return False
