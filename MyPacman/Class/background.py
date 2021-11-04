from pygame import sprite, draw, image
from pygame.math import Vector2 as vec

import vars as v


class background(sprite.Sprite):
    def __init__(self, images, wall, screen, grid_pos) -> None:
        sprite.Sprite.__init__(self)

        ###################################
        # /​​absolute background variables\ #
        self.image = image.load(images).convert()

        self.rect = self.image.get_rect()
        self.rect.center = (v.WIDTH / 2, v.HEIGHT / 2)

        self.screen = screen
        self.grid_pos = grid_pos

        self.wall_collision = []
        self.wall_dirc = wall
        # \​​absolute background variables/ #
        ###################################

        self.wall(self.wall_dirc)

    def update(self):
        self.grid(self.screen)
        self.grid_check(self.grid_pos)

    def grid(self, screen):  # General grid
        for x in range(v.WIDTH // v.WIDTH_CELL):
            draw.line(screen, v.GREY,
                      (x * v.WIDTH_CELL, 0),
                      (x * v.WIDTH_CELL, v.HEIGHT))
        for x in range(v.HEIGHT // v.HEIGHT_CELL):
            draw.line(screen, v.GREY,
                      (0, x * v.HEIGHT_CELL),
                      (v.WIDTH, x * v.HEIGHT_CELL))
        for wall in self.wall_collision:
            draw.rect(
                screen, v.PURPLE, (
                    wall.x * v.WIDTH_CELL, wall.y * v.HEIGHT_CELL,
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
                    if char == '1':
                        self.wall_collision.append(vec(xidx, yidx))
        print(len(self.wall_collision))
