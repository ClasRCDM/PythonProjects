from pygame import sprite
import pygame


class player_pacman(sprite.Sprite):
    def __init__(self, image) -> None:
        sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        pass
