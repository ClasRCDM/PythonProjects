import pygame
import vars as v

from os import path, getcwd
from sys import exit


########################
# Configuring my World #
#######################
class World:  # A Wordl
    def __init__(self, title):
        # Build game
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption(title)

        self.screen = None
        self.icon = None

        self.Fps = None

        self.Run = None
        self.running = None

        self.font = None

        # Itens World
        self.Sprites_world = None

        self.dirctrymges = None
        self.dirctyudo = None

        self.Game_Start = None
        self.Game = None

        self.widget_world = None

    def World_init(self):
        # Set itens world
        self.icon = path.join(getcwd(), v.MAIN_FILE, v.FILES[0], v.ICON)

        self.screen = pygame.display.set_mode((v.FUllSCREEN))
        pygame.display.set_icon(pygame.image.load(self.icon))

        self.Fps = pygame.time.Clock()

        self.Run = True
        self.running = True

        self.World_scenes()
        self.World_adofle()
        self.World_objcts()

    def World_objcts(self):
        # Add in World
        self.Sprites_world = pygame.sprite.Group()

        self.World_time()

    def World_widget(self):
        match self.widget_world:
            case 'StartGame':
                self.World_texts('-Pressione uma tecla para jogar', 14,
                                 v.YELLOW, v.WIDTH / 2, 320)

    def World_time(self):
        # Time and Space world
        while self.Run:

            self.World_events()

            self.World_sprits()
            self.World_SpritsDraw()

            self.World_functions()
            self.World_widget()
            self.World_images()

            self.Fps.tick(v.FPS)
            pygame.display.flip()

    def World_events(self):
        # Add/Create events
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT and self.Run:
                self.Run, self.running = False
                exit()
            if ev.type == pygame.KEYUP:
                self.Game = True
                self.Game_Start = False

    def World_functions(self):
        if self.Game_Start and not self.Game:
            self.widget_world = 'StartGame'

    def World_scenes(self):
        # Manage the scenes
        self.Game_Start = v.game_start

        self.Game = v.game

    def World_adofle(self):
        # Load files, and audios
        self.dirctrymges = path.join(getcwd(), v.MAIN_FILE, v.FILES[0])
        self.dirctyudo = path.join(getcwd(), v.MAIN_FILE, v.FILES[1])
        self.dirctyfnts = path.join(getcwd(), v.MAIN_FILE, v.FILES[2])
        print(self.dirctrymges)

        self.font_set = path.join(self.dirctyfnts, v.FONT)

    def World_images(self):
        # Call/add image
        match self.widget_world:
            case 'StartGame':
                pacmanlogo = path.join(self.dirctrymges, v.LOGO_PACMAN)
                pacmanlogo = pygame.image.load(pacmanlogo).convert_alpha()
                self.screen.blit(pacmanlogo, (6, 0))

    def World_sounds(self):
        # Call/add sound
        pass

    def World_sprits(self):
        # Set/Update sprits/draw
        self.Sprites_world.update()

    def World_texts(self, text: str, size: int, color, x: int, y: int):
        # Create/add/render texts
        font = pygame.font.Font(self.font_set, size)

        text_render = font.render(text, False, color)
        text_rect = text_render.get_rect()
        text_rect.midtop = (x, y)

        self.screen.blit(text_render, text_rect)

    def World_SpritsDraw(self):
        # Add/set draw about sprits
        self.screen.fill(v.BACKGROUND)
        self.Sprites_world.draw(self.screen)


###################
#  Init my World  #
###################

MyWorld = World(v.TITLE_GAME)
MyWorld.World_init()
