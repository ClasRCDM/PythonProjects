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

        ###############
        # Itens World #

        # # Sprites ##
        self.Sprites_world = None

        # # Directories ##
        self.dirctrymges = None
        self.dirctyudo = None

        # # Scenes ##
        self.Game_Start = None
        self.Game = None

        # # WidGets ##
        self.widget_world = None

        # # Images ##
        self.pacmanlogo = None

        # # Texts ##
        self.pos_anim = None

    def World_init(self):
        # Set itens world
        self.icon = path.join(getcwd(), v.MAIN_FILE, v.FILES[0], v.ICON)

        self.screen = pygame.display.set_mode((v.FUllSCREEN))
        pygame.display.set_icon(pygame.image.load(self.icon))

        self.Fps = pygame.time.Clock()

        self.Run = True
        self.running = True

        self.pos_anim = 'up'

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
                self.World_texts_animated('-Pressione uma tecla para jogar',
                                          13, 'zipper', 0.65,
                                          v.YELLOW, v.WIDTH / 2, 320)
                self.World_texts('-Desenvolvido por Clas.RCDM-', 14,
                                 v.WHITE, v.WIDTH / 2, 520)
                self.World_texts('-Projeto inspirado por João Tinti-', 10,
                                 v.GREY, v.WIDTH / 2, 550)

            case 'PlayGame':
                self.World_texts(f'FPS: {self.Fps.get_fps():.2f}', 10,
                                 v.GREY, v.WIDTH - 60, 10)

    def World_time(self):
        # Time and Space world
        while self.Run:

            self.World_events()
            self.World_functions()

            self.World_sprits()
            self.World_SpritsDraw()

            self.World_images()
            self.World_widget()

            self.World_sounds()

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

                start = pygame.mixer.Sound(start_dirc)

                start.fadeout(500)
                start.play()
                start.set_volume(0.1)

                v.MUSICS = ''

            case 'PlayGame_music':
                play = path.join(self.dirctyudo, v.music_PLAY)

                pygame.mixer.music.load(play)
                pygame.mixer.fadeout(500)
                pygame.mixer.music.play()

                v.MUSICS = 'Background_music'

            case 'Background_music':
                background_music_dirc = path.join(self.dirctyudo, v.music_BACKGROUND)

                background_music = pygame.mixer.Sound(background_music_dirc)

                background_music.play()
                background_music.set_volume(0.2)

                v.MUSICS = ''

    def World_sprits(self):
        # Set/Update sprits/draw
        self.Sprites_world.update()

    def World_texts(self,
                    text: str,
                    size: int,
                    color,
                    x: int,
                    y: int):

        # Create/add/render texts
        font = pygame.font.Font(self.font_set, size)

        text_render = font.render(text, False, color)
        text_rect = text_render.get_rect()
        text_rect.midtop = (x, y)

        self.screen.blit(text_render, text_rect)

    def World_texts_animated(self,
                             text: str,
                             size: int,
                             animation: str,
                             anim_val: float,
                             color,
                             x: int,
                             y: int):

        # Create/add/render animated texts
        v.size_anim += size if v.size_anim == 0 else 0

        font = pygame.font.Font(self.font_set, int(v.size_anim))
        font.set_underline(True)

        text_render = font.render(text, False, color)
        text_rect = text_render.get_rect()
        text_rect.midtop = (x, y)

        match animation:
            case 'zipper':
                if self.pos_anim == 'up':
                    v.size_anim += anim_val
                    if font.get_height() >= 16:
                        self.pos_anim = 'down'
                if self.pos_anim == 'down':
                    v.size_anim -= anim_val
                    if font.get_height() <= size:
                        self.pos_anim = 'up'

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
