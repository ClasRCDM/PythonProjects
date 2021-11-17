from os import path, getcwd

import Class.enemy as e
import vars as v


class spawn_enemies:
    def __init__(self, screen,
                 wall_dirc: str, walls: list,
                 cell_height: int, cell_width: int):
        self.screen = screen
        self.wall_dirc: str = wall_dirc
        self.walls: list = walls

        self.cell_height, self.cell_width = cell_height, cell_width

        directory = path.join(getcwd(), v.MAIN_FILE, v.FILES[0])
        self.sprite_enemy0 = path.join(directory, v.SPRITE_ENEMIES[0])
        self.sprite_enemy1 = path.join(directory, v.SPRITE_ENEMIES[1])
        self.sprite_enemy2 = path.join(directory, v.SPRITE_ENEMIES[2])
        self.sprite_enemy3 = path.join(directory, v.SPRITE_ENEMIES[3])

    def set_enemies(self):
        return list([e.Blinky(self.sprite_enemy0, self.walls,
                    self.cell_height, self.cell_width,
                    self.wall_dirc, self.screen),
                    e.Inky(self.sprite_enemy1, self.walls,
                    self.cell_height, self.cell_width,
                    self.wall_dirc, self.screen),
                    e.Pinky(self.sprite_enemy2, self.walls,
                    self.cell_height, self.cell_width,
                    self.wall_dirc),
                    e.Clyde(self.sprite_enemy3, self.walls,
                    self.cell_height, self.cell_width,
                    self.wall_dirc)])

    def group(self):
        return self.set_enemies()
