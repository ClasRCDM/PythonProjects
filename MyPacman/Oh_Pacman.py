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
        # $ WidGets $ #
        # $ Images $ #
        # $ Texts $ #
        self.Itens_text = {}

        # \Itens World/ #
        #################

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
        self.World_footer()

        self.World_scenes()

        self.World_objcts()

    def World_objcts(self):
        # Add in World
        self.Itens_world['Sprites_world'] = pygame.sprite.Group()

        self.World_time()

    def World_widget(self):
        match self.Itens_world['widget_world']:
            case 'StartGame':
                self.World_text_menu_update()
                self.World_footer_update()
                self.World_sounds()

                v.FPS = 7

            case 'PlayGame':
                t.text(self.screen, self.font_set,
                       f'FPS: {self.Fps.get_fps():.2f}', 10,
                       v.GREY, v.WIDTH - 60, 10, False)
                self.World_sounds()

                v.FPS = 60

    def World_widget_events(self, ev):
        if self.Itens_world['Game_Start'] and not self.Itens_world['Game']:
            self.World_text_menu_events(ev)

    def World_time(self):
        # Time and Space world
        while self.Run:

            self.point_mouse = pygame.mouse.get_pos()

            #####################################
            # /absolute defs of the world\ #
            self.World_events()
            self.World_functions()

            self.World_sprits()
            self.World_SpritsDraw()

            self.World_images()
            self.World_widget()
            # \absolute variables of the world/ #
            #####################################
            # /absolute defs of the game\ #
            self.World_pacman()
            # \absolute defs of the game/ #
            #####################################

            pygame.display.flip()
            self.Fps.tick(v.FPS)

    def World_events(self):
        # Add/Create events
        for ev in pygame.event.get():
            # Exit to game
            if ev.type == pygame.QUIT and self.Run:
                self.Run, self.running = False

                exit()

            # Init game
            if ev.type == pygame.KEYUP:
                self.Itens_world['Game'] = True
                self.Itens_world['Game_Start'] = False

                self.Itens_text = {}

                v.MUSICS = 'PlayGame_music'

            self.World_widget_events(ev)

    def World_functions(self):
        if self.Itens_world['Game_Start'] and not self.Itens_world['Game']:
            self.Itens_world['widget_world'] = 'StartGame'
        elif self.Itens_world['Game'] and not self.Itens_world['Game_Start']:
            self.Itens_world['widget_world'] = 'PlayGame'

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

    def World_images(self):
        # Call/add image
        match self.Itens_world['widget_world']:
            case 'StartGame':
                pacmanlogo = path.join(
                    self.Itens_world['dirctrymges'], v.LOGO_PACMAN)
                Inpacmanlogo = pygame.image.load(
                    pacmanlogo).convert_alpha()

                Inpacmanlogo_rect = Inpacmanlogo.get_rect()
                Inpacmanlogo_rect.center = (v.WIDTH / 2, v.HEIGHT / 4)

                self.screen.blit(Inpacmanlogo, (Inpacmanlogo_rect))
            case 'PlayGame':
                background_maze = path.join(
                    self.Itens_world['dirctrymges'], v.MAZE_BACKGROUND)
                Inbackground_maze = pygame.image.load(
                    background_maze).convert()

                Inbackground_maze_rect = \
                    Inbackground_maze.get_rect()
                Inbackground_maze_rect.center = (v.WIDTH / 2, v.HEIGHT / 2)

                self.screen.blit(
                    Inbackground_maze,
                    (Inbackground_maze_rect))

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

    def World_sprits(self):
        # Set/Update sprits/draw
        self.Itens_world['Sprites_world'].update()

    def World_footer(self):
        # Load/Render footer menu
        self.Itens_text['DevClasRCDM'] = t.text(
            self.screen, self.font_set, 'ClasRCDM-',
            12, v.WHITE, v.WIDTH / 2 + 105, 520, True)  # by ClasRCDM

        self.Itens_text['InsJoãoTinti'] = t.text(
            self.screen, self.font_set, 'João Tinti-',
            11, v.GREY, v.WIDTH / 2 + 115, 550, True)  # by João Tinti

    def World_footer_update(self):
        # Update footer menu
        t.text(self.screen, self.font_set, '-Desenvolvido por',
               12, v.WHITE, v.WIDTH / 2 - 65, 520, True)  # Developed
        self.Itens_text['DevClasRCDM'].animation(
            True, 1, 1, '+backforth', 'repeat', 'Touched')
        self.Itens_text['DevClasRCDM'].draw()

        t.text(self.screen, self.font_set, '-Projeto inspirado por',
               11, v.GREY, v.WIDTH / 2 - 75, 550, True)  # Project inspired
        self.Itens_text['InsJoãoTinti'].animation(
            True, 1, 1, '-backforth', 'repeat', 'Touched')
        self.Itens_text['InsJoãoTinti'].draw()

    def World_text_menu(self):
        # Load/render text menu
        self.Itens_text['Start_text'] = t.text(
            self.screen, self.font_set, v.text_START, 15,
            v.YELLOW, v.WIDTH / 2, 320, True)  # Press a key to play

    def World_text_menu_events(self, ev):
        # Check events menu
        self.Itens_text['Start_text'].point(pygame.mouse.get_pos(), ev)

    def World_text_menu_update(self):
        # Update text menu
        self.Itens_text['Start_text'].animation(
            True, 1, 2, '-zoon', 'one_click', 'Touched')
        self.Itens_text['Start_text'].draw()

    def World_pacman(self):
        match self.Itens_world['widget_world']:
            case 'PlayGame':
                self.World_pacman_grid()

    def World_pacman_grid(self):
        for x in range(v.WIDTH // v.WIDTH_CELL):
            pygame.draw.line(self.screen, v.GREY,
                             (x * v.WIDTH_CELL, 0),
                             (x * v.WIDTH_CELL, v.HEIGHT))
        for x in range(v.HEIGHT // v.HEIGHT_CELL):
            pygame.draw.line(self.screen, v.GREY,
                             (0, x * v.HEIGHT_CELL),
                             (v.WIDTH, x * v.HEIGHT_CELL))

    def World_SpritsDraw(self):
        # Add/set draw about sprits
        self.screen.fill(v.BACKGROUND)
        self.Itens_world['Sprites_world'].draw(self.screen)


###################
#  Init my World  #
###################

MyWorld = World(v.TITLE_GAME)
MyWorld.World_init()
