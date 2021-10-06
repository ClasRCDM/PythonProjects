###############
# DEF for game#
###############

from arcade import color, draw_lrtb_rectangle_filled, draw_text


# HUD
def button_play_game(posicao_play_mouse, cena, item, item2):
    if len(posicao_play_mouse) > 0:
        cena.remove(item)
        cena.append(item2)


def animation_menu_start(posicao_play_mouse, cena, play, mover: float):
    if len(posicao_play_mouse) > 0 or play == 'PLayGame':
        cena.move(mover, 0)


def text_screen(text: str, SCREEN_WIDTH: int, SCREEN_HEIGHT: int, BaLa: float):
    draw_lrtb_rectangle_filled(0, BaLa, 527, 490, color.BATTLESHIP_GREY)
    draw_text(text, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75, color.WHITE, font_size=20, anchor_x="center")
    return BaLa


# Gameplay
def move_ground(Sprite1, Sprite2, velocidade: float, x_1: float, x_2: float, mover: bool = False):
    Sprite1.center_x = x_1
    Sprite1.center_x -= velocidade

    Sprite2.center_x = x_2
    Sprite2.center_x -= velocidade if mover else 0


def spawn_kakito(Sprite, SpriteList, point_origin):
    SpriteList.append(Sprite)
    Sprite.center_x = point_origin[0]
    Sprite.center_y = point_origin[1]
    return True


def move_kakitos(SpriteList, speed):
    SpriteList.move(speed, 0)


def game_over(Sprite_gameover, Sprite_restart, SpriteList_view, SpriteList_collision):
    SpriteList_view.append(Sprite_gameover)
    SpriteList_view.append(Sprite_restart)
    SpriteList_collision.append(Sprite_restart)
    Sprite_restart.center_y = 350
