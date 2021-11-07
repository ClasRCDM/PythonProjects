import pygame
import vars as v

import Class.texts as t
import Class.sounds as s

import Class.player as p
import Class.background as b
import Class.enemies as e

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
        # $$ Player $$ #
        self.Entities_world = {}
        # $ WidGets $ #
        self.Itens_world['widget_world'] = 'StartGame'
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

        self.World_text_menu()
        self.World_footer()

        self.World_scenes()

        self.World_widget()
        self.World_objcts()
        # \absolute world classes/ #
        # &######################& #

    def World_objcts(self):
        # Add in World
        self.Itens_world['Sprites_world'] = pygame.sprite.Group()

        self.World_time()

    def World_widget(self):
        match self.Itens_world['widget_world']:
            case 'StartGame':
                self.World_image_LOGO()

            case 'PlayGame':
                pass

    def World_widget_update(self):
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
            self.World_footer_events(ev)

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
            self.World_pacman_update()
            # \absolute defs of the game/ #
            #####################################

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
            match self.Itens_world['widget_world']:
                case 'StartGame':
                    if ev.type == pygame.KEYUP:
                        self.Itens_world['Game'] = True
                        self.Itens_world['Game_Start'] = False
                        self.Itens_world['widget_world'] = 'PlayGame'

                        self.Text_world = {}
                        self.Images_world = {}

                        self.World_widget()
                        self.World_pacman()

                        v.MUSICS = 'PlayGame_music'

                case 'PlayGame':
                    self.Entities_world['Pacman'].pacman_movement(ev)

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
        self.Itens_world['directory_background'] = path.join(
            self.Itens_world['dirctrymges'], v.MAZE_BACKGROUND)

    def World_images_update(self):
        # Call/add image
        match self.Itens_world['widget_world']:
            case 'StartGame':
                self.screen.blit(
                    self.Images_world['pacmanlogo'],
                    (self.Images_world['pacmanlogo_rect']))
            case 'PlayGame':
                pass

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

    def World_footer(self):
        # Load/Render footer menu
        self.Text_world['DevClasRCDM'] = t.text(
            self.screen, self.font_set, v.text_DEV,
            12, v.WHITE, v.WIDTH / 2 + 105, 520, True)  # by ClasRCDM

        self.Text_world['InsJoãoTinti'] = t.text(
            self.screen, self.font_set, v.text_FOR,
            11, v.GREY, v.WIDTH / 2 + 115, 550, True)  # by João Tinti

    def World_footer_events(self, ev):
        self.Text_world['DevClasRCDM'].point(pygame.mouse.get_pos(), ev)
        self.Text_world['InsJoãoTinti'].point(pygame.mouse.get_pos(), ev)

    def World_footer_update(self):
        # Update footer menu
        t.text(self.screen, self.font_set, '-Desenvolvido por',
               12, v.WHITE, v.WIDTH / 2 - 65, 520, True)  # Developed
        self.Text_world['DevClasRCDM'].animation(
            True, 1, 1, '+backforth', 'repeat', 'Touched')
        self.Text_world['DevClasRCDM'].draw()
        self.Text_world['DevClasRCDM'].link('https://github.com/ClasRCDM')

        t.text(self.screen, self.font_set, '-Projeto inspirado por',
               11, v.GREY, v.WIDTH / 2 - 75, 550, True)  # Project inspired
        self.Text_world['InsJoãoTinti'].animation(
            True, 1, 1, '-backforth', 'repeat', 'Touched')
        self.Text_world['InsJoãoTinti'].draw()
        self.Text_world['InsJoãoTinti'].link('https://github.com/joaotinti75')

    def World_text_menu(self):
        # Load/render text menu
        self.Text_world['Start_text'] = t.text(
            self.screen, self.font_set, v.text_START, 15,
            v.YELLOW, v.WIDTH / 2, 320, True)  # Press a key to play

    def World_text_menu_events(self, ev):
        # Check events menu
        self.Text_world['Start_text'].point(pygame.mouse.get_pos(), ev)

    def World_text_menu_update(self):
        # Update text menu
        self.Text_world['Start_text'].animation(
            True, 1, 2, '-zoon', 'one_click', 'Touched')
        self.Text_world['Start_text'].draw()

    def World_pacman(self):
        match self.Itens_world['widget_world']:
            case 'PlayGame':
                pacman_sprite = path.join(
                    self.Itens_world['dirctrymges'],
                    v.SPRITE_PACMAN['PACMAN_RUN'])

                wall = path.join(
                    self.Itens_world['dirctrymges'], v.WALL_BACKGROUND)

                # Create the entities of the world
                self.Entities_world['Pacman'] = p.player_pacman(
                    pacman_sprite)

                self.Entities_world['Background'] = b.background(
                    self.Itens_world['directory_background'], wall,
                    self.screen,
                    self.Entities_world['Pacman'].grid_pos)

                self.Entities_world['Enemies'] = e.spawn_enemies(
                    wall, self.Entities_world['Background'].wall_collision)

                # Add to group sprites world
                self.Itens_world['Sprites_world'].add(
                    self.Entities_world['Background'])
                self.Itens_world['Sprites_world'].add(
                    self.Entities_world['Pacman'])
                self.Itens_world['Sprites_world'].add(
                    self.Entities_world['Enemies'].group())

    def World_pacman_update(self):
        match self.Itens_world['widget_world']:
            case 'PlayGame':
                self.Entities_world['Pacman'].move_update(
                    self.Entities_world['Background'].wall_collision)

                self.Entities_world['Pacman'].eat_coin(
                    self.Entities_world['Background'].on_coin(
                        self.Entities_world['Pacman'].pix_pos,
                        self.Entities_world['Pacman'].direction),
                    self.Entities_world['Background'].coins)

    def World_SpritsDraw(self):
        # Add/set draw about sprits
        self.screen.fill(v.BACKGROUND)
        self.Itens_world['Sprites_world'].draw(self.screen)


###################
#  Init my World  #
###################

MyWorld = World(v.TITLE_GAME)
MyWorld.World_init()
