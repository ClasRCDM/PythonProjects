from pygame import font


class text:  # Texts
    def __init__(self, screen, directory: str,
                 txt: str, size: int, color,
                 x: int = 0, y: int = 0,
                 pixel: bool = False):

        # Create/Add texts
        font.init()

        self.size: int = size

        self.txt: str = txt
        self.pixel: bool = pixel
        self.color = color

        self.x: int = x
        self.y: int = y

        self.directory: str = directory

        # # To create ##
        text_font = font.Font(self.directory, self.size)

        text_render = text_font.render(self.txt, self.pixel, self.color)
        text_rect = text_render.get_rect()
        text_rect.midtop = (self.x, self.y)

        screen.blit(text_render, text_rect)

        '''if text_rect.collidepoint(self.point_mouse):
            hover = True
        else:
            hover = False

        match animation:
            case 'zipper':
                if pos_anim == 'up':
                    size_anim += anim_val
                    if font.get_height() >= 16:
                        pos_anim = 'down'
                if pos_anim == 'down':
                    size_anim -= anim_val
                    if font.get_height() <= size:
                        pos_anim = 'up'
            case 'hover':
                if hover:
                    size_anim += anim_val
                    if font.get_height() >= 15:
                        pos_anim = 'down'
                if not hover:
                    size_anim -= anim_val
                    if font.get_height() <= size:
                        pos_anim = 'up'''
