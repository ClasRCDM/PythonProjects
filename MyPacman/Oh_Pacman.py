import pygame

import vars as v
import Class.texts as t
import Class.sounds as s

from os import path, getcwd
from sys import exit


########################
# Configuring my World #
########################
class World:  # A World l
    def __init__(self, title):
        super().__init__()
        # Build game
        pygame.init()

        pygame.display.set_caption(title)

        self.screen = None
        self.icon = None

        self.Fps = None

        self.Run = None
        self.running = None

        self.font = None

        self.point_mouse = None

        #################
        # \Itens World/ #

        # $ Sprites $ #
        self.Sprites_world = None

        # $ Directories $ #
        self.dirctrymges = None
        self.dirctyudo = None

        # $ Scenes $ #
        self.Game_Start = None
        self.Game = None

        # $ WidGets $ #
        self.widget_world = None

        # $ Images $ #
        self.pacmanlogo = None

        # $ Texts $ #
        self.Start_text = None

    def World_init(self):
        # Set itens world
        self.icon = path.join(getcwd(), v.MAIN_FILE, v.FILES[0], v.ICON)

        self.screen = pygame.display.set_mode((v.FUllSCREEN))
        pygame.display.set_icon(pygame.image.load(self.icon))

        self.Fps = pygame.time.Clock()

        self.Run = True
        self.running = True

        self.World_adofle()

        self.World_text_menu()

        self.World_scenes()

        self.World_objcts()

    def World_objcts(self):
        # Add in World
        self.Sprites_world = pygame.sprite.Group()

        self.World_time()

    def World_widget(self):
        match self.widget_world:
            case 'StartGame':
                self.World_text_menu_update()
                self.World_sounds()

            case 'PlayGame':
                t.text(self.screen, self.font_set,
                       f'FPS: {self.Fps.get_fps():.2f}', 10,
                       v.GREY, v.WIDTH - 60, 10, False)
                self.World_sounds()

    def World_widget_events(self, ev):
        self.World_text_menu_events(ev)

    def World_time(self):
        # Time and Space world
        while self.Run:

            self.point_mouse = pygame.mouse.get_pos()

            self.World_events()
            self.World_functions()

            self.World_sprits()
            self.World_SpritsDraw()

            self.World_images()
            self.World_widget()

            self.Fps.tick(v.FPS)
            pygame.display.flip()

    def World_events(self):
        # Add/Create events
        for ev in pygame.event.get():
            # Exit to game
            if ev.type == pygame.QUIT and self.Run:
                self.Run, self.running = False

                exit()

            # Init game
            if ev.type == pygame.KEYUP:
                self.Game, self.Game_Start = True, False

                v.MUSICS = 'PlayGame_music'
                v.FPS = 60

            self.World_widget_events(ev)

    def World_functions(self):
        if self.Game_Start and not self.Game:
            self.widget_world = 'StartGame'
        elif self.Game and not self.Game_Start:
            self.widget_world = 'PlayGame'

    def World_scenes(self):
        # Manage the scenes
        self.Game_Start = v.game_start

        self.Game = v.game

    def World_adofle(self):
        # Load files, and audios
        self.dirctrymges = path.join(getcwd(), v.MAIN_FILE, v.FILES[0])
        self.dirctyudo = path.join(getcwd(), v.MAIN_FILE, v.FILES[1])
        self.dirctyfnts = path.join(getcwd(), v.MAIN_FILE, v.FILES[2])

        self.font_set = path.join(self.dirctyfnts, v.FONT)

    def World_images(self):
        # Call/add image
        pacmanlogo = path.join(self.dirctrymges, v.LOGO_PACMAN)
        self.pacmanlogo = pygame.image.load(pacmanlogo).convert_alpha()

        match self.widget_world:
            case 'StartGame':
                self.screen.blit(self.pacmanlogo, (6, 0))

    def World_sounds(self):
        # Call/add sound
        match v.MUSICS:
            case 'StartGame_music':
                start_dirc = path.join(self.dirctyudo, v.music_START)
                s.sound(start_dirc, 0.1, True)

                v.MUSICS = ''

            case 'PlayGame_music':
                play = path.join(self.dirctyudo, v.music_PLAY)
                s.sound(play, play=True)
                pygame.mixer.fadeout(500)

                v.MUSICS = 'Background_music'

            case 'Background_music':
                background_music_dirc = path.join(
                    self.dirctyudo, v.music_BACKGROUND)

                s.sound(background_music_dirc, 0.5, play=True, loop=True)

                v.MUSICS = ''

    def World_sprits(self):
        # Set/Update sprits/draw
        self.Sprites_world.update()

    def World_text_menu(self):
        # Load/render texts
        self.Start_text = t.text(self.screen, self.font_set, v.text_START, 15, v.YELLOW,
                                 v.WIDTH / 2, 320, True)  # Press a key to play

    def World_text_menu_events(self, ev):
        self.Start_text.point(pygame.mouse.get_pos(), ev)

    def World_text_menu_update(self):
        # Update texts
        self.Start_text.animation(True, '-zoon', 'Touched')
        self.Start_text.draw()

        '''t.text(self.screen, self.font_set, '-Desenvolvido por',
               12, v.WHITE, v.WIDTH / 2 - 65, 520, True)
        t.text(self.screen, self.font_set, 'ClasRCDM-',
               12, v.WHITE, v.WIDTH / 2 + 105, 520, True)  # Developed by ClasRCDM

        t.text(self.screen, self.font_set, '-Projeto inspirado por',
               11, v.GREY, v.WIDTH / 2 - 75, 550, True)
        t.text(self.screen, self.font_set, 'João Tinti-',
               11, v.GREY, v.WIDTH / 2 + 115, 550, True)  # Project inspired by João Tinti'''

    def World_SpritsDraw(self):
        # Add/set draw about sprits
        self.screen.fill(v.BACKGROUND)
        self.Sprites_world.draw(self.screen)


###################
#  Init my World  #
###################

MyWorld = World(v.TITLE_GAME)
MyWorld.World_init()
