from pygame import font, MOUSEBUTTONUP, MOUSEBUTTONDOWN
from webbrowser import open_new_tab


class text:  # Texts
    def __init__(self, screen, directory: str,
                 txt: str, size: int, color,
                 x: int = 0, y: int = 0,
                 pixel: bool = False):

        # Create/Add texts
        font.init()

        # &#########################& #
        self.size, self.size_normal = size, size

        self.txt: str = txt
        self.pixel: bool = pixel
        self.color = color

        self.x, self.y = x, y

        self.screen = screen
        self.directory: str = directory

        # &#########################& #

        #################
        # /Itens Texts\ #

        self.Itens_texts = {}

        # $ Animation $ #
        self.Itens_texts['FPS'] = 60
        # $ Mouse Point $ #
        self.mouse_action_t: str = 'None'
        self.Itens_texts['state'] = 'None'
        # $ To create $ #

        # \Itens Texts/ #
        #################

        self.render()

    def render(self):
        # $ To create $ #
        text_font = font.Font(self.directory, self.size)
        text_render = text_font.render(self.txt, self.pixel, self.color)

        self.Itens_texts['text_rect'] = text_render.get_rect()
        self.Itens_texts['text_rect'].midtop = (self.x, self.y)

        self.screen.blit(text_render, self.Itens_texts['text_rect'])

    def animation(self,
                  animation: bool = True, value_move: int = 1, limit: int = 3,
                  type_animation: str = 'None', constant: str = 'repeat',
                  type: str = 'None', fps: int = 60):
        # I add values ​​for animation and check if it will animate
        self.Itens_texts['animation_if'] = animation
        self.Itens_texts['animation_constant'] = constant
        self.Itens_texts['limit'] = limit
        self.Itens_texts['FPS'] = fps

        anim_val = value_move

        self.action(type)

        if self.Itens_texts['animation_if']:
            self.type_animation(type_animation, anim_val)

    def type_animation(self, type_animation, anim_val):
        match type_animation:  # Select the animation and make it
            case '+zoon':
                if self.chack_animation_zoon('repeat'):
                    self.size += anim_val
                elif self.chack_animation_zoon('one_click'):
                    self.size = anim_val

                if self.size <= (self.size_normal + self.Itens_texts['limit'])\
                        and self.Itens_texts['animation_constant'] ==\
                        'one_click' and self.mouse_input:
                    self.size = (self.size_normal + self.Itens_texts['limit'])

                elif self.size >= (self.size_normal + self.Itens_texts['limit'])\
                        and not self.mouse_input:
                    self.size = self.size_normal

            case '-zoon':
                if self.chack_animation_zoon('repeat'):
                    self.size -= anim_val
                elif self.chack_animation_zoon('one_click'):
                    self.size = -anim_val

                if self.size <= (self.size_normal - self.Itens_texts['limit'])\
                        and self.Itens_texts['animation_constant'] ==\
                        'one_click' and self.mouse_input:
                    self.size = (self.size_normal - self.Itens_texts['limit'])

                elif self.size <=\
                        (self.size_normal - self.Itens_texts['limit'])\
                        and not self.mouse_input:
                    self.size = self.size_normal

            case '-backforth':
                self.animation_backforth('down', 'repeat', anim_val,)

                if self.size <= (self.size_normal - self.Itens_texts['limit']):
                    # self.size = self.size_normal
                    self.Itens_texts['state'] = 'up'
                if self.size >= self.size_normal:
                    # self.size = self.size_normal
                    self.Itens_texts['state'] = 'down'

            case '+backforth':
                self.animation_backforth('up', 'repeat', anim_val,)

                if self.size >= (self.size_normal + self.Itens_texts['limit']):
                    # self.size = self.size_normal
                    self.Itens_texts['state'] = 'down'
                if self.size <= self.size_normal:
                    # self.size = self.size_normal
                    self.Itens_texts['state'] = 'up'

    def animation_backforth(self, state, type, value):
        self.Itens_texts['state'] == state
        if self.chack_animation_backforth(type, 'down'):
            self.size -= value
        if self.chack_animation_backforth(type, 'up'):
            self.size += value

    def chack_animation_backforth(self, type, move):
        if self.Itens_texts['animation_constant'] == type and\
                self.Itens_texts['state'] == move:
            return True

    def chack_animation_zoon(self, type):
        if self.Itens_texts['animation_constant'] ==\
                type and self.mouse_input:
            return True

    def point(self, point_mouse, ev):  # Check mouse points
        self.Itens_texts['mouse_action_h'] = \
            'Hover' if self.Itens_texts['text_rect'].collidepoint(
                point_mouse) else 'None'

        if ev.type == MOUSEBUTTONUP:
            self.mouse_action_t = 'None'
        if ev.type == MOUSEBUTTONDOWN:
            self.mouse_action_t = \
                'Touched' if self.Itens_texts['text_rect'].collidepoint(
                    point_mouse) else 'None'

    def action(self, type):
        self.check_point(type, 'Hover', self.mouse_action_t)
        self.check_point(type, 'Touched', self.mouse_action_t)

    def check_point(self, type, action, event):
        if type == action:  # check for mouse collision on text
            self.mouse_input = True if event == type else False

    def link(self, link):  # opens a web page when clicked
        if self.mouse_input:
            open_new_tab(link)

    def draw(self):  # Render
        self.render()
