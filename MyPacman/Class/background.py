from pygame import sprite

import pygame
import vars as v


class background(sprite.Sprite):
    def __init__(self, image, screen) -> None:
        sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert()

        self.rect = self.image.get_rect()
        self.rect.center = (v.WIDTH / 2, v.HEIGHT / 2)

        self.screen = screen

    def update(self):
        self.background_grid(self.screen)

    def background_grid(self, screen):
        for x in range(v.WIDTH // v.WIDTH_CELL):
            pygame.draw.line(screen, v.GREY,
                             (x * v.WIDTH_CELL, 0),
                             (x * v.WIDTH_CELL, v.HEIGHT))
        for x in range(v.HEIGHT // v.HEIGHT_CELL):
            pygame.draw.line(screen, v.GREY,
                             (0, x * v.HEIGHT_CELL),
                             (v.WIDTH, x * v.HEIGHT_CELL))
