####################
# Game mode classes#
####################

from arcade import SpriteList
from arcade import Sprite

Size_1000550 = [1000 / 2, 550 / 2]


class Dino(SpriteList):
    def __init__(self):
        super(Dino, self).__init__()
        """ Defines input variables """
        self.Dino_Sprite = Sprite('PastSprites_Imagens/Dino_Menu.png',
                                  center_x=Size_1000550[0], center_y=Size_1000550[1], hit_box_algorithm='Simple')

        self.append(self.Dino_Sprite)

        self.p_x: float = self.Dino_Sprite.position[0]
        self.p_y: float = self.Dino_Sprite.position[1]

        self.Progscale: float = 0.98

        self.Start_Position: float = 58.33
        self.pos_start: tuple = (int(-650), int(-240))

        self.Dino_Animation = 'walk'
        self.Dino_Animation_value = 0

        self.Dou_jump: str = 'None'
        self.jump: int = 800

        self.game: bool = False
        self.GameOver: bool = False

    def scale_game(self, delta_time):
        # I change the position
        if self.p_x >= self.Start_Position:
            self.move(self.pos_start[0] * delta_time, self.pos_start[1] * delta_time)
            self.rescale(self.Progscale)
        else:
            self.game = True

    def reposition_dino(self, delta_time):
        if self.GameOver:
            self.move(0, -(self.jump - 250) * delta_time)
            if self.p_y <= 125.80: self.GameOver = False

    def jump_dino(self, delta_time):
        # Jump
        if self.Dou_jump == 'jump':
            self.move(0, self.jump * delta_time)
            if self.p_y >= 365.53: self.Dou_jump = 'down'
        elif self.Dou_jump == 'down':
            self.move(0, -(self.jump - 250) * delta_time)
            if self.p_y <= 125.80: self.Dou_jump = 'None'

    def player_animation(self):
        pass

    def on_update(self, delta_time: float = 1 / 60):
        """ Inputs """
        # Says the player's location on the screen
        self.p_x: float = self.Dino_Sprite.position[0]
        self.p_y: float = self.Dino_Sprite.position[1]

    def update_animation(self, delta_time: float = 1 / 75):
        self.on_update()

        self.scale_game(delta_time)
        self.reposition_dino(delta_time)
        self.jump_dino(delta_time)
