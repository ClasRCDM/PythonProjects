import Class.text as t  # Set Text
import vars as v  # Variables

from pygame import mouse


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
    def __init__(self):
        pass

    def World_footer(self, screen, text_world, font_set):
        # Load/Render footer menu
        text_world['DevClasRCDM'] = t.text(
            screen, font_set, v.text_DEV,
            12, v.WHITE, v.WIDTH / 2 + 105, 520, True)  # by ClasRCDM

        text_world['InsJoãoTinti'] = t.text(
            screen, font_set, v.text_FOR,
            11, v.GREY, v.WIDTH / 2 + 115, 550, True)  # by João Tinti

    def World_footer_events(self, text_world, ev):
        text_world['DevClasRCDM'].point(mouse.get_pos(), ev)
        text_world['InsJoãoTinti'].point(mouse.get_pos(), ev)

    def World_footer_update(self, screen, text_world, font_set):
        # Update footer menu
        t.text(screen, font_set, '-Desenvolvido por',
            12, v.WHITE, v.WIDTH / 2 - 65, 520, True)  # Developed
        text_world['DevClasRCDM'].animation(
            True, 1, 1, '+backforth', 'repeat', 'Touched')
        text_world['DevClasRCDM'].draw()
        text_world['DevClasRCDM'].link('https://github.com/ClasRCDM')

        t.text(screen, font_set, '-Projeto inspirado por',
            11, v.GREY, v.WIDTH / 2 - 75, 550, True)  # Project inspired
        text_world['InsJoãoTinti'].animation(
            True, 1, 1, '-backforth', 'repeat', 'Touched')
        text_world['InsJoãoTinti'].draw()
        text_world['InsJoãoTinti'].link('https://github.com/joaotinti75')
