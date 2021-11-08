# & /Imports World\ & #
import pygame
import vars as v  # Variables

import Class.texts as ts  # Set Texts
import Class.text as t  # Create Text
import Class.sounds as s  # Add sound

import Class.player as p  # Add player
import Class.background as b  # Add background
import Class.enemies as e  # Spawn Enemies

from os import path, getcwd  # Get files
from sys import exit  # QUIT system
# & \Imports World/ & #


########################
# Configuring my World #
########################
class World:  # A World l
    def __init__(self, title):
        super().__init__()
        # Build game
        pygame.init()
        pygame.display.set_caption(title)

        # &#########################& #
        self.screen = None
        self.icon = None

        self.Fps = None

        self.Run = None
        self.running = None

        self.point_mouse = None
        # &#########################& #

        #################
        # \Itens World/ #

        self.Itens_world = {}

        # $ Sprites $ #
        # $ Directories $ #
        # $ Scenes $ #
        # $$ Player $$ #
        self.Entities_world = {}
        # $ WidGets $ #
        self.Itens_world['Scenes'] = 'StartGame'
        # $ Images $ #
        self.Images_world = {}
        # $ Texts $ #
        self.Text_world = {}

        # \Itens World/ #
        #################

    def World_init(self):
        # &###############################& #
        # /absolute variables of the world\ #
        self.icon = path.join(getcwd(), v.MAIN_FILE, v.FILES[0], v.ICON)

        self.screen = pygame.display.set_mode((v.FUllSCREEN))
        pygame.display.set_icon(pygame.image.load(self.icon))

        self.Fps = pygame.time.Clock()

        self.Run = True
        self.running = True
        # \absolute variables of the world/ #
        # &###############################& #
        # /absolute world classes\ #
        self.World_adofle()

        self.World_scenes()

        self.World_widget()
        self.World_objcts()
        # \absolute world classes/ #
        # &######################& #

    def World_objcts(self):
        # Add in World
        self.Itens_world['Sprites_world'] = pygame.sprite.Group()
        self.Itens_world['Background_world'] = pygame.sprite.Group()

        self.World_time()

    def World_widget(self):
        match self.Itens_world['Scenes']:
            case 'StartGame':
                self.World_image_LOGO()
                self.Itens_world['text_footer'] = \
                    ts.footer(self.screen, self.font_set)
                self.Text_world['DevClasRCDM'] = \
                    self.Itens_world['text_footer'].text_dev()
                self.Text_world['InsJoãoTinti'] = \
                    self.Itens_world['text_footer'].text_for()

            case 'PlayGame':
                pass

    def World_widget_update(self):
        match self.Itens_world['Scenes']:
            case 'StartGame':
                self.World_sounds()
                self.Itens_world['text_footer'].update(
                    self.Text_world['DevClasRCDM'],
                    self.Text_world['InsJoãoTinti'])

                v.FPS = 7

            case 'PlayGame':
                t.text(self.screen, self.font_set,
                       f'FPS: {self.Fps.get_fps():.2f}', 10,
                       v.GREY, v.WIDTH - 60, 10, False)
                self.World_sounds()

                v.FPS = 120

    def World_widget_events(self, ev):
        if self.Itens_world['Game_Start'] and not self.Itens_world['Game']:
            pass

    def World_time(self):
        # Time and Space world
        while self.Run:

            self.point_mouse = pygame.mouse.get_pos()

            #####################################
            # /absolute defs of the world\ #
            self.World_events()
            self.World_functions()

            self.World_SpritsDraw()
            self.World_sprits_update()

            self.World_images_update()
            self.World_widget_update()
            # \absolute variables of the world/ #
            #####################################
            # /absolute defs of the game\ #
            # self.World_pacman()
            # \absolute defs of the game/ #
            #####################################

            self.Itens_world['Background_world'].update()

            pygame.display.flip()
            pygame.display.update()
            self.Fps.tick(v.FPS)

    def World_events(self):
        # Add/Create events
        for ev in pygame.event.get():
            # Exit to game
            if ev.type == pygame.QUIT and self.Run:
                self.Run, self.running = False

                exit()

            # Init game
            match self.Itens_world['Scenes']:
                case 'StartGame':
                    self.Itens_world['text_footer'].events(
                        ev,
                        self.Text_world['DevClasRCDM'],
                        self.Text_world['InsJoãoTinti'])

                    if ev.type == pygame.KEYUP:
                        self.Itens_world['Game'] = True
                        self.Itens_world['Game_Start'] = False
                        self.Itens_world['Scenes'] = 'PlayGame'

                        self.Text_world = {}
                        self.Images_world = {}

                        self.World_widget()

                        v.MUSICS = 'PlayGame_music'

                case 'PlayGame':
                    pass

    def World_functions(self):
        if self.Itens_world['Game_Start'] and not self.Itens_world['Game']:
            self.Itens_world['Scenes'] = 'StartGame'
        elif self.Itens_world['Game'] and not self.Itens_world['Game_Start']:
            self.Itens_world['Scenes'] = 'PlayGame'

    def World_scenes(self):
        # Manage the scenes
        self.Itens_world['Game_Start'] = v.game_start
        self.Itens_world['Game'] = v.game

    def World_adofle(self):
        # Load files, and audios
        self.Itens_world['dirctrymges'] = path.join(
            getcwd(), v.MAIN_FILE, v.FILES[0])
        self.Itens_world['dirctyudo'] = path.join(
            getcwd(), v.MAIN_FILE, v.FILES[1])
        self.Itens_world['dirctyfnts'] = path.join(
            getcwd(), v.MAIN_FILE, v.FILES[2])

        self.font_set = path.join(self.Itens_world['dirctyfnts'], v.FONT)
        self.Itens_world['directory_background'] = path.join(
            self.Itens_world['dirctrymges'], v.MAZE_BACKGROUND)

    def World_images_update(self):
        # Call/add image
        match self.Itens_world['Scenes']:
            case 'StartGame':
                self.screen.blit(
                    self.Images_world['pacmanlogo'],
                    (self.Images_world['pacmanlogo_rect']))

    def World_image_LOGO(self):
        pacmanlogo = path.join(
            self.Itens_world['dirctrymges'], v.LOGO_PACMAN)
        self.Images_world['pacmanlogo'] = pygame.image.load(
            pacmanlogo).convert_alpha()
        self.Images_world['pacmanlogo_rect'] =\
            self.Images_world['pacmanlogo'].get_rect()
        self.Images_world['pacmanlogo_rect'].center =\
            (v.WIDTH / 2, v.HEIGHT / 4)

    def World_sounds(self):
        # Call/add sound
        match v.MUSICS:
            case 'StartGame_music':
                start_dirc = path.join(
                    self.Itens_world['dirctyudo'], v.music_START)
                s.sound(start_dirc, 0.1, True)

                v.MUSICS = ''

            case 'PlayGame_music':
                play = path.join(self.Itens_world['dirctyudo'], v.music_PLAY)
                s.sound(play, play=True)
                pygame.mixer.fadeout(500)

                v.MUSICS = 'Background_music'

            case 'Background_music':
                background_music_dirc = path.join(
                    self.Itens_world['dirctyudo'], v.music_BACKGROUND)

                s.sound(background_music_dirc, 0.5, play=True, loop=True)

                v.MUSICS = ''

    def World_sprits_update(self):
        # Set/Update sprits/draw
        self.Itens_world['Sprites_world'].update()

    def World_SpritsDraw(self):
        # Add/set draw about sprits
        self.screen.fill(v.BACKGROUND)
        self.Itens_world['Sprites_world'].draw(self.screen)
        self.Itens_world['Background_world'].draw(self.screen)


###################
#  Init my World  #
###################

MyWorld = World(v.TITLE_GAME)
MyWorld.World_init()
