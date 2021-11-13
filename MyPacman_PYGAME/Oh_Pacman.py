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
        self.screen = pygame.display.set_mode((v.FUllSCREEN))
        self.icon = path.join(getcwd(), v.MAIN_FILE, v.FILES[0], v.ICON)

        self.Fps = None

        self.Run = self.running = None

        self.cell_width = self.cell_height = None
        # &#########################& #

        #################
        # \Itens World/ #

        self.Itens_world: dict = {}

        # $ Sprites $ #
        # $ Directories $ #
        self.Directory_world: dict = {}
        # $ Scenes $ #
        # $$ Player $$ #
        self.Entities_world: dict = {}
        # $ WidGets $ #
        self.Itens_world['Scenes'] = 'StartGame'
        # $ Images $ #
        self.Images_world: dict = {}
        # $ Texts $ #
        self.Text_world: dict = {}

        # \Itens World/ #
        #################

    def World_init(self):
        # &###############################& #
        # /absolute variables of the world\ #
        pygame.display.set_icon(pygame.image.load(self.icon))

        self.Fps = pygame.time.Clock()

        self.Run = self.running = True

        self.Itens_world['directory'] = {}

        self.cell_width: int = v.MAZE_WIDTH // v.COLS
        self.cell_height: int = v.MAZE_HEIGHT // v.ROWS
        # \absolute variables of the world/ #
        # &###############################& #
        # /absolute world classes\ #
        self.World_adofle()

        self.World_scenes()

        self.Scene_global()
        self.World_objcts()
        # \absolute world classes/ #
        # &######################& #

    def World_objcts(self):
        # Add in World
        self.Itens_world[
            'Sprites_world'] = self.Itens_world[
                'Background_world'] = pygame.sprite.Group()

        self.World_time()

    def Scene_global(self):
        match self.Itens_world['Scenes']:
            case 'StartGame':
                ###############################
                # /absolute commands in Menu\ #
                # $(Images)$ #
                self.World_image_LOGO()

                # $(Texts)$ #
                # $$(Footer)$$ #
                self.Itens_world['text_footer'] = \
                    ts.footer(self.screen,
                              self.Directory_world['font_set'])
                self.Text_world['DevClasRCDM'] = \
                    self.Itens_world['text_footer'].dev()
                self.Text_world['InsJoãoTinti'] = \
                    self.Itens_world['text_footer'].forj()

                # $$(Start Menu)$$ #
                self.Itens_world['text_startmenu'] = \
                    ts.start_menu(self.screen,
                                  self.Directory_world['font_set'])
                self.Text_world['StartMenu'] = \
                    self.Itens_world['text_startmenu'].start()
                # $(Texts)$ ##
                # \absolute commands in Menu/ #
                ###############################

            case 'PlayGame':
                ###############################
                # /absolute commands in Game\ #
                # $(Background/Map)$ #
                self.Itens_world['Background'] = b.background(
                    self.Directory_world['diry_bck_img'],
                    self.Directory_world['diry_bck_txt'],
                    self.screen, self.cell_width, self.cell_height)

                self.Entities_world['Pacman'] = \
                    p.pacman(
                        self.Directory_world['sprite_pacman'],
                        self.Itens_world['Background'].wall_collision,
                        self.Itens_world['Background'].coins,
                        self.Itens_world['Background'].big_coins,
                        self.cell_width, self.cell_height,
                        self.Directory_world['diry_bck_txt'])

                self.Entities_world['Enemies'] = e.spawn_enemies(
                    self.Directory_world['diry_bck_txt'],
                    self.Itens_world['Background'].wall_collision,
                    self.cell_width, self.cell_height)

                # $(Add in world)$ #
                self.Itens_world['Background_world'].add(
                    self.Itens_world['Background'])
                self.Itens_world['Background_world'].add(
                    self.Entities_world['Pacman'])
                self.Itens_world['Background_world'].add(
                    self.Entities_world['Enemies'].group())
                # \absolute commands in Game/ #
                ###############################

    def Scene_global_update(self):
        match self.Itens_world['Scenes']:
            case 'StartGame':
                ###############################
                # /absolute commands in Menu\ #
                # $(Sounds)$ #
                self.World_sounds()

                # $(Texts)$ #
                # $$(Footer)$$ #
                self.Itens_world['text_footer'].update(
                    self.Text_world['DevClasRCDM'],
                    self.Text_world['InsJoãoTinti'])
                # $$(Start Menu)$$ #
                self.Itens_world['text_startmenu'].update(
                    self.Text_world['StartMenu'])

                v.FPS = 7
                # \absolute commands in Menu/ #
                ###############################

            case 'PlayGame':
                ###############################
                # /absolute commands in Game\ #
                # $(Texts)$ #
                t.text(self.screen, self.Directory_world['font_set'],
                       f'FPS: {self.Fps.get_fps():.2f}', 10,
                       v.GREY, v.WIDTH - 60, 10, False)
                self.World_sounds()

                v.FPS = 120

                # \absolute commands in Game/ #
                ###############################

    def World_time(self):
        # Time and Space world
        while 1:

            ################################
            # /absolute defs of the world\ #
            self.World_events()
            self.World_functions()

            self.World_SpritsDraw()
            self.World_sprits_update()

            self.World_images_update()

            self.Scene_global_update()
            # \absolute defs of the world/ #
            ################################
            # /absolute defs of the game\ #
            # self.World_pacman()
            # \absolute defs of the game/ #
            ###############################

            self.Itens_world['Background_world'].update()

            pygame.display.flip()
            pygame.display.update()
            self.Fps.tick(v.FPS)

            if not self.Run:
                break

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

                    self.Itens_world['text_startmenu'].events(
                        ev,
                        self.Text_world['StartMenu'])

                    if ev.type == pygame.KEYUP:
                        if ev.key == pygame.K_SPACE:
                            self.Itens_world['Game'] = True
                            self.Itens_world['Game_Start'] = False
                            self.Itens_world['Scenes'] = 'PlayGame'

                            self.Text_world = self.Images_world = {}

                            del self.Itens_world['text_footer']
                            del self.Itens_world['text_startmenu']

                            self.Scene_global()

                            v.MUSICS = 'PlayGame_music'

                case 'PlayGame':
                    self.Entities_world['Pacman'].movement(ev)

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

        self.Directory_world['font_set'] = path.join(
            self.Itens_world['dirctyfnts'], v.FONT)

        self.Directory_world['diry_bck_img'] = path.join(
            self.Itens_world['dirctrymges'], v.MAZE_BACKGROUND)
        self.Directory_world['diry_bck_txt'] = path.join(
            self.Itens_world['dirctrymges'], v.WALL_BACKGROUND)

        self.Directory_world['sprite_pacman'] = path.join(
            self.Itens_world['dirctrymges'], v.SPRITE_PACMAN)

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

if __name__ == '__main__':
    MyWorld = World(v.TITLE_GAME)
    MyWorld.World_init()