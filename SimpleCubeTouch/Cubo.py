import pygame

pygame.init()

surface = pygame.display.set_mode((640, 740))
pygame.display.set_caption('O cubo')
window_size = surface.get_rect()

FPS = pygame.time.Clock()


class Cubo:
    def __init__(self):
        super(Cubo, self).__init__()

        self.cubo_w = None
        self.cubo_h = None

        self.cubo = None

        self.touched = None

    def init_cubo(self):
        self.cubo_w = 100
        self.cubo_h = 100

        self.cubo = pygame.Rect((0, 0), (self.cubo_w, self.cubo_h))
        self.cubo.center = (window_size.w / 2, window_size.h / 2)

        self.touched = False

    def check_touched(self):
        if self.cubo.collidepoint(ev.pos):
            self.touched = True
            pygame.mouse.get_rel()

    def move_touched(self):
        if self.touched:
            self.cubo.move_ip(pygame.mouse.get_rel())
            self.cubo.clamp_ip(window_size)
            surface.fill((100, 0, 0), self.cubo)

    def gravity(self):
        if not self.touched:
            self.cubo.move_ip((0, 15))
            self.cubo.clamp_ip(window_size)


# Cubo
Cubo = Cubo()

# Inputs
touched = False

# Text
MYFONT = pygame.font.SysFont('Arial', 12)
text = None

Cubo.init_cubo()
while True:
    # Cores
    surface.fill((255, 255, 255))

    # Eventos gerais
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
        # Click
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            Cubo.check_touched()
        # Pos Click
        elif ev.type == pygame.MOUSEBUTTONUP:
            Cubo.touched = False

    # Cubo
    surface.fill((0, 0, 100), Cubo.cubo)
    Cubo.move_touched()
    Cubo.gravity()

    text = MYFONT.render(f'X:{Cubo.cubo.x} Y:{Cubo.cubo.y}', 1, (0, 0, 0))
    surface.blit(text, (10, 10))

    pygame.display.flip()
    FPS.tick(75)
