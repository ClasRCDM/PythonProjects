import pygame

pygame.init()

WINDOW_SIZE = (640, 700)
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('O cubo')
window_getsize = surface.get_rect()

FPS = pygame.time.Clock()


class World:
    def __init__(self):
        super(World, self).__init__()

        self.background = None

        self.FPS = None

    def world(self):
        self.background = surface.fill((255, 255, 255))

        self.FPS = pygame.time.Clock()

    def world_events(self):
        # Eventos gerais
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Click
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                Cubo.check_touched()
            # Pos Click
            elif ev.type == pygame.MOUSEBUTTONUP:
                Cubo.touched = False

    def world_body(self):
        pygame.display.flip()
        self.FPS.tick(75)


class Cubo:
    def __init__(self):
        super(Cubo, self).__init__()

        self.cubo_w = None
        self.cubo_h = None

        self.cubo = None
        self.cubo_pos_inside = None

        self.touched = None

        self.point_mouse = None

    def init_cubo(self):
        self.cubo_w: int = 100
        self.cubo_h: int = 100

        self.cubo = pygame.Rect((0, 0), (self.cubo_w, self.cubo_h))
        self.cubo.center = (window_getsize.w / 2, window_getsize.h / 2)

        self.touched: bool = False

    def check_touched(self):
        if self.cubo.collidepoint(ev.pos):
            self.touched = True
            pygame.mouse.get_rel()

    def move_touched(self):
        if self.touched:
            self.cubo.move_ip(pygame.mouse.get_rel())
            self.cubo.clamp_ip(window_getsize)
            surface.fill((100, 0, 0), self.cubo)
        else:
            surface.fill((0, 0, 100), self.cubo)

    def get_pos_cubo(self):
        self.point_mouse = pygame.mouse.get_pos()
        self.cubo_pos_inside = self.point_mouse[0] - self.cubo.x, self.point_mouse[1] - self.cubo.y

    def gravity(self):
        if not self.touched and not self.cubo.y >= (WINDOW_SIZE[1] - self.cubo_h):
            self.cubo.move_ip((0, 15))
            self.cubo.clamp_ip(window_getsize)


# Cubo
Cubo = Cubo()

# Inputs
touched = False

# Text
MYFONT = pygame.font.SysFont('Arial', 12)

Cubo.init_cubo()
while True:
    # Cores
    surface.fill((255, 255, 255))

    # Eventos gerais
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Click
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            Cubo.check_touched()
        # Pos Click
        elif ev.type == pygame.MOUSEBUTTONUP:
            Cubo.touched = False

    # Cubo
    Cubo.move_touched()
    Cubo.gravity()

    Position_cubo = MYFONT.render(f'X:{Cubo.cubo.x} Y:{Cubo.cubo.y}', 1, (0, 0, 0))
    surface.blit(Position_cubo, (WINDOW_SIZE[0] - (WINDOW_SIZE[0] - 10), WINDOW_SIZE[1] - (WINDOW_SIZE[1] - 10)))
    Text_FPS = MYFONT.render(f'FPS: {FPS.get_fps():.2f}', 1, (0, 0, 0))
    surface.blit(Text_FPS, (WINDOW_SIZE[0] - 70, WINDOW_SIZE[1] - (WINDOW_SIZE[1] - 10)))

    pygame.display.flip()
    FPS.tick(75)
