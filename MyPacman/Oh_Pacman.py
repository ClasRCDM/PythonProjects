import pygame
import vars as v


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

        # Itens World
        self.Sprites_world = None

    def World_init(self):
        # Set itens world
        self.screen = pygame.display.set_mode((v.FUllSCREEN))
        pygame.display.set_icon(pygame.image.load(v.ICON))

        self.Fps = pygame.time.Clock()

        self.Run = True
        self.running = True

        self.World_objcts()

    def World_objcts(self):
        # Add in World
        self.Sprites_world = pygame.sprite.Group()

        self.World_time()

    def World_widget(self):
        pass

    def World_time(self):
        # Time and Space world
        while self.Run:

            self.World_events()

            self.World_sprits()
            self.World_SpritsDraw()

            self.Fps.tick(v.FPS)

    def World_events(self):
        # Add/Create events
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT and self.Run:
                self.Run, self.running = False

    def World_sprits(self):
        # Set/Update sprits/draw
        self.Sprites_world.update()

    def World_SpritsDraw(self):
        # Add/set draw about sprits
        self.screen.fill(v.BACKGROUND)
        self.Sprites_world.draw(self.screen)

        pygame.display.flip()


MyWorld = World(v.TITLE_GAME)
MyWorld.World_init()
