from pygame import sprite
from pygame import image as img, transform as tfm

import vars as v


class enemy(sprite.Sprite):
    def __init__(self, image, x, y) -> None:
        sprite.Sprite.__init__(self)

        #################################
        # /player's absolute variables\ #
        self.image = img.load(image).convert_alpha()
        self.image = tfm.scale(self.image, (17, 17))

        self.rect = self.image.get_rect()

        self.rect[0] = x
        self.rect[1] = y
        # \player's absolute variables/ #
        #################################
