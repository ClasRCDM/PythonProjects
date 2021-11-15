import Class.text as t  # Set Text
import vars as v  # Variables

from pygame import mouse


class start_menu():
    def __init__(self, screen, font_set: str):
        self.screen = screen
        self.font_set: str = font_set

    def start(self):
        # Load/render text menu
        return t.text(
            self.screen, self.font_set, v.text_START, 15,
            v.YELLOW, v.WIDTH / 2, 320, True)  # Press a key to play

    def update(self, text_startmenu):
        # Update text menu
        text_startmenu.animation(
            True, 1, 2, '-zoon', 'one_click', 'Touched')
        text_startmenu.draw()

    def events(self, ev, text_startmenu):
        # Check events menu
        text_startmenu.point(mouse.get_pos(), ev)


class footer():
    def __init__(self, screen, font_set: str):
        self.screen = screen
        self.font_set: str = font_set

    def dev(self):
        # Load/Render footer menu
        return t.text(
            self.screen, self.font_set, v.text_DEV,
            12, v.WHITE, v.WIDTH / 2 + 105, 520, True)  # by ClasRCDM

    def forj(self):
        return t.text(
            self.screen, self.font_set, v.text_FOR,
            11, v.GREY, v.WIDTH / 2 + 115, 550, True)  # by João Tinti

    def events(self, ev, text_dev, text_for):
        text_dev.point(mouse.get_pos(), ev)
        text_for.point(mouse.get_pos(), ev)

    def update(self, text_dev, text_for):
        # Update footer menu
        t.text(self.screen, self.font_set, '-Desenvolvido por',
               12, v.WHITE, v.WIDTH / 2 - 65, 520, True)  # Developed

        text_dev.animation(
            True, 1, 1, '+backforth', 'repeat', 'Touched')
        text_dev.draw()
        text_dev.link('https://github.com/ClasRCDM')

        t.text(self.screen, self.font_set, '-Projeto inspirado por',
               11, v.GREY, v.WIDTH / 2 - 75, 550, True)  # Project inspired
        text_for.animation(
            True, 1, 1, '-backforth', 'repeat', 'Touched')
        text_for.draw()
        text_for.link('https://github.com/joaotinti75')
