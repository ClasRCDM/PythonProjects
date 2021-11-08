import Class.text as t  # Set Text
import vars as v  # Variables

from pygame import mouse, event


class menu_start():
    def __init__(self):
        pass

    def World_text_menu(self, screen, text_world, font_set):
        # Load/render text menu
        text_world['Start_text'] = t.text(
            screen, font_set, v.text_START, 15,
            v.YELLOW, v.WIDTH / 2, 320, True)  # Press a key to play

    def World_text_menu_events(self, text_world, ev):
        # Check events menu
        text_world['Start_text'].point(mouse.get_pos(), ev)

    def World_text_menu_update(self, text_world):
        # Update text menu
        text_world['Start_text'].animation(
            True, 1, 2, '-zoon', 'one_click', 'Touched')
        text_world['Start_text'].draw()


class footer():
    def __init__(self, screen, font_set: str):
        self.screen = screen

        self.font_set: str = font_set

    def text_dev(self):
        # Load/Render footer menu
        return t.text(
            self.screen, self.font_set, v.text_DEV,
            12, v.WHITE, v.WIDTH / 2 + 105, 520, True)  # by ClasRCDM

    def text_for(self):
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
