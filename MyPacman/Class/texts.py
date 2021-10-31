from pygame import font, MOUSEBUTTONUP, MOUSEBUTTONDOWN


class text:  # Texts
    def __init__(self, screen, directory: str,
                 txt: str, size: int, color,
                 x: int = 0, y: int = 0,
                 pixel: bool = False):

        # Create/Add texts
        font.init()

        self.size: int = size
        self.size_normal: int = size

        self.txt: str = txt
        self.pixel: bool = pixel
        self.color = color

        self.x: int = x
        self.y: int = y

        self.screen = screen
        self.directory: str = directory

        # $ Animation $ #
        self.animation_if: bool = False

        self.animation_type: str = 'None'
        self.animation_style: str = 'None'
    
        self.animation_constant: str = 'None'

        # $ Mouse Point $ #
        self.mouse_input: bool = False
        self.mouse_action_h: str = 'None'
        self.mouse_action_t: str = 'None'

        # $ To create $ #
        text_font = font.Font(self.directory, self.size)
        text_render = text_font.render(self.txt, self.pixel, self.color)

        self.text_font = None
        self.text_render = None

        self.text_rect = text_render.get_rect()
        self.text_rect.midtop = (self.x, self.y)

        if not self.animation_if:
            self.screen.blit(text_render, self.text_rect)

    def animation(self,
                  animation: bool = True, value_move: int = 1,
                  type_animation: str = 'None', constant: str = 'repeat',
                  type: str = 'None'):  # Animation texts

        self.animation_if = animation
        self.animation_constant = constant

        anim_val = value_move

        if type == 'Hover':
            self.mouse_input = True if self.mouse_action_h == type else False
        elif type == 'Touched':
            self.mouse_input = True if self.mouse_action_t == type else False

        if self.animation_if:
            match type_animation:
                case '+zoon':
                    self.size += anim_val

                case '-zoon':
                    if self.animation_constant == 'repeat' and self.mouse_input:
                        self.size -= anim_val
                    elif self.animation_constant == 'one_click' and self.mouse_input:
                        self.size = -anim_val

                    if self.size <= (self.size_normal - 3) and self.animation_constant == 'one_click' and self.mouse_input:
                        self.size = (self.size_normal - 3)
                    elif self.size <= (self.size_normal - 3) and not self.mouse_input:
                        self.size = self.size_normal

    def point(self, point_mouse, ev):  # Check mouse points
        if self.text_rect.collidepoint(point_mouse):
            self.mouse_action_h = 'Hover'
        else: self.mouse_action_h = 'None'

        if ev.type == MOUSEBUTTONUP:
            self.mouse_action_t = 'None'
        if ev.type == MOUSEBUTTONDOWN:
            if self.text_rect.collidepoint(point_mouse):
                self.mouse_action_t = 'Touched'

    def draw(self):
        text_font = font.Font(self.directory, self.size)
        text_render = text_font.render(self.txt, self.pixel, self.color)

        self.text_rect = text_render.get_rect()
        self.text_rect.midtop = (self.x, self.y)

        self.screen.blit(text_render, self.text_rect)
