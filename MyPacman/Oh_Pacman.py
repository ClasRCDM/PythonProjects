import pygame, os
import vars as v


########################
# Configuring my World #
#######################
class World:  # A Wordl
    def __init__(self, title):
        # Build game
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(title)

        self.screen = None

        self.Fps = None

        self.Run = None
        self.running = None

        self.font = pygame.font.match_font(v.FONT)

        # Itens World
        self.Sprites_world = None

        self.dirctrymges = None
        self.dirctyudo = None

        self.Game_Start = None

    def World_init(self):
        # Set itens world
        self.screen = pygame.display.set_mode((v.FUllSCREEN))
        pygame.display.set_icon(pygame.image.load(v.ICON))

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
        if self.Game_Start:
            self.World_texts('-Pressione uma tecla para jogar', 32,
                             v.YELLOW, v.WIDTH / 2, 320)

    def World_time(self):
        # Time and Space world
        while self.Run:

            self.World_events()

            self.World_sprits()
            self.World_SpritsDraw()

            self.World_widget()

            self.Fps.tick(v.FPS)
            pygame.display.flip()

    def World_events(self):
        # Add/Create events
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT and self.Run:
                self.Run, self.running = False

        # self.World_widget()

    def World_scenes(self):
        # Manage the scenes
        self.Game_Start = v.game_start

    def World_adofle(self):
        # Load files, and audios
        self.dirctrymges = os.path.join(os.getcwd(), 'images')
        self.dirctyudo = os.path.join(os.getcwd(), 'sounds')

        self.pacmanlogo = os.path.join(self.dirctrymges, v.LOGO_PACMAN)

    def World_images(self):
        # Call/add image
        self.pacmanlogo = pygame.image.load(self.pacmanlogo).convert()

    def World_sounds(self):
        # Call/add sound
        pass

    def World_sprits(self):
        # Set/Update sprits/draw
        self.Sprites_world.update()

    def World_texts(self, text: str, size: int, color, x: int, y: int):
        # Create/add/render texts
        font = pygame.font.Font(self.font, size)

        text_render = font.render(text, True, color)
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
print('Init Game')
MyWorld.World_init()
